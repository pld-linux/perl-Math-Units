%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Units
Summary:	Math-Units perl module
Summary(pl):	Modu³ perla Math-Units
Name:		perl-Math-Units
Version:	1.2
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-Units perl module.

%description -l pl
Modu³ perla Math-Units.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc *.gz examples/convert.pl
%{perl_sitelib}/Math/Units.pm
%{_mandir}/man3/*
