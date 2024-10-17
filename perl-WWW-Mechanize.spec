%define modname	WWW-Mechanize

Summary:	Handy web browsing in a Perl object
Name:		perl-%{modname}
Version:	2.19
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/WWW/WWW-Mechanize-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl(HTML::Form)
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(IO::Socket::SSL)
BuildRequires:	perl(URI)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Memory::Cycle)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::LongString)
BuildRequires:	perl(HTTP::Daemon)
BuildRequires:	perl(HTTP::Response::Encoding)
BuildRequires:	perl(HTTP::Server::Simple::CGI)

%description
WWW::Mechanize, or Mech for short, helps you automate interaction with a
website. It supports performing a sequence of page fetches including following
links and submitting forms. Each fetched page is parsed and its links and forms
are extracted. A link or a form can be selected, form fields can be filled and
the next page can be fetched. Mech also stores a history of the URLs you've
visited, which can be queried and revisited.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor <<EOF
EOF

%build
%make_build

%install
%make_install

# Some tests will fail because of firewalls and friends
# Also we don't currently have all dependencies used there
#check
#%make_build test

%files 
%doc Changes etc/www-mechanize-logo.png
%{_bindir}/*
%{perl_vendorlib}/WWW
%{_mandir}/man1/*
%{_mandir}/man3/*
