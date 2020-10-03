Name: bluetooth-rfkill-event
Summary: Bluetooth rfkill event daemon
URL: https://downloadcenter.intel.com/Detail_Desc.aspx?DwnldID=24389
Version: 1.0
Release: 1
License: GPLv2
Source0: %{name}-%{version}.tar.bz2
Requires: bluez-libs
Requires: glib2
Requires: broadcom-bluetooth
Requires: bluetooth-rfkill-event-configs
BuildRequires: bluez-libs-devel
BuildRequires: glib2-devel
BuildRequires: systemd

%description
Bluetooth rfkill event daemon. Part of Intel Edison GPL/LGPL sources.

%package configs-mer
Summary:    Default configuration for bluetooth-rfkill-event
Requires:   %{name} = %{version}-%{release}
Provides:   bluetooth-rfkill-event-configs

%description configs-mer
This package provides default configuration for bluetooth-rfkill-event

%prep
%setup -q -n %{name}-%{version}/bluetooth-rfkill-event

%build
%make_build

%install
rm -rf %{buildroot}
%make_install INSTALL_ROOT=%{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/bluetooth_rfkill_event
%{_unitdir}/bluetooth-rfkill-event.service
%{_unitdir}/network.target.wants/bluetooth-rfkill-event.service

%files configs-mer
%defattr(-,root,root,-)
%dir %{_sysconfdir}/bluetooth-rfkill-event
%{_sysconfdir}/sysconfig/bluetooth-rfkill-event
