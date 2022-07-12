%define libname libdspy-1
%define sover 1
%define oname d-spy

Name:           dspy
Version:        1.2.1
Release:        1
Summary:        A D-Bus explorer for GNOME
License:        GPL-3.0
URL:            https://gitlab.gnome.org/GNOME/d-spy
Source:         https://download.gnome.org/sources/dspy/1.2/dspy-%{version}.tar.xz

# appstream-glib BR disabled until upstream fixes the metadata test
# BuildRequires: appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  libxml2-utils
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.68
BuildRequires:  pkgconfig(gtk4) >= 4.6
BuildRequires:  pkgconfig(libadwaita-1) >= 1.0

%description
D-Spy is a simple tool to explore D-Bus connections.

%package        -n %{libname}-%{sover}
Summary:        Shared library for %{name}

%description    -n %{libname}-%{sover}
Shared library for %{name}.

%package        devel
Summary:        Development/header files for %{name}
Requires:       %{name} = %{version}
Requires:       %{libname}-%{sover} = %{version}

%description    devel
Development/header files for %{name}.

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%files
%license COPYING COPYING.lgpl3
%doc NEWS
%{_bindir}/%{oname}
%{_datadir}/appdata/org.gnome.dspy.appdata.xml
%{_datadir}/applications/org.gnome.dspy.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.dspy.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.dspy.devel.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.dspy.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.dspy-symbolic.svg

%files -n %{libname}-%{sover}
%{_libdir}/%{libname}.so.*

%files devel
%{_includedir}/dspy-%{sover}
%{_libdir}/%{libname}.so
