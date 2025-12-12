Summary:	Create legacy-free OS images
Name:		mkosi
Version:	24.3
Release:	2
License:	LGPLv2+
URL:		https://github.com/systemd/mkosi
Source0:	https://github.com/systemd/mkosi/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python >= 3.0
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(pytest)
Requires:	python3dist(xattr)
Requires:	systemd-container
Recommends:	(dnf5 or dnf)
Recommends:	gnupg
Recommends:	xz
Recommends:	tar
Recommends:	cpio
Recommends:	zstd
Recommends:	btrfs-progs
Recommends:	dosfstools
Recommends:	mtools
Recommends:	e2fsprogs
Recommends:	squashfs-tools
Recommends:	cryptsetup
Recommends:	python3dist(argcomplete)
Recommends:	python3dist(cryptography)
Recommends:	python3dist(pexpect)
Recommends:	openssh-clients
Recommends:	socat
Recommends:	openssl
Recommends:	sbsigntools
Recommends:	systemd-repart >= 254
Recommends:	acl
Recommends:	kmod

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
pytest tests/ -v

# just a smoke test for syntax or import errors
PYTHONPATH="%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}" %{buildroot}%{_bindir}/mkosi --help >/dev/null

%files
%license LICENSE
%doc README.md
%{_bindir}/mkosi
%{_bindir}/mkosi-initrd
%{python3_sitelib}/mkosi
%{python3_sitelib}/mkosi-%{version}.dist-info
