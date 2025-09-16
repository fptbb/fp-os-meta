Name:           fp-os-meta
Version:        1.0
Release:        3%{?dist}
Summary:        A simple meta-package to install dependencies
License:        MIT
BuildArch:      noarch

# Dependencies
Requires:       megatools
Requires:       fuse-encfs
Requires:       yt-dlp
Requires:       coreos-installer
Requires:       gameconqueror
Requires:       nmap-ncat
Requires:       netcat
Requires:       libpcap
Requires:       libnotify
Requires:       iproute
Requires:       freerdp
Requires:       dialog
Requires:       upx
Requires:       tinygo
Requires:       golang
Requires:       gnupg2
Requires:       git
Requires:       buildah
Requires:       code
Requires:       bash-completion
Requires:       powerline-fonts
Requires:       zsh
Requires:       kitty
Requires:       kde-partitionmanager
Requires:       gnome-calculator
Requires:       gnome-disk-utility
Requires:       kleopatra
Requires:       pam-u2f
Requires:       rpm-build
Requires:       rpmdevtools
Requires:       copr-cli

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
* Mon Sep 15 2025 Lucas <lucas@fptbb.com> - 1.0-2
- Added packages
* Mon Sep 15 2025 Lucas <lucas@fptbb.com> - 1.0-1
- Initial package
