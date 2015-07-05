%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	A terminal emulator similar to xterm for KDE
Name:		konsole
Version:	15.04.3
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
Url:		http://konsole.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
# if you don't know how to check ARM build
# don't remove this patch
Patch0:		konsole-4.14.3-qFuzzyCompare-arm.patch
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Pty)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(ECM)

%description
A terminal emulator, similar to xterm, for KDE.

%files
%{_bindir}/*
%{_libdir}/libkdeinit5_konsole.so
# Technically this should be a separate libpackage, but given it is
# required by konsole and nothing else can use it, splitting it out
# really doesn't make sense. Let's keep it here.
%{_libdir}/libkonsoleprivate.so.*
%{_libdir}/qt5/plugins/konsolepart.so
%{_datadir}/konsole
%{_datadir}/appdata/org.kde.konsole.appdata.xml
%{_datadir}/applications/org.kde.konsole.desktop
%{_datadir}/knotifications5/konsole.notifyrc
%{_datadir}/kservices5/konsolepart.desktop
%{_datadir}/kservices5/ServiceMenus/konsolehere.desktop
%{_datadir}/kservices5/ServiceMenus/konsolerun.desktop
%{_datadir}/kservicetypes5/terminalemulator.desktop
%{_datadir}/kxmlgui5/konsole
%doc %{_docdir}/HTML/en/konsole

#-----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
