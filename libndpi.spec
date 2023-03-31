%define	oname	ndpi
%define	major	1
%define	libname	%mklibname %{oname} %{major}
%define	devname	%mklibname %{oname} -d
%define real_version 1.8.0

Summary:	Open source deep packet inspection
Name:		libndpi
Version:	1.8
Release:	3
License:	LGPLv3
Group:		System/Libraries
URL:		http://www.ntop.org/products/ndpi/
Source0:	http://downloads.sourceforge.net/project/ntop/nDPI/nDPI-%{version}.tar.gz
Patch0:		libndpi-1.5.0-get-rid-of-third-party-json-c-and-fix-build-against.patch
BuildRequires:	pcap-devel

%description
nDPI is a ntop-maintained superset of the popular OpenDPI library. Released
under the GPL license, its goal is to extend the original library by adding
new protocols that are otherwise available only on the paid version of OpenDPI.
In addition to Unix platforms, we also support Windows, in order to provide
you a cross-platform DPI experience. Furthermore, we have modified nDPI do be
more suitable for traffic monitoring applications, by disabling specific
features that slow down the DPI engine while being them un-necessary for
network traffic monitoring.

nDPI is used by both ntop and nProbe for adding application-layer detection of
protocols, regardless of the port being used. This means that it is possible
to both detect known protocols on non-standard ports (e.g. detect http non
ports other than 80), and also the opposite (e.g. detect Skype traffic on port
80). This is because nowadays the concept of port=application no longer holds.

%package -n	ndpiReader
Summary:	nDPI reading tool
Group:		Networking/Other

%description -n	ndpiReader
Tool for reading DPI..

%package -n	%{libname}
Summary:	Open source deep packet inspection library
Group:		System/Libraries

%description -n	%{libname}
nDPI is a ntop-maintained superset of the popular OpenDPI library. Released
under the GPL license, its goal is to extend the original library by adding
new protocols that are otherwise available only on the paid version of OpenDPI.
In addition to Unix platforms, we also support Windows, in order to provide
you a cross-platform DPI experience. Furthermore, we have modified nDPI do be
more suitable for traffic monitoring applications, by disabling specific
features that slow down the DPI engine while being them un-necessary for
network traffic monitoring.

nDPI is used by both ntop and nProbe for adding application-layer detection of
protocols, regardless of the port being used. This means that it is possible
to both detect known protocols on non-standard ports (e.g. detect http non
ports other than 80), and also the opposite (e.g. detect Skype traffic on port
80). This is because nowadays the concept of port=application no longer holds.

This package provides the shared %{name} library.

%package -n	%{devname}
Summary:	Header files and libraries for developing applications for nDPI
Group:		Development/C
Requires:	%{libname} >= %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	%{oname}-devel = %{EVRD}

%description -n	%{devname}
nDPI is a ntop-maintained superset of the popular OpenDPI library. Released
under the GPL license, its goal is to extend the original library by adding
new protocols that are otherwise available only on the paid version of OpenDPI.
In addition to Unix platforms, we also support Windows, in order to provide
you a cross-platform DPI experience. Furthermore, we have modified nDPI do be
more suitable for traffic monitoring applications, by disabling specific
features that slow down the DPI engine while being them un-necessary for
network traffic monitoring.

nDPI is used by both ntop and nProbe for adding application-layer detection of
protocols, regardless of the port being used. This means that it is possible
to both detect known protocols on non-standard ports (e.g. detect http non
ports other than 80), and also the opposite (e.g. detect Skype traffic on port
80). This is because nowadays the concept of port=application no longer holds.


These are the header files and libraries for developing applications for
%{name}.

%prep
%setup -qn nDPI-%{version}
rm -rf packages/ubuntu/
libtoolize --copy --force
autoreconf -fiv

%build
%configure
%make

%install
%makeinstall_std

%files -n ndpiReader
%{_bindir}/ndpiReader

%files -n %{libname}
%{_libdir}/libndpi.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%dir %{_includedir}/libndpi-%{real_version}/libndpi
%{_includedir}/libndpi-%{real_version}/libndpi/*.h
%{_libdir}/libndpi.so
%{_libdir}/pkgconfig/libndpi.pc
