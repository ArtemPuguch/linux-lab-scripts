Name:           count-files
Version:        1.0
Release:        1%{?dist}
Summary:        Script to count regular files in /etc

License:        MIT
URL:            https://github.com/ArtemPuguch/linux-lab-scripts
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       bash
Requires:       coreutils
Requires:       findutils

%description
A Bash script that counts the number of regular files
in the /etc directory, excluding directories and symbolic links. It also supports a configuration file for custom paths.

%prep
%setup -q

%install
# Створення бінарної директорії
mkdir -p %{buildroot}%{_bindir}
install -m 755 count_files.sh %{buildroot}%{_bindir}/count_files

# 1. Додавання man-сторінки
mkdir -p %{buildroot}%{_mandir}/man1
cat << 'EOF' > %{buildroot}%{_mandir}/man1/count_files.1
.TH COUNT_FILES 1 "November 2026" "1.0" "User Commands"
.SH NAME
count_files \- counts regular files in /etc
.SH SYNOPSIS
.B count_files
.SH DESCRIPTION
A simple utility script that counts the number of regular files in the target directory (default /etc), excluding directories and symbolic links.
.SH FILES
.I /etc/count-files.conf
Configuration file for specifying custom target directories.
.SH AUTHOR
Artem Puguch
EOF

# 2. Створення конфігураційного файлу у /etc
mkdir -p %{buildroot}%{_sysconfdir}
echo "TARGET_DIR=/etc" > %{buildroot}%{_sysconfdir}/count-files.conf

%pre
# Дії перед встановленням
echo "[INFO] Preparing to install count-files package..."

%post
# Дії після встановлення
echo "[INFO] Package count-files successfully installed!"
if [ -f %{_sysconfdir}/count-files.conf ]; then
    echo "[INFO] Configuration file created at %{_sysconfdir}/count-files.conf"
fi

%files
%{_bindir}/count_files
%config(noreplace) %{_sysconfdir}/count-files.conf
%{_mandir}/man1/count_files.1*

%changelog
* Tue Nov 17 2026 Artem Puguch <artempuguch9@gmail.com> - 1.0-1
- Added man page, configuration file, and %pre/%post installation scripts
