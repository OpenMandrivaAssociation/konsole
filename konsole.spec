Name:		konsole
Summary:	A terminal emulator similar to xterm for KDE
Version:	4.8.97
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
URL:		http://konsole.kde.org/
Source:		ftp://ftp.kde.org/pub/kde/unstable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-devel
Requires:	kdebase4-runtime
Requires:	x11-font-misc-misc

%description
A terminal emulator, similar to xterm, for KDE.

%files
%doc README COPYING COPYING.DOC COPYING.LIB
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
%{_kde_docdir}/%{name}

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
mkdir -p %{buildroot}/%{_kde_docdir}/%{name}
mv doc/* %{buildroot}/%{_kde_docdir}/%{name}

