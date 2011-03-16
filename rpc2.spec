%define	name	rpc2
%define	version	2.10
%define	release	%mkrel 1
%define	major	4
%define	libname	    %mklibname %{name}_ %{major}
%define	develname	%mklibname %{name} -d

Summary:	RPC2 library
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPL
URL:		http://www.coda.cs.cmu.edu
Source0:	ftp://ftp.wu-wien.ac.at/pub/systems/coda/src/%{name}-%{version}.tar.gz
Patch:      rpc2-2.8-fix-format-errors.patch
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	liblwp-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%patch -p 1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig -n %{libname}
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig -n %{libname}
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/librpc2.so.*
%{_libdir}/libse.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc NEWS
%{_bindir}/rp2gen
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/rpc2
%{_libdir}/pkgconfig/rpc2.pc
