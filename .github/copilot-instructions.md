# Agent Instructions

## Speech Service and SDK Issue Reporting

When investigating Azure Speech service, Speech SDK, STT, TTS, Translation, or Voice Live failures in this repository, collect enough evidence to make the report actionable before suggesting or drafting a GitHub issue.

Use the Azure Speech SDK samples issue tracker for SDK bugs, sample bugs, documentation problems, and feature requests:

https://github.com/Azure-Samples/cognitive-services-speech-sdk/issues

Do not route every Speech problem to GitHub. Use this channel split:

| Issue type | Best channel |
| --- | --- |
| SDK bug / sample bug | GitHub Issue |
| Documentation problem | GitHub Issue |
| Feature request | GitHub Issue |
| Customer production outage | Azure Support Ticket |
| Resource-specific failure | Azure Support Ticket |
| Billing/SLA | Azure Support Ticket |

### Evidence From Test Runs

Benchmark CSVs already include `request_id` and `session_id` columns. Use those fields, plus the realtime `_words.jsonl` sidecar when present, before drafting any Speech SDK or service issue. REST services should contain `apim-request-id` or another response header ID; realtime SDK rows should contain `SessionId` and may use `ResultId` as the closest correlating ID when `SpeechServiceResponse_RequestId` is unavailable.

When drafting an issue, also include timestamp, region, endpoint type, SDK version, language SDK, OS, locale, auth type, test command, input sample ID, and exact error/cancellation details. If any ID field is blank, say so explicitly instead of inventing one.

### GitHub Issue Template

Use this structure when drafting GitHub issues for Speech SDK or Speech service behavior questions that belong on GitHub:

````markdown
## Issue Summary
Short description of the problem.

Example:
SpeechRecognizer intermittently returns NoMatch after 30-60 minutes of continuous streaming.

## Impact
- Service: STT / TTS / Translation / Voice Live
- Severity: High / Medium / Low
- Customer impact:
- Frequency:
- Production or test:

## Environment
- SDK Version:
- Language SDK: Python / C# / Java / JS / C++
- OS:
- Region:
- Endpoint:
- Authentication:
- Network environment:

## Steps to Reproduce
1.
2.
3.
4.

## Expected Behavior
What should happen.

## Actual Behavior
What actually happens.

## Error Messages
Paste exact error message.

```text
ERROR: ...
RequestId: ...
SessionId: ...
```

## Logs and Artifacts
- Test command:
- Input sample or manifest row:
- SDK logs / service logs:
- Minimal repro link or snippet:
````

Before filing, check current open issues for similar SDK bugs, STT/TTS behavior questions, Python/Java/C# SDK problems, translation issues, threading issues, memory leaks, and sample defects. If the impact is a production outage, resource-specific failure, or billing/SLA concern, advise using an Azure Support Ticket instead of GitHub.