%define name xmms-lirc
%define version 1.4
%define release %mkrel 3

Summary: This is a LIRC plugin for xmms (Infrared Controler)
Name:    %{name}
Version: %{version}
Release: %{release}
Source0: lirc-xmms-plugin-%{version}.tar.bz2
License: GPL
Group:   Sound
URL:	http://www.lirc.org/software.html
Buildrequires: gtk+1.2-devel, xmms-devel, binutils, lirc-devel, mawk, gcc

%description
This is a LIRC plugin for xmms (Infrared Controler)

%prep
%setup -q -n lirc-xmms-plugin-%{version}
%configure

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_libdir}/xmms/General/*

