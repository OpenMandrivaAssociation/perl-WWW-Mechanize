%define module	WWW-Mechanize
%define name	perl-%{module}
%define version 1.22
%define release %mkrel 1

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Handy web browsing in a Perl object
License:	    GPL or Artistic
Group:		    Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/WWW/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(CGI)
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(IO::Socket::SSL)
Buildrequires:	perl(URI)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::Exception)
Buildrequires:	perl(Test::Memory::Cycle)
Buildrequires:	perl(Test::Pod)
Buildrequires:	perl(Test::Warn)
Buildrequires:	perl(Test::LongString)
Buildarch:	    noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
WWW::Mechanize, or Mech for short, helps you automate interaction with a
website. It supports performing a sequence of page fetches including following
links and submitting forms. Each fetched page is parsed and its links and forms
are extracted. A link or a form can be selected, form fields can be filled and
the next page can be fetched. Mech also stores a history of the URLs you've
visited, which can be queried and revisited.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes etc/www-mechanize-logo.png
%{perl_vendorlib}/WWW
%{_mandir}/*/*
%{_bindir}/*


