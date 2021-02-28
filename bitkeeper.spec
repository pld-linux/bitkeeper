Summary:	A distributed concurent versioning system better than CVS
Summary(pl.UTF-8):	System kontroli wersji lepszy niż CVS
Name:		bitkeeper
Version:	7.3.3
Release:	0.1
License:	Apache v2.0
Group:		Development/Version Control
Source0:	https://www.bitkeeper.org/downloads/%{version}/bk-%{version}.src.tar.gz
# Source0-md5:	8253674ac4e6756706b3d9a7fe80ef4d
URL:		https://www.bitkeeper.org/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gperf
BuildRequires:	libtomcrypt-devel
BuildRequires:	libtommath-devel
BuildRequires:	lz4-devel
BuildRequires:	pcre-devel
BuildRequires:	tk-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A distributed concurrent versioning system better than CVS.

%description -l pl.UTF-8
System kontroli wersji lepszy niż CVS.

%prep
%setup -q -n bk-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALLED_BK=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc */*.pdf doc/quickstart README.md RELEASE-NOTES*
#%attr(755,root,root) %{_bindir}/*
#%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
#%{_mandir}/man*/*
