Summary:	OpenFabrics Alliance InfiniBand MAD library
Summary(pl.UTF-8):	Biblioteka OpenFabrics Alliance InfiniBand MAD
Name:		libibmad
Version:	1.3.12
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	https://www.openfabrics.org/downloads/management/%{name}-%{version}.tar.gz
# Source0-md5:	7aabf50569c4d30a9a0689fd96097e4f
URL:		https://www.openfabrics.org/
BuildRequires:	libibumad-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libibmad provides low layer InfiniBand functions for use by the IB
diagnostic and management programs. These include MAD, SA, SMP, and
other basic IB functions.

%description -l pl.UTF-8
libibmad to biblioteka udostępniająca niskopoziomowe funkcje
InfiniBand przeznaczone dla programów diagnostycznych i zarządzających
IB. Obejmuje MAD, SA, SMP i inne podstawowe funkcje IB.

%package devel
Summary:	Header files for libibmad library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libibmad
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libibumad-devel

%description devel
Header files for libibmad library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libibmad.

%package static
Summary:	Static libibmad library
Summary(pl.UTF-8):	Statyczna biblioteka libibmad
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static libibmad library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę libibmad.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libibmad.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibmad.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibmad.so
%{_libdir}/libibmad.la
%{_includedir}/infiniband/mad.h
%{_includedir}/infiniband/mad_osd.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libibmad.a
