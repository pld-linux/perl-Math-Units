%include	/usr/lib/rpm/macros.perl
Summary:	Math-Units perl module
Summary(pl):	Modu� perla Math-Units
Name:		perl-Math-Units
Version:	1.2
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/Math-Units-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-Units perl module.

%description -l pl
Modu� perla Math-Units.

%prep
%setup -q -n Math-Units-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO}.gz examples/convert.pl

%{perl_sitelib}/Math/Units.pm
%{perl_sitearch}/auto/Math/Units

%{_mandir}/man3/*
