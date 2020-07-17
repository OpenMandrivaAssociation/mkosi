Summary:	Create legacy-free OS images
Name:		mkosi
Version:	5
Release:	2
License:	LGPLv2+
URL:		https://github.com/systemd/mkosi
Source0:	https://github.com/systemd/mkosi/archive/v%{version}/%{name}-%{version}.tar.gz
# (tpg) sent upstream https://github.com/systemd/mkosi/pull/454
Patch0:		mkosi-5-addopenmandriva-support.patch
BuildArch:	noarch
ExclusiveArch:	%{x86_64}
BuildRequires:	python >= 3.0
Recommends:	dnf
Recommends:	debootstrap
#Recommends:	arch-install-scripts
#Recommends:	edk2-ovmf
Recommends:	gnupg
Recommends:	xz
Recommends:	tar
Recommends:	btrfs-progs
Recommends:	dosfstools
Recommends:	e2fsprogs
Recommends:	squashfs-tools
Recommends:	cryptsetup

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
# no build required

%install
# It's just one file, and setup.py install would copy useless .egg-info
install -Dpt %{buildroot}%{_bindir}/ mkosi

%files
%license LICENSE
%doc README.md
%_bindir/mkosi

%check
# just a smoke test for syntax or import errors
%{buildroot}%{_bindir}/mkosi --help
