# Egress Network Port Tester

The script is designed to test egress (outbound) network connectivity by attempting to establish TCP connections to specified ports on a given host. It provides feedback on whether each connection attempt is successful or fails. The intent is to support quickly testing egress filtering or to aid in troubleshooting connectivity issues.


### Compiling

Compiling the script into a standalone executable can be accomplished using Nuitka:

```
python -m nuitka --onefile script.py\
```

## Tasks
- [x] Add command-line arguments
- [ ] Compile using Nuitka
- [ ] General review and expansion
