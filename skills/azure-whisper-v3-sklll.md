# Azure Whisper v3 Endpoint Smoke Test (Reusable)

## Goal

Quickly verify whether an Azure Speech endpoint can run `whisper-large-v3` with a single transcription request.

## Preconditions

- Workspace has a `.env` file with:
  - `AZURE_SPEECH_ENDPOINT`
  - `AZURE_SPEECH_KEY`
- At least one `.wav` file is available under `TestAudio3.0/`
- Windows PowerShell with `curl.exe` available

## Why this method

PowerShell escaping for multipart JSON is error-prone. The most stable approach is:

1. Write `definition` JSON to a temp file.
2. Use `curl.exe -F` to upload `definition` and `audio` as multipart fields.

This avoids common `Invalid JSON format` failures caused by inline escaping.

## One-shot Smoke Test (PowerShell)

Run from workspace root:

```powershell
Set-Location "d:\dev\test-mazda-asr-multilingual"

# Load .env into current process only
Get-Content .env |
  Where-Object { $_ -match '^[A-Za-z_][A-Za-z0-9_]*=' } |
  ForEach-Object {
    $k, $v = $_ -split '=', 2
    [Environment]::SetEnvironmentVariable($k, $v, 'Process')
  }

$endpoint = ($env:AZURE_SPEECH_ENDPOINT).TrimEnd('/')
$key = $env:AZURE_SPEECH_KEY
$audio = (Get-ChildItem -Path "TestAudio3.0" -Recurse -File -Include *.wav | Select-Object -First 1).FullName

if (-not $endpoint -or -not $key -or -not $audio) {
  Write-Output "Missing endpoint/key/audio"
  exit 1
}

$url = "$endpoint/speechtotext/transcriptions:transcribe?api-version=2024-11-15"
$defPath = Join-Path $PWD "tmp_whisper_def.json"
'{"locales":["de-DE"],"model":"whisper-large-v3"}' | Set-Content -Path $defPath -Encoding utf8

curl.exe -sS -D - -X POST "$url" \
  -H "Ocp-Apim-Subscription-Key: $key" \
  -F "definition=@$defPath;type=application/json" \
  -F "audio=@$audio;type=audio/wav"

Remove-Item $defPath -Force
```

## Success Criteria

- HTTP status is `200 OK`
- Response body contains at least one of:
  - `combinedPhrases`
  - `phrases`
  - recognized text fields

## Language Specification (Verified)

Yes, language can be explicitly specified for Whisper v3 in this endpoint by setting `locales` in `definition`.

Validated on 2026-05-09 with:

- `model`: `whisper-large-v3`
- `locales`: `["de-DE"]`
- Result: `HTTP=200`, response included `phrases[0].locale=de-DE`

To test another language, change only this JSON:

```json
{"locales":["en-GB"],"model":"whisper-large-v3"}
```

Examples:

- German: `de-DE`
- British English: `en-GB`
- French: `fr-FR`
- Spanish: `es-ES`
- Italian: `it-IT`

## Common Failures

- `HTTP 400` + `Invalid JSON format`:
  - `definition` multipart content is malformed.
  - Use temp JSON file upload method above.
- `401/403`:
  - Invalid key, key-endpoint mismatch, or permission issue.
- Endpoint is null in shell:
  - `.env` not loaded in current process.

## Optional: 5-sample quick stability check

Run this PowerShell block to test first 5 wav files with `whisper-large-v3` and print success rate + average latency:

```powershell
Set-Location "d:\dev\test-mazda-asr-multilingual"

# Load .env into current process
Get-Content .env |
  Where-Object { $_ -match '^[A-Za-z_][A-Za-z0-9_]*=' } |
  ForEach-Object {
    $k, $v = $_ -split '=', 2
    [Environment]::SetEnvironmentVariable($k, $v, 'Process')
  }

$endpoint = ($env:AZURE_SPEECH_ENDPOINT).TrimEnd('/')
$key = $env:AZURE_SPEECH_KEY
if (-not $endpoint -or -not $key) {
  Write-Output "Missing endpoint/key"
  exit 1
}

$url = "$endpoint/speechtotext/transcriptions:transcribe?api-version=2024-11-15"
$defPath = Join-Path $PWD "tmp_whisper_def.json"
'{"locales":["de-DE"],"model":"whisper-large-v3"}' | Set-Content -Path $defPath -Encoding utf8

$files = Get-ChildItem -Path "TestAudio3.0" -Recurse -File -Include *.wav | Select-Object -First 5
if (-not $files -or $files.Count -eq 0) {
  Write-Output "No wav files found"
  Remove-Item $defPath -Force -ErrorAction SilentlyContinue
  exit 1
}

$ok = 0
$times = @()

foreach ($f in $files) {
  $bodyPath = Join-Path $PWD "tmp_whisper_body.json"
  $sw = [System.Diagnostics.Stopwatch]::StartNew()
  $code = & curl.exe -sS -o "$bodyPath" -w "%{http_code}" -X POST "$url" `
    -H "Ocp-Apim-Subscription-Key: $key" `
    -F "definition=@$defPath;type=application/json" `
    -F "audio=@$($f.FullName);type=audio/wav"
  $sw.Stop()

  $ms = [math]::Round($sw.Elapsed.TotalMilliseconds, 1)
  $times += $ms
  if ($code -eq "200") { $ok += 1 }

  Write-Output ("FILE=" + $f.Name + " HTTP=" + $code + " LATENCY_MS=" + $ms)
  Remove-Item $bodyPath -Force -ErrorAction SilentlyContinue
}

$total = $files.Count
$avg = [math]::Round((($times | Measure-Object -Average).Average), 1)
$rate = [math]::Round(($ok * 100.0 / $total), 1)
Write-Output "--- SUMMARY ---"
Write-Output ("SUCCESS=" + $ok + "/" + $total + " (" + $rate + "%)")
Write-Output ("AVG_LATENCY_MS=" + $avg)

Remove-Item $defPath -Force -ErrorAction SilentlyContinue
```

Interpretation:

- If success rate is near `100%`, endpoint/model is stable for smoke-level validation.
- If many non-200 responses occur, verify key-endpoint pairing and request quota first.

## Notes

- This is a pure smoke test for endpoint/model availability.
- It is not intended for WER/latency benchmarking.
