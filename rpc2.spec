%define	name	rpc2
%define	version	2.0
%define	release	%mkrel 1
%define	major	4
%define	libname	%mklibname %{name}_ %{major}

Summary:	RPC2 library
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
URL:		http://www.coda.cs.cmu.edu
License:	LGPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	flex liblwp-devel ncurses-devel readline-devel
Group:		Development/Other

%description
The RPC2 library.

%package -n	%{libname}
Summary:	RPC2 library development files
Group:		Development/Other

%description -n %{libname}
The RPC2 library.

%package -n	%{libname}-devel
Summary:	RPC2 library development files
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	rpc2-devel = %{version}-%{release}

%description -n %{libname}-devel
Headers and static libraries for developing programs using the RPC2 library.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
chmod 755 $RPM_BUILD_ROOT%{_libdir}/libfail.so.*
chmod 755 $RPM_BUILD_ROOT%{_libdir}/librpc2.so.*
chmod 755 $RPM_BUILD_ROOT%{_libdir}/libse.so.*

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -p /sbin/ldconfig -n %{libname}
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig -n %{libname}
%endif

%files 
%defattr(-,root,root)
%doc NEWS
%{_bindir}/filcon

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libfail.so.*
%{_libdir}/librpc2.so.*
%{_libdir}/libse.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_bindir}/rp2gen
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%dir %{_includedir}/rpc2
%{_includedir}/rpc2/*

