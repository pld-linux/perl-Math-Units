%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Units
Summary:	Math::Units Perl module - unit conversion
Summary(pl):	Modu³ Perla Math::Units - przelicznie jednostek
Name:		perl-Math-Units
Version:	1.2
Release:	12
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5089d07f2042c567759d1c761c40dd98
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Math::Units module converts a numeric value in one unit of
measurement to some other unit. The units must be compatible, i.e.
length can not be converted to volume. If a conversion can not be made
an exception is thrown.

%description -l pl
Modu³ Math::Units przelicza warto¶ci numeryczne z jednej jednostki
miary na inn±. Jednostki musz± byæ zgodne, tzn. d³ugo¶æ nie mo¿e byæ
przeliczona na objêto¶æ. Je¶li konwersja nie mo¿e zostaæ wykonana,
rzucany jest wyj±tek.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO examples/convert.pl
%{perl_vendorlib}/Math/Units.pm
%{_mandir}/man3/*
