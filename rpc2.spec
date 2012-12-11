%define	major	4
%define	libname	    %mklibname %{name}_ %{major}
%define	develname	%mklibname %{name} -d

Summary:	RPC2 library
Name:		rpc2
Version:	2.10
Release:	2
License:	LGPL
URL:		http://www.coda.cs.cmu.edu
Source0:	ftp://ftp.wu-wien.ac.at/pub/systems/coda/src/%{name}-%{version}.tar.gz
Patch0:		rpc2-2.8-fix-format-errors.patch
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	liblwp-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
Group:		Development/Other

%description
RPC2 is a remote procedure call library layered on top of UDP sockets and is
used by the Coda distributed filesystem. 

%package -n	%{libname}
Summary:	RPC2 library development files
Group:		Development/Other

%description -n %{libname}
RPC2 is a remote procedure call library layered on top of UDP sockets and is
used by the Coda distributed filesystem. 

%package -n	%{develname}
Summary:	RPC2 library development files
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	rpc2-devel = %{version}-%{release}
Obsoletes:  %mklibname %{name}_ -d 4

%description -n %{develname}
Headers and static libraries for developing programs using the RPC2 library.

%prep
%setup -q
%patch0 -p 1

%build
%configure2_5x
%make

%install
%makeinstall

%files -n %{libname}
%{_libdir}/librpc2.so.*
%{_libdir}/libse.so.*

%files -n %{develname}
%doc NEWS
%{_bindir}/rp2gen
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/rpc2
%{_libdir}/pkgconfig/rpc2.pc


%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 2.10-1mdv2011.0
+ Revision: 645419
- update to new version 2.10

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.8-5mdv2011.0
+ Revision: 614716
- the mass rebuild of 2010.1 packages

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 2.8-4mdv2010.0
+ Revision: 442756
- rebuild

* Wed Mar 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.8-3mdv2009.1
+ Revision: 354015
- better description

* Fri Mar 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.8-2mdv2009.1
+ Revision: 349541
- fix devel package name

* Thu Mar 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.8-1mdv2009.1
+ Revision: 349450
- new version
- new devel policy

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.0-1mdv2008.1
+ Revision: 140747
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import rpc2


* Tue Aug  8 2006 Antoine Ginies <aginies@mandriva.com> 2.0-1mdv2007.0
- 2.0
- use mkrel

* Thu Feb 16 2006 Antoine Ginies <aginies@mandriva.com> 1.28-1mdk
- 1.28

* Fri Jan 21 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.26-1mdk
- 1.26
- use %%mklibname
- cosmetics
- new major
- fix provides

* Sat Dec 21 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.14-1mdk
- 1.14
- Fix Requires/Provides

* Wed Jul 24 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.13-2mdk
- rebuild for new readline

* Mon Nov 12 2001 Florin <florin@mandrakesoft.com> 1.13-1mdk
- 1.13
- add url tag

* Sat Nov  3 2001 Stefan van der Eijk <stefan@eijk.nu> 1.12-2mdk
- BuildRequires: ncurses-devel

* Thu Aug 23 2001 Florin Grad <florin@mandrakesoft.com> 1.12-1mdk
- 1.12
- License entry

* Tue Jun 12 2001 Stefan van der Eijk <stefan@eijk.nu> 1.11-2mdk
- Provides: rpc2-devel

* Tue Jun 12 2001 Stefan van der Eijk <stefan@eijk.nu> 1.11-1mdk
- 1.11
- BuildRequires: flex lwp-devel readline-devel
- add Provides for devel package

* Mon Jan 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.8-2mdk
- rebuild

* Thu Nov 16 2000 Florin Grad <florin@mandrakesoft.com> 1.8-1mdk
- 1.8
- lib split compliant
* Fri Sep 15 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.5-3mdk
- BM
- macros
* Thu Aug 31 2000 Florin Grad <florin@mandrakesoft.com> 1.5-2mdk
- adding macros
* Fri Jul 7 2000 Florin Grad <florin@mandrakesoft.com> 1.5-1mdk
- First attempt.
