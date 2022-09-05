Summary:	GeoIP Update - automatically update GeoIP2 or GeoIP Legacy binary databases
Summary(pl.UTF-8):	GeoIP Update - automatyczna aktualizacja binarnych baz danych GeoIP2 lub GeoIP Legacy
Name:		geoipupdate
Version:	4.9.0
Release:	1
License:	Apache v2.0
Group:		Applications/Networking
#Source0Download: https://github.com/maxmind/geoipupdate/releases
Source0:	https://github.com/maxmind/geoipupdate/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	edd364519222e99b1009aec7d7edfb40
%if 0
go mod vendor
tar -caf ~/geoipupdate-vendor.tar.xz vendor
%endif
Source1:	%{name}-vendor-%{version}.tar.xz
# Source1-md5:	c232481778faf5d48bb9e6994d54ad82
Patch0:		go-vendor.patch
URL:		https://github.com/maxmind/geoipupdate
BuildRequires:	curl-devel
BuildRequires:	golang >= 1.3.1
BuildRequires:	pandoc
BuildRequires:	rpmbuild(macros) >= 2.009
BuildRequires:	zlib-devel
Provides:	GeoIP-update = %{version}-%{release}
Obsoletes:	GeoIP-update <= 2.2.2-2
Conflicts:	GeoIP < 1.6.0
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages 0

%description
The GeoIP Update program performs automatic updates of GeoIP2 and
GeoIP Legacy binary databases. Currently the program only supports
Linux and other Unix-like systems.

%description -l pl.UTF-8
Program GeoIP Update wykonuje automatyczne aktualizacje binarnych baz
danych GeoIP2 lub GeoIP Legacy. Obecnie program działa tylko na
Linuksie i innych systemach uniksowych.

%prep
%setup -q -a1
%patch0 -p1

%build
%{__make} \
	DATADIR=/usr/share/GeoIP \
	CONFFILE=%{_sysconfdir}/GeoIP.conf \
	VERSION="%{version} (PLD Linux)"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man{1,5}}
install -p build/%{name} $RPM_BUILD_ROOT%{_bindir}
cp -p build/GeoIP.conf $RPM_BUILD_ROOT%{_sysconfdir}/GeoIP.conf
cp -p build/geoipupdate.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p build/GeoIP.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md
%attr(755,root,root) %{_bindir}/geoipupdate
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/GeoIP.conf
%{_mandir}/man1/geoipupdate.1*
%{_mandir}/man5/GeoIP.conf.5*
