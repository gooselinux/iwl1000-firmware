Name:           iwl1000-firmware
Version:        128.50.3.1
Release:        1.1%{?dist}
Summary:        Firmware for Intel® PRO/Wireless 1000 B/G/N network adaptors

Group:          System Environment/Kernel
License:        Redistributable, no modification permitted
URL:            http://intellinuxwireless.org/
Source0:        http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-1000-ucode-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch


%description
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl1000 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%prep
%setup -c -q

pushd iwlwifi-1000-ucode-%{version}
# Change encoding
sed -i 's/\r//'  LICENSE.iwlwifi-1000-ucode README.iwlwifi-1000-ucode
# Rename docs
mv LICENSE.iwlwifi-1000-ucode ../LICENSE
mv README.iwlwifi-1000-ucode ../README
# Preserve timestamp
touch -r *.ucode ../LICENSE ../README
popd


%build
# Nothing to build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib/firmware
pushd iwlwifi-1000-ucode-%{version}
install -pm 0644 *.ucode $RPM_BUILD_ROOT/lib/firmware/
popd


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE README
/lib/firmware/*.ucode


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 128.50.3.1-1.1
- Rebuilt for RHEL 6

* Wed Sep 16 2009 John W. Linville <linville@tuxdriver.com> - 128.50.3.1-1
- Initial import
