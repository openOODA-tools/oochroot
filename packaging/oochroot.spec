Name:           oochroot
Version:        0.2.0
Release:        1%{?dist}
Summary:        Sovereign ROOT JAIL and capability-bounded container confinement manager.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oochroot
Source0:        oochroot-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oochroot is a sovereign, capability-bounded ROOT JAIL and isolation
manager written in pure openOODA, featuring zero ambient authority,
systemd service confinement synthesis, and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oochroot
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oochroot-uninstall

%files
/usr/bin/oochroot
/usr/bin/oochroot-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevation to pure openOODA v0.2.0 with systemd confinement synthesis and MCP server
