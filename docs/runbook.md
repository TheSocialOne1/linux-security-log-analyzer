# Runbook: linux-security-log-analyzer

## How to run
1) Create/activate venv:
- python3 -m venv .venv
- source .venv/bin/activate

2) Run:
- python log_analyzer.py sample_logs/secure.log

## Common issues

### "python: command not found"
Use:
- python3 ...

### Virtualenv not activated
If you don't see `(.venv)` in your prompt:
- source .venv/bin/activate

### Script prints 0 results
Confirm your log file contains the patterns the parser matches (e.g., failed login lines).
