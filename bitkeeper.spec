Summary:	A distributed concurent versioning system better than CVS
Summary(pl):	System kontroli wersji lepszy ni¿ CVS
Name:		bitkeeper
Version:	2.1.6pre5
Release:	1
License:	BitKeeper
Group:		Development/Version Control
Source0:	http://www.bitmover.com/download/bk-2.1.x/x86-glibc22-linux.bin
Source1:	http://www.bitmover.com/download/bk-2.1.x/alphaev56-glibc21-linux.bin
Source2:	http://www.bitmover.com/download/bk-2.1.x/powerpc-glibc21-linux.bin
Source3:	http://www.bitmover.com/download/bk-2.1.x/sparc64-glibc21-linux.bin
URL:		http://www.bitkeeper.com/
Requires:	tk >= 8.0
BuildRequires:	fileutils
ExclusiveArch:	%{ix86} alpha ppc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A distributed concurrent versioning system better than CVS.

%description -l pl
System kontroli wersji lepszy ni¿ CVS.

%prep
%setup -q -c -T
umask 022
%ifarch %{ix86}
dd if=%{SOURCE0} skip=1 bs=7008 | gzip -d | tar xf -
%endif
%ifarch alpha
dd if=%{SOURCE1} skip=1 bs=7354 | gzip -d | tar xf -
%endif
%ifarch ppc
dd if=%{SOURCE2} skip=1 bs=6864 | gzip -d | tar xf -
%endif
%ifarch sparc64
dd if=%{SOURCE3} skip=1 bs=6704 | gzip -d | tar xf -
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir}/%{name},%{_bindir}}

cp -ap bitkeeper/* $RPM_BUILD_ROOT%{_libdir}/%{name}

ln -s %{_libdir}/%{name}/bitkeeper.config $RPM_BUILD_ROOT%{_sysconfdir}

for file in admin bk delta get prs rmdel unget; do
	ln -s %{_libdir}/%{name}/${file} $RPM_BUILD_ROOT%{_bindir}/${file}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc bitkeeper/*.pdf
%attr(755,root,root) %{_bindir}/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(-,root,root) %{_libdir}/%{name}
