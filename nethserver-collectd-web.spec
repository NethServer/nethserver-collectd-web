Summary: NethServer python web interface to collectd
Name: nethserver-collectd-web
Version: 1.0.2
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: https://dev.nethesis.it/projects/%{name}

BuildRequires: nethserver-devtools

Requires: nethserver-collectd, nethserver-httpd
Requires: perl-CGI, perl-RRD-Simple

%description
NethServer python web interface to collectd
See: http://collectdweb.appspot.com

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{version}-%{release}-filelist

%files -f %{version}-%{release}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.2-1.ns6
- Rebuild for 6.5 beta3

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1.ns6
- Rebuild for automatic package handling. #1870

* Thu Feb 21 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> 1.0.0-1
- First release

