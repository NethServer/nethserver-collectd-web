Summary: NethServer python web interface to collectd
Name: nethserver-collectd-web
Version: 1.0.3
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: https://dev.nethesis.it/projects/%{name}

BuildRequires: nethserver-devtools

AutoReq: no
Requires: nethserver-collectd, nethserver-httpd
Requires: perl-CGI, perl-RRD-Simple
Requires: nethserver-lib >= 1.0.3

%description
NethServer python web interface to collectd
See: http://collectdweb.appspot.com

%prep
%setup

%post

%preun

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} $RPM_BUILD_ROOT > e-smith-%{version}-filelist
echo "%doc COPYING"          >> e-smith-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)

%changelog
* Thu May 26 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.3-1
- Access to graphs and reports from trusted network - Bug #3370 [NethServer]

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.2-1.ns6
- Rebuild for 6.5 beta3

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1.ns6
- Rebuild for automatic package handling. #1870

* Thu Feb 21 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> 1.0.0-1
- First release

