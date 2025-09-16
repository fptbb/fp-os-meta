#!/usr/bin/env python3
import json
import re
import sys
from datetime import datetime
from pathlib import Path

# Paths
SPEC_FILE = Path("rpms/meta.spec")
PACKAGES_FILE = Path("packages.json")

# Metadata
NAME = "fp-os-meta"
VERSION = "1.0"
LICENSE = "MIT"
SUMMARY = "A simple meta-package to install dependencies"
BUILDARCH = "noarch"

def read_release_number():
    """Reads the current Release number from the spec file, returns 0 if missing."""
    if not SPEC_FILE.exists():
        return 0
    text = SPEC_FILE.read_text()
    match = re.search(r"^Release:\s*(\d+)", text, re.MULTILINE)
    return int(match.group(1)) if match else 0

def generate_spec(packages, release):
    """Generates the .spec file content from package data and release number."""
    date = datetime.now().strftime("%a %b %d %Y")
    changelog_entry = f"* {date} Lucas <lucas@fptbb.com> - {VERSION}-{release}\n- Regenerated package list"

    sorted_packages = sorted(packages, key=lambda x: x["package"].lower())
    requires_lines = "\n".join(
        f"# {pkg['comment']}\nRequires:       {pkg['package']}"
        for pkg in sorted_packages
    )

    spec = f"""Name:           {NAME}
Version:        {VERSION}
Release:        {release}%{{?dist}}
Summary:        {SUMMARY}
License:        {LICENSE}
BuildArch:      {BUILDARCH}

# Dependencies
{requires_lines}

%description
This is a dummy package that doesn’t ship anything itself, but pulls in
the required dependencies.

%prep
# nothing

%build
# nothing

%install
mkdir -p %{{buildroot}}%{{_docdir}}/%{{name}}
echo "This is a meta-package that installs dependencies." > %{{buildroot}}%{{_docdir}}/%{{name}}/README

%files
%doc %{{_docdir}}/%{{name}}

%changelog
{changelog_entry}
"""
    return spec

def main():
    json_file = Path(sys.argv[1]) if len(sys.argv) > 1 else PACKAGES_FILE
    if not json_file.exists():
        print(f"Error: {json_file} not found")
        sys.exit(1)

    data = json.loads(json_file.read_text())
    if not isinstance(data, list) or not all(isinstance(p, dict) and "package" in p for p in data):
        print("Error: JSON must be a list of objects with 'package' and 'comment' keys")
        sys.exit(1)

    release = read_release_number() + 1
    spec_content = generate_spec(data, release)

    SPEC_FILE.parent.mkdir(parents=True, exist_ok=True)
    SPEC_FILE.write_text(spec_content)
    print(f"✅ Wrote updated spec to {SPEC_FILE} (release {release})")

if __name__ == "__main__":
    main()
