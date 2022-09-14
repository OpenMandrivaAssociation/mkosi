Summary:	Create legacy-free OS images
Name:		mkosi
Version:	13
Release:	3
License:	LGPLv2+
URL:		https://github.com/systemd/mkosi
Source0:	https://github.com/systemd/mkosi/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python >= 3.0
BuildRequires:	python3dist(setuptools)
Requires:	python3dist(xattr)
Requires:	systemd-container
Recommends:	dnf
Recommends:	gnupg
Recommends:	xz
Recommends:	tar
Recommends:	cpio
Recommends:	zstd
Recommends:	btrfs-progs
Recommends:	dosfstools
Recommends:	e2fsprogs
Recommends:	squashfs-tools
Recommends:	cryptsetup
Recommends:	python3dist(argcomplete)
Recommends:	python3dist(cryptography)
Recommends:	python3dist(pexpect)

%description
A fancy wrapper around "dnf --installroot", "debootstrap" and
"pacstrap", that may generate disk images with a number of bells and
whistles.

Generated images are "legacy-free". This means only GPT disk labels
(and no MBR disk labels) are supported, and only systemd based images
may be generated. Moreover, for bootable images only EFI systems are
supported (not plain MBR/BIOS).

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

%check
# just a smoke test for syntax or import errors
%{buildroot}%{_bindir}/mkosi --help

%files
%license LICENSE
%doc README.md
%{_bindir}/mkosi
%{python3_sitelib}/mkosi
%{python3_sitelib}/mkosi-%{version}-py*.egg-info/
%doc %{_mandir}/man1/mkosi.1*
