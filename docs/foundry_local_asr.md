# Foundry Local ASR Evaluation

This benchmark includes two local Foundry services:

- `foundry_whisper_v3`: file transcription through `audio_client.transcribe(file)`.
- `foundry_nemotron_asr`: live transcription session that streams 16 kHz mono PCM chunks.

## Setup

Install Foundry Local dependencies:

```powershell
pip install -r requirements-foundry.txt
foundry service status
foundry model list | Select-String -Pattern 'whisper|nemotron|speech|asr' -CaseSensitive:$false
```

Default model aliases are based on the local catalog available during testing:

```powershell
$env:FOUNDRY_WHISPER_MODEL_ALIAS = 'whisper-large-v3-turbo'
$env:FOUNDRY_NEMOTRON_MODEL_ALIAS = 'nemotron-3.5-asr-streaming-0.6b'
```

The adapter defaults to CPU variants because the local CUDA variants failed on this machine with cuDNN runtime errors. To try GPU again after updating Foundry Local, CUDA, or drivers:

```powershell
$env:FOUNDRY_DEVICE = 'gpu'
```

Use `FOUNDRY_DEVICE=cpu` or unset the variable to return to the stable CPU path.

## Language Handling

By default the adapter passes the benchmark locale language subtag to Foundry Local, for example `de-DE` becomes `de`. To force auto-detection for all locales:

```powershell
$env:FOUNDRY_LANGUAGE = 'auto'
```

The tested Foundry Local models were stable enough for the default benchmark set on `en-GB`, `es-ES`, `fr-FR`, `it-IT`, and `pl-PL`. Keep `de-DE`, `nb-NO`, `nl-NL`, and `sv-SE` as optional diagnostic runs for now: the smoke results completed without runtime errors, but WER was high or language handling was unstable, especially for `nb-NO` where `nb` produced English hallucinations on some clips.

## Commands

One sample per dataset across the default Foundry-supported language set:

```powershell
python -X utf8 run_full.py --languages en-GB es-ES fr-FR it-IT pl-PL --max-per-dataset 1 --services foundry_whisper_v3 foundry_nemotron_asr --workers 1 --tag foundry_cpu --no-pace
```

Full 30-sample run across the default Foundry-supported language/scenario datasets:

```powershell
python -X utf8 run_full.py --languages en-GB es-ES fr-FR it-IT pl-PL --max-per-dataset 30 --services foundry_whisper_v3 foundry_nemotron_asr --workers 1 --tag foundry_cpu_full --no-pace
```

Optional weak-support diagnostic run:

```powershell
python -X utf8 run_full.py --languages de-DE nb-NO nl-NL sv-SE --max-per-dataset 5 --services foundry_whisper_v3 foundry_nemotron_asr --workers 1 --tag foundry_cpu_weak_langs --no-pace
```

On the tested CPU path, the one-sample run took roughly 1 minute per language after models were loaded. A full 30-sample run can take several hours locally.

## References

- <https://learn.microsoft.com/en-us/azure/foundry-local/how-to/how-to-transcribe-audio?tabs=windows&pivots=programming-language-python>
- <https://learn.microsoft.com/en-us/azure/foundry-local/how-to/how-to-live-transcribe-audio?tabs=windows&pivots=programming-language-python>