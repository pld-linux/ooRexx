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
# Source0-md5:	d9801c4c7981328ea063f1a2fd2216a5
URL:		http://www.oorexx.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open Object Rexx is an object-oriented scripting language. The
language is designed for "non-programmer" type users, so it is easy to
learn and easy to use, and provides an excellent vehicle to enter the
world of object-oriented programming without much effort.

It extends the procedural way of programming with object-oriented
features that allow you to gradually change your programming style as
you learn more about objects.

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
