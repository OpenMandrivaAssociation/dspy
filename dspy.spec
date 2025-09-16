%define libname libdspy-1
%define sover 1
%define oname d-spy

Name:           dspy
Version:        49.1
Release:        1
Summary:        A D-Bus explorer for GNOME
License:        GPL-3.0
URL:            https://gitlab.gnome.org/GNOME/d-spy
Source0:	https://gitlab.gnome.org/GNOME/d-spy/-/archive/%{version}/d-spy-%{version}.tar.bz2
#Source:         https://download.gnome.org/sources/d-spy/1.2/dspy-%{version}.tar.xz

BuildRequires:	appstream
BuildRequires:	gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libxml2-utils
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.68
BuildRequires:  pkgconfig(gtk4) >= 4.6
BuildRequires:  pkgconfig(libadwaita-1) >= 1.0
BuildRequires:	pkgconfig(libdex-1)

Obsoletes: %{libname}-%{sover}
Obsoletes: dspy-devel

%description
D-Spy is a simple tool to explore D-Bus connections.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%find_lang d-spy

%files -f d-spy.lang
%license COPYING COPYING.lgpl3
%doc NEWS
%{_bindir}/%{oname}
%{_datadir}/metainfo/org.gnome.dspy.metainfo.xml
%{_datadir}/applications/org.gnome.dspy.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.dspy.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.dspy.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.dspy-symbolic.svg
%{_datadir}/dbus-1/services/org.gnome.dspy.service
