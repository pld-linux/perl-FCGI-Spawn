#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	FCGI
%define	pnam	Spawn
Summary:	FCGI::Spawn - process manager/application server for FastCGI protocol
Name:		perl-FCGI-Spawn
Version:	0.15
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/FCGI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a8128d47b98d269d1d3b566cadc942bd
URL:		http://search.cpan.org/dist/FCGI-Spawn/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FCGI::Spawn is used to serve as a FastCGI process manager. Besides the
features the FCGI::ProcManager posess itself, the FCGI::Spawn is
targeted as web server admin understandable instance for building the
own fastcgi server with copy-on-write memory sharing among forks and
with single input parameters like processes number and maximum
requests per fork.

%prep
%setup -q -n %{pdir}-%{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/FCGI/*.pm
%{_mandir}/man3/*
