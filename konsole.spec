%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 70 -o "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)
#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	A terminal emulator similar to xterm for KDE
Name:		konsole
Version:	25.08.0
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
Url:		https://konsole.kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/konsole/-/archive/%{gitbranch}/konsole-%{gitbranchd}.tar.bz2#/konsole-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/konsole-%{version}.tar.xz
%endif
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DBUILD_QCH:BOOL=ON
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

%rename plasma6-konsole

%description
A terminal emulator, similar to xterm, for KDE.

%files -f %{name}.lang
%{_datadir}/zsh/site-functions/_konsole
%{_datadir}/qlogging-categories6/konsole.categories
%{_bindir}/*
# Technically this should be a separate libpackage, but given it is
# required by konsole and nothing else can use it, splitting it out
# really doesn't make sense. Let's keep it here.
%{_libdir}/libkonsoleapp.so.*
%{_libdir}/libkonsoleprivate.so.*
%{_qtdir}/plugins/kf6/parts/konsolepart.so
%dir %{_qtdir}/plugins/konsoleplugins
%{_qtdir}/plugins/konsoleplugins/konsole_sshmanagerplugin.so
%{_datadir}/metainfo/org.kde.konsole.appdata.xml
%{_datadir}/applications/org.kde.konsole.desktop
%{_datadir}/knotifications6/konsole.notifyrc
%{_qtdir}/plugins/konsoleplugins/konsole_quickcommandsplugin.so
%{_datadir}/kio/servicemenus/konsolerun.desktop
%{_datadir}/kglobalaccel/org.kde.konsole.desktop
%{_datadir}/polkit-1/actions/org.kde.konsole.policy

#-----------------------------------------------------------------------------

%install -a
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
cat >%{buildroot}%{_datadir}/polkit-1/actions/org.kde.konsole.policy <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-FileCopyrightText: no
     SPDX-License-Identifier: CC0-1.0
-->
<!DOCTYPE policyconfig PUBLIC
"-//freedesktop//DTD PolicyKit Policy Configuration 1.0//EN"
"http://www.freedesktop.org/standards/PolicyKit/1/policyconfig.dtd">
<policyconfig>

 <vendor>Konsole</vendor>
 <vendor_url>https://apps.kde.org/konsole</vendor_url>

 <action id="org.kde.konsole.pkexec.run">
    <description>Konsole terminal</description>
    <message>Authentication is required to run the Konsole terminal in admin mode</message>
    <icon_name>org.kde.konsole</icon_name>
    <defaults>
     <allow_any>no</allow_any>
     <allow_inactive>no</allow_inactive>
     <allow_active>auth_admin</allow_active>
    </defaults>
    <annotate key="org.freedesktop.policykit.exec.path">/usr/bin/konsole</annotate>
    <annotate key="org.freedesktop.policykit.exec.allow_gui">true</annotate>
 </action>
</policyconfig>
EOF
