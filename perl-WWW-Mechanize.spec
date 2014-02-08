%define upstream_name  WWW-Mechanize
%define upstream_version 1.72

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Handy web browsing in a Perl object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl(HTML::Form)
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(IO::Socket::SSL)
BuildRequires:	perl(URI)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Memory::Cycle)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::LongString)
BuildRequires:	perl(HTTP::Daemon)
BuildRequires:	perl(HTTP::Response::Encoding)
BuildRequires:	perl(HTTP::Server::Simple::CGI)
BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%install
%makeinstall_std

%check
make test

%files 
%doc Changes etc/www-mechanize-logo.png
%{perl_vendorlib}/WWW
%{_mandir}/*/*
%{_bindir}/*


%changelog
* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.680.0-1mdv2011.0
+ Revision: 660023
- update to new version 1.68

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.660.0-2mdv2011.0
+ Revision: 597105
- rebuild

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.660.0-1mdv2011.0
+ Revision: 596701
- update to 1.66

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.640.0-1mdv2011.0
+ Revision: 552694
- update to 1.64

* Tue Apr 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.620.0-1mdv2010.1
+ Revision: 534591
- new version

  + Jérôme Quelin <jquelin@mandriva.org>
    - update to 1.60

* Wed Aug 19 2009 Jérôme Quelin <jquelin@mandriva.org> 1.600.0-1mdv2010.0
+ Revision: 418113
- update to 1.60

* Wed Jul 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.580.0-1mdv2010.0
+ Revision: 396356
- update to 0.58

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.560.0-1mdv2010.0
+ Revision: 394968
- update to 1.56
- using %%perl_convert_version
- fixed license field

* Tue Jan 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.54-1mdv2009.1
+ Revision: 328903
- update to new version 1.54

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.52-1mdv2009.1
+ Revision: 309454
- update to new version 1.52

* Tue Oct 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.50-1mdv2009.1
+ Revision: 297977
- new version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.34-4mdv2009.0
+ Revision: 258790
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.34-3mdv2009.0
+ Revision: 246710
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 11 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.34-1mdv2008.1
+ Revision: 117549
- update to new version 1.34

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 1.32-2mdv2008.1
+ Revision: 109344
- rebuild

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.32-1mdv2008.1
+ Revision: 104441
- update to new version 1.32

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-1mdv2008.0
+ Revision: 47740
- update to new version 1.30


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdv2007.1
+ Revision: 133690
- new version

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2007.0
- New version 1.20

* Mon Oct 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.16-1mdk
- 1.16

* Wed Sep 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-1mdk
- New release 1.14
- buildrequires

* Wed Jun 08 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-2mdk 
- better url
- spec cleanup
- make test in %%check
- don't ship useless empty directories

* Fri Feb 25 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.12-1mdk
- 1.12

* Wed Feb 09 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.10-1mdk
- 1.10
- Reenable make test and BuildRequires

* Sun Jan 23 2005 Stefan van der Eijk <stefan@mandrake.org> 1.08-1mdk
- 1.08
- disable make test, as it seems to be broken on 1.06 & 1.08
- commented out the BuildRequires for the test

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.06-2mdk
- fix buildrequires in a backward compatible way

* Mon Dec 13 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.06-1mdk
- new version
- add logo in doc

* Thu Nov 04 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.04-1mdk 
- new version
- rpmbuildupdate aware

* Thu Apr 22 2004 Olivier Blin <blino@mandrake.org> 1.02-2mdk
- quiet setup
- fix Summary

* Thu Apr 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.02-1mdk
- new version

* Tue Mar 30 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.74-1mdk
- first mdk release

