Name:           fp-os-meta
Version:        1.0
Release:        6%{?dist}
Summary:        A simple meta-package to install dependencies
License:        MIT
BuildArch:      noarch

# Dependencies
# Enables tab-completion for many CLI tools
Requires:       bash-completion
# Build OCI/Docker images without needing a daemon
Requires:       buildah
# Visual Studio Code IDE for development
Requires:       code
# Manage Fedora COPR repositories from the command line
Requires:       copr-cli
# Tool to install Fedora CoreOS systems
Requires:       coreos-installer
# Show text-based UI dialogs in shell scripts
Requires:       dialog
# Dolphin integration for revision control systems, Dropbox, and disk images.
Requires:       dolphin-plugins
# Encrypted filesystem support via FUSE
Requires:       fuse-encfs
# Cheat Engine for Linux (debug and memory edit)
Requires:       gameconqueror
# Distributed version control system
Requires:       git
# Simple desktop calculator
Requires:       gnome-calculator
# GUI for disk management
Requires:       gnome-disk-utility
# OpenPGP encryption and signing tools
Requires:       gnupg2
# Heimdall is a utility to flash firmware on to Galaxy S devices
Requires:       heimdall
# Networking utilities like ip addr and ip route
Requires:       iproute
# GUI tool to manage disk partitions
Requires:       kde-partitionmanager
# Extremely fast, GPU-accelerated terminal emulator
Requires:       kitty
# Certificate and key management tool
Requires:       kleopatra
# Send desktop notifications from scripts and apps
Requires:       libnotify
# Packet capture library for network sniffing tools
Requires:       libpcap
# Access MEGA.nz cloud storage from CLI
Requires:       megatools
# TCP/UDP swiss-army knife for networking
Requires:       netcat
# The nextcloud desktop client dolphin extension.
Requires:       nextcloud-client-dolphin
# Alternative netcat implementation (comes with nmap)
Requires:       nmap-ncat
# YubiKey and FIDO U2F authentication for PAM
Requires:       pam-u2f
# KDE and Plasma resources management GUI.
Requires:       plasma-discover
# Patched fonts with powerline symbols
Requires:       powerline-fonts
# The official Linux CLI for ProtonVPN.
Requires:       protonvpn-cli
# Tools to build RPM packages
Requires:       rpm-build
# Developer tools for RPM packaging
Requires:       rpmdevtools
# Small Go compiler for microcontrollers and WebAssembly
Requires:       tinygo
# Ultimate Packer for Executables (binary compressor)
Requires:       upx
# Powerful video downloader with YouTube support
Requires:       yt-dlp
# Feature-rich shell with scripting capabilities
Requires:       zsh

%description
This is a dummy package that doesn’t ship anything itself, but pulls in
the required dependencies.

%prep
# nothing

%build
# nothing

%install
mkdir -p %{buildroot}%{_docdir}/%{name}
echo "This is a meta-package that installs dependencies." > %{buildroot}%{_docdir}/%{name}/README

%files
%doc %{_docdir}/%{name}

%changelog
* Mon Oct 27 2025 Lucas <lucas@fptbb.com> - 1.0-6
- Regenerated package list
