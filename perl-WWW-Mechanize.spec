%define upstream_name	 WWW-Mechanize
%define upstream_version 1.68

Name:		    perl-%{upstream_name}
Version:	    %perl_convert_version %{upstream_version}
Release:	    %mkrel 1

Summary:	    Handy web browsing in a Perl object
License:	    GPL+ or Artistic
Group:		    Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

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
Buildrequires:	perl(HTTP::Response::Encoding)
Buildrequires:	perl(HTTP::Server::Simple::CGI)
Buildarch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
WWW::Mechanize, or Mech for short, helps you automate interaction with a
website. It supports performing a sequence of page fetches including following
links and submitting forms. Each fetched page is parsed and its links and forms
are extracted. A link or a form can be selected, form fields can be filled and
the next page can be fetched. Mech also stores a history of the URLs you've
visited, which can be queried and revisited.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


