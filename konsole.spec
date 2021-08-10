%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	A terminal emulator similar to xterm for KDE
Name:		konsole
Version:	21.08.0
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
Url:		http://konsole.kde.org/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
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
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Pty)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(ECM)

# This is not quite true... But something has to kill off the
# kde-l10n packages from before kapps-17.04.0 (when messages
# started being bundled with packages), and konsole is probably
# just about the most likely package to be installed...
Obsoletes:	kde-l10n-ar < 3:17.0.0-1
Obsoletes:	kde-l10n-ast < 3:17.0.0-1
Obsoletes:	kde-l10n-bg < 3:17.0.0-1
Obsoletes:	kde-l10n-bs < 3:17.0.0-1
Obsoletes:	kde-l10n-ca < 3:17.0.0-1
Obsoletes:	kde-l10n-cs < 3:17.0.0-1
Obsoletes:	kde-l10n-da < 3:17.0.0-1
Obsoletes:	kde-l10n-de < 3:17.0.0-1
Obsoletes:	kde-l10n-el < 3:17.0.0-1
Obsoletes:	kde-l10n-en_GB < 3:17.0.0-1
Obsoletes:	kde-l10n-eo < 3:17.0.0-1
Obsoletes:	kde-l10n-es < 3:17.0.0-1
Obsoletes:	kde-l10n-et < 3:17.0.0-1
Obsoletes:	kde-l10n-eu < 3:17.0.0-1
Obsoletes:	kde-l10n-fa < 3:17.0.0-1
Obsoletes:	kde-l10n-fi < 3:17.0.0-1
Obsoletes:	kde-l10n-fr < 3:17.0.0-1
Obsoletes:	kde-l10n-ga < 3:17.0.0-1
Obsoletes:	kde-l10n-gl < 3:17.0.0-1
Obsoletes:	kde-l10n-he < 3:17.0.0-1
Obsoletes:	kde-l10n-hi < 3:17.0.0-1
Obsoletes:	kde-l10n-hr < 3:17.0.0-1
Obsoletes:	kde-l10n-hu < 3:17.0.0-1
Obsoletes:	kde-l10n-ia < 3:17.0.0-1
Obsoletes:	kde-l10n-id < 3:17.0.0-1
Obsoletes:	kde-l10n-is < 3:17.0.0-1
Obsoletes:	kde-l10n-it < 3:17.0.0-1
Obsoletes:	kde-l10n-ja < 3:17.0.0-1
Obsoletes:	kde-l10n-kk < 3:17.0.0-1
Obsoletes:	kde-l10n-km < 3:17.0.0-1
Obsoletes:	kde-l10n-ko < 3:17.0.0-1
Obsoletes:	kde-l10n-lt < 3:17.0.0-1
Obsoletes:	kde-l10n-lv < 3:17.0.0-1
Obsoletes:	kde-l10n-mr < 3:17.0.0-1
Obsoletes:	kde-l10n-nb < 3:17.0.0-1
Obsoletes:	kde-l10n-nds < 3:17.0.0-1
Obsoletes:	kde-l10n-nl < 3:17.0.0-1
Obsoletes:	kde-l10n-nn < 3:17.0.0-1
Obsoletes:	kde-l10n-pa < 3:17.0.0-1
Obsoletes:	kde-l10n-pl < 3:17.0.0-1
Obsoletes:	kde-l10n-pt < 3:17.0.0-1
Obsoletes:	kde-l10n-pt_BR < 3:17.0.0-1
Obsoletes:	kde-l10n-ro < 3:17.0.0-1
Obsoletes:	kde-l10n-ru < 3:17.0.0-1
Obsoletes:	kde-l10n-sk < 3:17.0.0-1
Obsoletes:	kde-l10n-sl < 3:17.0.0-1
Obsoletes:	kde-l10n-sr < 3:17.0.0-1
Obsoletes:	kde-l10n-sv < 3:17.0.0-1
Obsoletes:	kde-l10n-tr < 3:17.0.0-1
Obsoletes:	kde-l10n-ug < 3:17.0.0-1
Obsoletes:	kde-l10n-uk < 3:17.0.0-1
Obsoletes:	kde-l10n-wa < 3:17.0.0-1
Obsoletes:	kde-l10n-zh_CN < 3:17.0.0-1
Obsoletes:	kde-l10n-zh_TW < 3:17.0.0-1
Obsoletes:	kde-l10n-af < 3:17.0.0-1
Obsoletes:	kde-l10n-az < 3:17.0.0-1
Obsoletes:	kde-l10n-be < 3:17.0.0-1
Obsoletes:	kde-l10n-bn_IN < 3:17.0.0-1
Obsoletes:	kde-l10n-bo < 3:17.0.0-1
Obsoletes:	kde-l10n-br < 3:17.0.0-1
Obsoletes:	kde-l10n-csb < 3:17.0.0-1
Obsoletes:	kde-l10n-cy < 3:17.0.0-1
Obsoletes:	kde-l10n-fo < 3:17.0.0-1
Obsoletes:	kde-l10n-fy < 3:17.0.0-1
Obsoletes:	kde-l10n-hne < 3:17.0.0-1
Obsoletes:	kde-l10n-kn < 3:17.0.0-1
Obsoletes:	kde-l10n-ku < 3:17.0.0-1
Obsoletes:	kde-l10n-gu < 3:17.0.0-1
Obsoletes:	kde-l10n-lo < 3:17.0.0-1
Obsoletes:	kde-l10n-mai < 3:17.0.0-1
Obsoletes:	kde-l10n-mi < 3:17.0.0-1
Obsoletes:	kde-l10n-mk < 3:17.0.0-1
Obsoletes:	kde-l10n-ml < 3:17.0.0-1
Obsoletes:	kde-l10n-mt < 3:17.0.0-1
Obsoletes:	kde-l10n-ne < 3:17.0.0-1
Obsoletes:	kde-l10n-oc < 3:17.0.0-1
Obsoletes:	kde-l10n-se < 3:17.0.0-1
Obsoletes:	kde-l10n-si < 3:17.0.0-1
Obsoletes:	kde-l10n-ta < 3:17.0.0-1
Obsoletes:	kde-l10n-tg < 3:17.0.0-1
Obsoletes:	kde-l10n-th < 3:17.0.0-1
Obsoletes:	kde-l10n-ven < 3:17.0.0-1
Obsoletes:	kde-l10n-vi < 3:17.0.0-1
Obsoletes:	kde-l10n-xh < 3:17.0.0-1
Obsoletes:	kde-l10n-en_US < 3:17.0.0-1
Obsoletes:	kde-l10n-ca-valencia < 3:17.0.0-1

%description
A terminal emulator, similar to xterm, for KDE.

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/konsole.categories
%{_datadir}/knsrcfiles/konsole.knsrc
%{_bindir}/*
# Technically this should be a separate libpackage, but given it is
# required by konsole and nothing else can use it, splitting it out
# really doesn't make sense. Let's keep it here.
%{_libdir}/libkonsoleapp.so.*
%{_libdir}/libkonsoleprivate.so.*
%{_libdir}/qt5/plugins/konsolepart.so
%{_datadir}/khotkeys/konsole.khotkeys
%{_datadir}/konsole
%{_datadir}/metainfo/org.kde.konsole.appdata.xml
%{_datadir}/applications/org.kde.konsole.desktop
%{_datadir}/knotifications5/konsole.notifyrc
%{_datadir}/kservices5/konsolepart.desktop
%{_datadir}/kservices5/ServiceMenus/konsolerun.desktop
%{_datadir}/kservicetypes5/terminalemulator.desktop

#-----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
