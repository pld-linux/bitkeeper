Summary:	A distributed concurent versioning system better than CVS
Summary(pl.UTF-8):	System kontroli wersji lepszy niż CVS
Name:		bitkeeper
Version:	3.2.0
Release:	1
License:	BitKeeper
Group:		Development/Version Control
Source0:	http://bitkeeper:get%20bitkeeper@www.bitmover.com/download/bk-3.2.0/bk-%{version}-x86-glibc23-linux.bin
# Source0-md5:	21a14b3ea291ef70d59d350ccde4f19a
Source1:	http://bitkeeper:get%20bitkeeper@www.bitmover.com/download/bk-3.2.0/bk-%{version}-alpha-glibc22-linux.bin
# Source1-md5:	e1cb11215b03fd30e7e4b5fb5763d3e2
Source2:	http://bitkeeper:get%20bitkeeper@www.bitmover.com/download/bk-3.2.0/bk-%{version}-powerpc-glibc21-linux.bin
# Source2-md5:	7ad959ee34f35516bd607bdd1192171c
Source3:	http://bitkeeper:get%20bitkeeper@www.bitmover.com/download/bk-3.2.0/bk-%{version}-sparc-glibc21-linux.bin
# Source3-md5:	bd432ed8612d5d7d884c3418615d658f
URL:		http://www.bitkeeper.com/
Requires:	tk >= 8.0
BuildRequires:	fileutils
BuildRequires:	perl-base
ExclusiveArch:	%{ix86} alpha ppc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A distributed concurrent versioning system better than CVS.

%description -l pl.UTF-8
System kontroli wersji lepszy niż CVS.

%prep
%setup -q -c -T
umask 022
SRC=
%ifarch %{ix86}
SRC=%{SOURCE0}
%endif
%ifarch alpha
SRC=%{SOURCE1}
%endif
%ifarch ppc
SRC=%{SOURCE2}
%endif
%ifarch sparc64
SRC=%{SOURCE3}
%endif

chmod 755 ${SRC}
${SRC} bitkeeper
chmod -R u+rwX,a+rX .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir}/%{name},%{_bindir},%{_mandir}/man1}

cp -ap bitkeeper/* $RPM_BUILD_ROOT%{_libdir}/%{name}

for man in $RPM_BUILD_ROOT%{_libdir}/%{name}/man/man1/*; do
	tman=$(basename "$man")
	if ! (echo "$tman" | grep -Eq "^bk-"); then
		tman="bk-$tman"
	fi
	mv $man $RPM_BUILD_ROOT%{_mandir}/man1/${tman}
done

rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/man/

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
%{_mandir}/man*/*
%attr(-,root,root) %{_libdir}/%{name}
