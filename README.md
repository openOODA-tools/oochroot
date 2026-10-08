# oochroot: Sovereign ROOT JAIL

<div align="center">

```
================================================================================
                                oochroot
                Sovereign openOODA ROOT JAIL & CONFINEMENT
================================================================================
```

**Sovereign ROOT JAIL**  
*Sets up capability-bounded root filesystem jail with pivot_root semantics and systemd confinement synthesis.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oochroot/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oochroot-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oochroot/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oochroot/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oochroot-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oochroot/uninstall.sh | bash
```

---

## 2. CLI Usage

```
oochroot 0.2.0 (openOODA sovereign container & jail)
usage: oochroot [OPTION]... NEWROOT [COMMAND [ARG]...]
  or:  oochroot [OPTION]... --demo

Run COMMAND with root directory set to NEWROOT or inspect jail confinement.

Options:
  -u, --userspec=USER:GROUP  specify user and group (ID or name) to use
      --mount-api-vfs        mount API virtual filesystems (/proc, /sys, /dev)
      --systemd              synthesize declarative systemd service unit
      --audit                audit root filesystem for jailbreak vulnerabilities
      --dry-run              simulate chroot setup and print confinement plan
      --demo                 run demonstration scenarios with synthetic fixtures
      --json                 output formatted as JSON telemetry
  -h, --help                 display this help and exit
  -V, --version              output version information and exit
      --mcp                  run as Model Context Protocol stdio server
```

---

## 3. Declarative systemd Confinement Synthesis

Following pure systemd-native server architecture, `oochroot` emits declarative service unit definitions utilizing `RootDirectory=`, `MountAPIVFS=yes`, and kernel sandboxing directives:

```bash
# Synthesize declarative systemd service unit for container jail:
oochroot --systemd -u sandbox:sandbox --mount-api-vfs /var/lib/jails/app /bin/sh
```

Output:
```ini
# /etc/systemd/system/oochroot-jail.service
# Generated declaratively by oochroot v0.2.0
[Unit]
Description=Sovereign Container Jail (oochroot-jail)
Documentation=man:oochroot(1) https://openooda-tools.github.io/oochroot
After=local-fs.target

[Service]
Type=exec
RootDirectory=/var/lib/jails/app
MountAPIVFS=yes
ProtectSystem=strict
ProtectHome=yes
PrivateTmp=yes
NoNewPrivileges=yes
PrivateDevices=false
User=sandbox:sandbox
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
ExecStart=/bin/sh
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oochroot` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

```bash
oochroot --mcp
```

### Registered Tools
* **`chroot_inspect`**: Inspect candidate root directory layout, essential hierarchy, and shell availability.
* **`chroot_plan`**: Plan pseudofs mount points and isolation parameters for root jail.
* **`chroot_systemd`**: Synthesize declarative systemd service unit with `RootDirectory` confinement.
* **`chroot_audit`**: Audit root directory against jailbreak vectors and device node leaks.
* **`chroot_verify`**: Validate complete jail configuration and compute readiness score.

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
