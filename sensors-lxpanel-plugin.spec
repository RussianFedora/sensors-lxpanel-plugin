Name:           sensors-lxpanel-plugin
Version:        1.7
Release:        1%{?dist}
Summary:        Monitor temperature/voltages/fan speeds in LXDE through lm-sensors

License:        GPLv2
URL:            http://danamlund.dk/sensors_lxpanel_plugin/
Source0:        http://danamlund.dk/sensors_lxpanel_plugin/%{name}-%{version}.tar.gz

BuildRequires:  lm_sensors-devel
BuildRequires:  lxpanel-devel
BuildRequires:  gtk2-devel

Requires:       lxpanel

%description
Monitor temperature/voltages/fan speeds in LXDE using lm-sensors

%prep
%setup -q
echo '#!/bin/bash' > configure
chmod +x configure


%build
%configure
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_libdir}/lxpanel/plugins
%make_install


%files
%doc README COPYING
%{_libdir}/lxpanel/plugins/sensors.so



%changelog
* Tue Jun 04 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 1.7-1.R
- Update to 1.7

* Tue Jun 04 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4-1.R
- Update to 1.4

* Mon Apr 08 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3-1.R
- Update to 1.3

* Mon Apr 08 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2-1.R
- Initial release
