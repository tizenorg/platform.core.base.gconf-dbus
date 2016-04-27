#sbs-git:slp/pkgs/g/gconf-dbus gconf-dbus 2.16.0 00a1761211cf288653a387587d6abc2bfc4d5626
Name:           gconf-dbus
Version: 2.16.0
Release:        2
License:        LGPL-2.0+
Summary:        A process-transparent configuration system
Url:            http://www.gnome.org
Group:          System/Base
Source:         ftp://ftp.gnome.org/pub/GNOME/mobile/2.23/2.23.92/sources/%{name}-%{version}.tar.gz
Source1001: 	gconf-dbus.manifest
Patch0:		01_removePopt.patch
Patch1:		02_poweroff.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(dbus-1),
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.60
BuildRequires:  pkgconfig(glib-2.0) > 2.8.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires: intltool
Requires:       %{name} = %{version}-%{release}
Requires:       dbus

%description
GConf-dbus is a process-transparent configuration database API used to
store user preferences. It has pluggable backends and features to
support workgroup administration.

%package devel
Summary:        Headers and libraries for GConf development
Group:          Development/Libraries
Requires:       %{name} = %{version}
# we install an automake macro
Requires:       automake
Requires:       pkgconfig(dbus-1),
Requires:       pkgconfig(dbus-glib-1)
Requires:       pkgconfig(glib-2.0) > 2.8.0
Requires:       pkgconfig(libxml-2.0)

%description devel
GConf-dbus development package. Contains files needed for doing
development using GConf.

%package utils
Summary:        gconf-dbus system tools
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires:       dbus

%description utils
GConf-dbus development package. Contains files needed for doing
development using GConf.


%prep
%setup -q
cp %{SOURCE1001} .
%patch0 -p1
%patch1 -p1

%build
%configure --disable-static --disable-gtk-doc --disable-defaults-service --disable-gtk --disable-nls --enable-system-bus 
make

%install
rm -fr %{buildroot}
%make_install

%find_lang GConf2

%clean
rm -rf %{buildroot}

%post -p  /sbin/ldconfig

%postun -p /sbin/ldconfig


%files utils 
%manifest %{name}.manifest
%{_bindir}/gconf-merge-tree
%{_bindir}/gconftool-2
%manifest gconf-dbus.manifest
%license COPYING

%files  -f GConf2.lang
%manifest %{name}.manifest
%doc COPYING
%doc %{_datadir}/sgml/gconf/*
%config(noreplace) %{_sysconfdir}/gconf/2/path
%dir %{_sysconfdir}/gconf
%dir %{_sysconfdir}/gconf/2
%dir %{_sysconfdir}/gconf/gconf.xml.defaults
%dir %{_sysconfdir}/gconf/gconf.xml.mandatory
%{_libexecdir}/*
%{_libdir}/*.so.*
%dir %{_libdir}/GConf-dbus
%dir %{_libdir}/GConf-dbus/2
%{_libdir}/GConf-dbus/2/*.so
%{_datadir}/dbus-1/services/gconf.service
%{_sysconfdir}/dbus-1/system.d/gconfd.conf
%manifest gconf-dbus.manifest
%license COPYING

%files devel
%manifest %{name}.manifest
%doc %{_datadir}/gtk-doc/html/gconf/*
%doc %{_mandir}/man1/*
%{_libdir}/*.so
%{_includedir}/gconf
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/*
%license COPYING
