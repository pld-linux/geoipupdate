Summary:	GeoIP Update - automatically update GeoIP2 or GeoIP Legacy binary databases
Summary(pl.UTF-8):	GeoIP Update - automatyczna aktualizacja binarnych baz danych GeoIP2 lub GeoIP Legacy
Name:		GeoIP-update
Version:	2.2.2
Release:	1
License:	GPL v2
Group:		Libraries
#Source0Download: https://github.com/maxmind/geoipupdate/releases
Source0:	https://github.com/maxmind/geoipupdate/releases/download/v%{version}/geoipupdate-%{version}.tar.gz
# Source0-md5:	06284bd7bcb298d078d794eb630dae55
URL:		https://github.com/maxmind/geoipupdate
BuildRequires:	curl-devel
BuildRequires:	zlib-devel
Conflicts:	GeoIP < 1.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GeoIP Update program performs automatic updates of GeoIP2 and
GeoIP Legacy binary databases. Currently the program only supports
Linux and other Unix-like systems.

%description -l pl.UTF-8
Program GeoIP Update wykonuje automatyczne aktualizacje binarnych baz
danych GeoIP2 lub GeoIP Legacy. Obecnie program działa tylko na
Linuksie i innych systemach uniksowych.

%prep
%setup -q -n geoipupdate-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/GeoIP.conf.default

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.md README.md
%attr(755,root,root) %{_bindir}/geoipupdate
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/GeoIP.conf
%{_mandir}/man1/geoipupdate.1*
%{_mandir}/man5/GeoIP.conf.5*
