Name:           fp-os-meta
Version:        1.0
Release:        1%{?dist}
Summary:        A simple meta-package to install dependencies
License:        MIT
BuildArch:      noarch

# This is the important part — dependencies you want installed:
Requires:       bash
Requires:       coreutils
Requires:       ffmpeg
Requires:       yadm

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
* Mon Sep 15 2025 Lucas <you@example.com> - 1.0-1
- Initial package
