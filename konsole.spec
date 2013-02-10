Name:		konsole
Summary:	A terminal emulator similar to xterm for KDE
Version:	4.10.0
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
URL:		http://konsole.kde.org/
%define is_beta %(if test `echo %version |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-devel
Requires:	kdebase4-runtime
Requires:	x11-font-misc-misc

%description
A terminal emulator, similar to xterm, for KDE.

%files
%doc README COPYING COPYING.DOC COPYING.LIB doc/*
%{_kde_bindir}/konsole
%{_kde_bindir}/konsoleprofile
%{_kde_libdir}/kde4/libkonsolepart.so
%{_kde_libdir}/libkdeinit4_konsole.so
%{_kde_libdir}/libkonsoleprivate.so
%{_kde_appsdir}/konsole
%{_kde_appsdir}/kconf_update/konsole*
%{_kde_applicationsdir}/konsole.desktop
%{_kde_services}/konsolepart.desktop
%{_kde_services}/ServiceMenus/konsolehere.desktop
%{_kde_servicetypes}/terminalemulator.desktop
%{_kde_docdir}/HTML/en/%{name}

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0
- Fix file listed twice RPM error

* Wed Jul 18 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97

* Sun Jul 01 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- Update to 4.8.95
- Fix file list

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762478
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758065
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 744546
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 739304
- New upstream tarball $NEW_VERSION

* Fri Dec 02 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:4.7.80-1
+ Revision: 737251
- add missing 'kdebase4-devel' buildrequires

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New upstream tarball 4.7.80

* Sat Sep 10 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-1
+ Revision: 699190
- imported package konsole

