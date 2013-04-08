Name:           sensors-lxpanel-plugin
Version:        1.2
Release:        1%{?dist}
Summary:        Monitor temperature/voltages/fan speeds in LXDE through lm-sensors

License:        GPLv3
URL:            http://danamlund.dk/sensors_lxpanel_plugin/
Source0:        http://danamlund.dk/sensors_lxpanel_plugin/%{name}-%{version}.tar.gz

BuildRequires:  lm_sensors-devel
BuildRequires:  lxpanel-devel
BuildRequires:  gtk2-devel

%description
Monitor temperature/voltages/fan speeds in LXDE using lm-sensors

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_libdir}/lxpanel/plugins
install sensors.so %{buildroot}%{_libdir}/lxpanel/plugins

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README
%{_libdir}/lxpanel/plugins/sensors.so



%changelog
* Mon Apr 08 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2-1.R
- Initial release
