%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 70 -o "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)
#define git 20231023

Summary:	A terminal emulator similar to xterm for KDE
Name:		plasma6-konsole
Version:	24.01.75
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
Url:		http://konsole.kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/konsole/-/archive/master/konsole-master.tar.bz2#/konsole-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/konsole-%{version}.tar.xz
%endif
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Pty)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	cmake(ECM)
BuildRequires:	%mklibname -d KF6IconWidgets
# Just to make sure we don't pull in the conflicting Plasma5 package
BuildRequires:	plasma6-xdg-desktop-portal-kde

%description
A terminal emulator, similar to xterm, for KDE.

%files -f %{name}.lang
%{_libdir}/kconf_update_bin/konsole_show_menubar
%{_datadir}/kconf_update/konsole.upd
%{_datadir}/kconf_update/konsole_add_hamburgermenu_to_toolbar.sh
%{_datadir}/zsh/site-functions/_konsole
%{_datadir}/qlogging-categories6/konsole.categories
%{_datadir}/knsrcfiles/konsole.knsrc
%{_bindir}/*
# Technically this should be a separate libpackage, but given it is
# required by konsole and nothing else can use it, splitting it out
# really doesn't make sense. Let's keep it here.
%{_libdir}/libkonsoleapp.so.*
%{_libdir}/libkonsoleprivate.so.*
%{_qtdir}/plugins/kf6/parts/konsolepart.so
%dir %{_qtdir}/plugins/konsoleplugins
%{_qtdir}/plugins/konsoleplugins/konsole_sshmanagerplugin.so
%{_datadir}/konsole
%{_datadir}/metainfo/org.kde.konsole.appdata.xml
%{_datadir}/applications/org.kde.konsole.desktop
%{_datadir}/knotifications6/konsole.notifyrc
%{_libdir}/kconf_update_bin/konsole_globalaccel
%{_qtdir}/plugins/konsoleplugins/konsole_quickcommandsplugin.so
%{_datadir}/kio/servicemenus/konsolerun.desktop
%{_datadir}/kglobalaccel/org.kde.konsole.desktop

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n konsole-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

# We get this from distro-release
rm %{buildroot}%{_sysconfdir}/xdg/konsolerc
