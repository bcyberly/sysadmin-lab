# Learning Log – sysadmin-lab

*This log is a continuation of my daily progress documentation. Days 1–14 cover the development of my [Network Toolkit](https://github.com/bcyberly/Network_Toolkit) and foundational networking concepts. You can find those entries in the [Network_Toolkit LEARNING_LOG.md](https://github.com/bcyberly/Network_Toolkit/blob/main/docs/LEARNING_LOG.md).*

---

## [2026-03-01] – Day 15: Environment Setup

### Tasks Completed
- Created two new GitHub repositories: [`sysadmin-lab`](https://github.com/bcyberly/sysadmin-lab) and [`ctf-writeups`](https://github.com/bcyberly/ctf-writeups).
- Cloned `sysadmin-lab` locally and set up the basic folder structure (`src/`, `docs/`, `tests/`, `src/scripts/`).
- Added `psutil` to `requirements.txt` for future system monitoring scripts.
- Made the initial commit: `chore: initial repo structure for OS internals`.
- Set up a Linux Ubuntu 22.04 LTS virtual machine using VirtualBox.
- Ensured SSH was enabled and tested connectivity from the Windows host.
- Installed essential monitoring and debugging tools inside the VM: `strace`, `lsof`, `sysstat`, and (attempted) `htop` (accidentally typed `hotp` but corrected later).
- On the Windows side, downloaded and extracted the **Sysinternals Suite** to `C:\Tools\Sysinternals` and added it to the system PATH.

### Commands Used

**Linux VM setup (inside VM):**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install openssh-server -y
sudo apt install htop strace lsof sysstat -y
```

**Windows side (PowerShell as Admin):**
```powershell
# Enable WSL2 (if not already)
wsl --install
wsl --set-default-version 2

# Extract Sysinternals Suite (example)
Expand-Archive -Path .\SysinternalsSuite.zip -DestinationPath C:\Tools\Sysinternals
```

### Screenshots

- **System update in Ubuntu VM:**  
  ![Ubuntu update](images/linux_update_system.png)
- **Installing basic monitoring tools:**  
  ![Installing tools](images/basic_tools_monitoring_and_debugging.png)  
  *(Note: I typed `hotp` by mistake, but the actual tool is `htop`. I corrected it later.)*

### Reflection
- The repository structure follows the same pattern I used for the `Network_Toolkit` project – keeping code, docs, and tests separate feels natural now.
- Setting up the Linux VM was straightforward; the key takeaway is to use a generic hostname (`user-VirtualBox` in the screenshots) to avoid leaking personal info when sharing screenshots.
- Installing the Sysinternals Suite gives me access to powerful Windows internals tools like Process Explorer and Process Monitor – I’ll explore them in later labs.
- This environment is now ready for deeper exploration of processes, system calls, and filesystem internals.

---