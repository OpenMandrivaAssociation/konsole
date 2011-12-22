Name: konsole
Summary: A terminal emulator similar to xterm for KDE
Version: 4.7.95
Release: 1
Epoch: 1
Group: Graphical desktop/KDE
License: GPLv2 LGPLv2 GFDL
URL: http://konsole.kde.org/
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: kdebase4-devel >= 1:%{version}
Requires: kdebase4-runtime
Requires: x11-font-misc-misc

Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%{name}-%version.tar.bz2

%description
A terminal emulator, similar to xterm, for KDE.

%files
%doc README COPYING COPYING.DOC COPYING.LIB
%dir %_kde_docdir/%{name}/
%_kde_docdir/%{name}/manual
%_kde_docdir/%{name}/developer
%_kde_docdir/%{name}/user
%_kde_bindir/konsole
%_kde_bindir/konsoleprofile
%_kde_libdir/kde4/libkonsolepart.so
%_kde_libdir/libkdeinit4_konsole.so
%_kde_libdir/libkonsoleprivate.so
%_kde_datadir/applications/kde4/konsole.desktop
%_kde_appsdir/konsole
%_kde_datadir/kde4/services/konsolepart.desktop
%_kde_datadir/kde4/servicetypes/terminalemulator.desktop
%_kde_datadir/kde4/services/ServiceMenus/konsolehere.desktop
%_kde_docdir/HTML/en/%name

#-----------------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
mkdir -p %{buildroot}/%_kde_docdir/%{name}
mv doc/* %{buildroot}/%_kde_docdir/%{name}

