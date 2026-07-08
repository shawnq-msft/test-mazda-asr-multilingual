# Hojo-ASR-V1 Azure GPU Evaluation

This benchmark can run HojoAI Hojo-ASR-V1 as an offline service named `hojo_asr`.

## Model Fit

Hojo-ASR-V1 is Apache-2.0 and the model card lists support for Mandarin, English, Cantonese, and Sichuan dialect. In this repository, only `en-GB` is clearly inside that language coverage. Treat the other Mazda locales (`de-DE`, `es-ES`, `fr-FR`, `it-IT`, `nb-NO`, `nl-NL`, `pl-PL`, `sv-SE`) as out-of-coverage stress tests unless Hojo publishes broader European-language support.

Primary readout:

- Accuracy: WER/SER by locale and scenario, compared against the existing `fast_mai_1`, `fast_mai_1.5`, `whisper_v3`, and `realtime` baselines.
- Latency: `lbl_ms` records local `model.run_infer` wall time after model load. Do not compare Hojo `lbl_ms` directly to Azure network service UPL without a separate serving/streaming setup.
- GPU sizing: report average samples/sec or clips/sec separately from WER if throughput matters.

## Azure GPU Request

Request one Linux GPU VM for a short evaluation run.

Current subscription status from provisioning attempts:

- Automatic quota increases for CUDA GPU families were not available in this subscription. `Standard NCASv3_T4 Family` in `westus2`, `Standard NCADS_A100_v4 Family` in `southcentralus`, and `Standard NCadsH100v5 Family` in `westus` all required support escalation.
- Creating a Spot `Standard_NC4as_T4_v3` VM in `westus2` also failed with regional capacity restrictions.
- The Azure CLI support API is blocked by the subscription support plan: `az support in-subscription tickets create` returns `InvalidSupportPlan` for the current Free support plan.
- `NVv4` SKUs may show quota, but they are graphics/virtualization-oriented AMD GPU VMs and are not an appropriate CUDA target for Hojo-ASR-V1.

Use the Azure Portal quota/support flow unless the subscription gets a paid support plan that enables the support API.

Recommended starting SKU:

- `Standard_NC24ads_A100_v4` if available: 1x A100 80 GB, safest for a Qwen3-decoder ASR model.
- `Standard_NC6s_v3` or `Standard_NC24s_v3` if quota is easier: V100 class, likely acceptable for batch size 1-4 but may need slower throughput.
- `Standard_NVadsA10_v5` if A10 quota is the easiest path: good fallback for functional testing.

Disk and image:

- Ubuntu 22.04 LTS
- NVIDIA driver/CUDA image if your Azure subscription offers it, otherwise install drivers after provisioning
- 256 GB OS disk or a separate data disk if caching Hugging Face models locally

Request text:

```text
Need one temporary Azure GPU VM to evaluate HojoAI/Hojo-ASR-V1, an Apache-2.0 open-source ASR model, against the Mazda multilingual command dataset. The run is offline inference only; no training. Expected workload is roughly 9 locales x up to 9 scenarios x 30 audio clips per scenario. Preferred SKU: Standard_NC24ads_A100_v4; fallback: NC24s_v3, NC6s_v3, or NVadsA10_v5. Need quota for 1 VM for 1-2 days plus enough disk to cache the Hugging Face model.
```

Minimum quota request for the current blocked path:

```text
Quota type: Compute VM cores
Region: westus2
VM family: Standard NCASv3_T4 Family vCPUs
Requested limit: 4 vCPUs
Target VM size: Standard_NC4as_T4_v3
Reason: Temporary CUDA GPU VM for HojoAI/Hojo-ASR-V1 offline ASR benchmark. Inference only, no training. Automatic quota request failed with QuotaNotAvailableForResource, and Spot creation failed with SkuNotAvailable/capacity restrictions.
```

After quota approval, create the VM with:

```powershell
az vm create --resource-group rg-hojo-asr-gpu-wus2 --name vm-hojo-asr-t4-wus2 --location westus2 --image Canonical:0001-com-ubuntu-server-jammy:22_04-lts-gen2:22.04.202606110 --size Standard_NC4as_T4_v3 --admin-username azureuser --ssh-key-values $HOME\.ssh\id_rsa.pub --os-disk-size-gb 256 --storage-sku Premium_LRS --public-ip-sku Standard --tags workload=hojo-asr purpose=benchmark owner=shawn gpu=t4 --output json
```

## VM Setup

```bash
sudo apt-get update
sudo apt-get install -y git git-lfs ffmpeg python3.10-venv
sudo apt-get install -y nvidia-driver-535 || true
nvidia-smi

git clone <this-repo-url>
cd test-mazda-asr-multilingual
python3.10 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements-hojo.txt
```

Download the model once on the VM:

```bash
huggingface-cli download HojoAI/Hojo-ASR-V1 --local-dir /mnt/models/Hojo-ASR-V1
export HOJO_MODEL_PATH=/mnt/models/Hojo-ASR-V1
export HOJO_DEVICE=cuda:0
export HOJO_BATCH_SIZE=1
```

## Smoke Test

Run one sample per dataset for the in-coverage English locale first:

```bash
python -X utf8 run_full.py --languages en-GB --max-per-dataset 1 --services hojo_asr --workers 1 --tag hojo_smoke
```

If that works, run the main English comparison:

```bash
python -X utf8 run_full.py --languages en-GB --max-per-dataset 30 --services hojo_asr --workers 1 --tag hojo
```

Then run the out-of-coverage multilingual stress pass:

```bash
python -X utf8 run_full.py --languages de-DE es-ES fr-FR it-IT nb-NO nl-NL pl-PL sv-SE --max-per-dataset 30 --services hojo_asr --workers 1 --tag hojo
```

Use `--workers 1` for the current adapter because the model is shared in-process and protected by an inference lock. Increase `HOJO_BATCH_SIZE` only after the smoke test passes and GPU memory is stable.

## Regenerate Reports

Reports and error analysis are generated automatically by `run_full.py`. To regenerate from CSVs:

```bash
python -X utf8 -c "
from pathlib import Path
from benchmark.report import build_report
from scripts.error_analysis import main as error_main
for csv_path in sorted(Path('results').glob('hojo_*.csv')):
    build_report(csv_path, csv_path.with_name(csv_path.stem + '_report.md'))
    error_main(csv_path, csv_path.with_name(csv_path.stem + '_error_analysis.md'))
"
```

## Expected Interpretation

A useful decision threshold is:

- `en-GB`: Hojo should be compared seriously if WER is near the current best baseline, around 0.13 on the latest run.
- Other locales: poor WER is not necessarily a model failure because they are outside the stated model coverage. Use those runs to document behavior, not to reject the model for supported languages.
- If Hojo has strong English WER but weak European-language WER, the next step is either language-specific fine-tuning or choosing a multilingual ASR model with explicit European-language support.
