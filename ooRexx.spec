# TODO:
# - cleanup
# - remove unnecessary binaries
# - split development files from package
Summary:	Open Object Rexx
Summary(pl.UTF-8):	Zorientowany objektowo Rexx
Name:		ooRexx
Version:	3.2.0
Release:	0.1
License:	CPL
Group:		Applications
Source0:	http://dl.sourceforge.net/oorexx/%{name}-%{version}.tar.gz
# Source0-md5:	4a3220466acd13028311e3498efb306a
URL:		http://www.oorexx.org/
ExcludeArch:	%{x8664} alpha ia64 ppc64 s390x sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open Object Rexx is an object-oriented scripting language. The
language is designed for "non-programmer" type users, so it is easy to
learn and easy to use, and provides an excellent vehicle to enter the
world of object-oriented programming without much effort.

It extends the procedural way of programming with object-oriented
features that allow you to gradually change your programming style as
you learn more about objects.

%description -l pl.UTF-8
Otwarty Obiektowy Rexx jeseet zorientowanym obiektowo językiem
skryptowym. Język jest przeznaczony dla użytkowników nie bedących
programistami, więc jeset łatwy do nauki i użycia, udostepniając
doskonwałe mechanizmy do bezproblemowego wejścia w programowanie
obiektowe.

Rozszerza programowanie proceduralne o obiektowo zorientowane
możliwości, aby umozliwić stopniową zmianę stylu programowania
podczas nauki obiektów.

%prep
%setup -q

sed -e 's@%{_bindir}/sh@/bin/sh@g' -i platform/unix/rexx.sh samples/unix/trexx
sed -e 's@%{_bindir}/csh@/bin/csh@g' -i platform/unix/rexx.csh

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
%{_libdir}/%{name}
%{_includedir}/rexx.h
