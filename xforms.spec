Summary:	Graphical user interface toolkit for X Window Systems
Name:		xforms
Version:	0.88
Release:	8
Copyright:	noncommercial distributable (see Copyright)
Group:		Development/Libraries
Source0:	ftp://einstein.phys.uwm.edu/pub/xforms/linux/elf/bxform-088-glibc.tgz
Source1:	ftp://einstein.phys.uwm.edu/pub/xforms/linux-sparc/bxform-088.sparc.tgz
Source2:	ftp://einstein.phys.uwm.edu/pub/xforms/linux-alpha/elf/bxform-088.alpha.tgz
Source3:	ftp://einstein.phys.uwm.edu/pub/xforms/DOC/forms_sngl.ps.gz
Source10:	fdesign.wmconfig
Patch0:		bxform-mkconfig.patch
Patch1:		bxform-config.patch
URL:		http://bragg.phys.uwm.edu/xforms/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6
%define		_mandir	%{_prefix}/man

%description
XForms is a GUI toolkit based on Xlib for X Window Systems. It features a
rich set of objects, such as buttons, sliders, and menus etc.  integrated
into an easy and efficient object/event callback execution model that allows
fast and easy construction of X-applications. In addition, the library is
extensible and new objects can easily be created and added to the library.

%package demos
Group:       Development/Libraries
Summary:     xforms library demo programs
Requires:    %{name} = %{version}

%description demos
Demos using the XForms library

%package devel
Summary:     xforms - header files and development documentation
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description devel
Xforms - header files and development documentation.

%package static
Summary:     xforms static libraries
Group:       Development/Libraries
Requires:    %{name}-devel = %{version}

%description static
Xforms static libraries.

%package -n fdesign
Summary:     fdesign -  Forms Library User Interface Designer
Group:       Development/Building
Requires:    %{name} = %{version}

%description -n fdesign
fdesign is a GUI builder that helps the construction of graphical user
interface in a WYSIWYG (what you see is what you get) way by allowing the
user to directly manipulate various objects, such as buttons, sliders and
menus etc. Once a satisfactory UI is constructed, the user can save the
composed interface into an external file containing some program code. When
compiled, linked with the Forms Library, and executed, the generated code
would, at run time (or print time for PostScript output), construct the
exact same interfaces as those seen within fdesign.

%prep
%ifarch i386 i486 i586 i686
%setup -q -T -n xforms -b 0
%endif

%ifarch sparc sparc64
%setup -q -T-n xforms -b 1
%endif

%ifarch alpha
%setup -q -T-n xforms -b 2
%endif

%patch0 -p1

cp %{SOURCE3} .
%patch1 -p1

%build
make demo CCFLAG="$RPM_OPT_FLAGS"; make clean
rm -f DEMOS/*.orig

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/src/examples/xforms} \
	$RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir},%{_mandir}/man{1,5}}

make install \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	LIB_DIR=$RPM_BUILD_ROOT%{_libdir} \
	MAN1_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	MAN5_DIR=$RPM_BUILD_ROOT%{_mandir}/man5 \
	HEADER_DIR=$RPM_BUILD_ROOT%{_includedir}

rm -rf $RPM_BUILD_ROOT%{_mandir}/man5/forms.5
echo ".so xforms.5" > $RPM_BUILD_ROOT%{_mandir}/man5/forms.5

ln -sf libforms.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libforms.so

cp -a contrib $RPM_BUILD_ROOT/usr/src/examples/xforms
install mkconfig.h $RPM_BUILD_ROOT/usr/src/examples/xforms
cp -a DEMOS $RPM_BUILD_ROOT/usr/src/examples/xforms
install FORMS/gl.c $RPM_BUILD_ROOT/usr/src/examples/xforms

install %{SOURCE10} $RPM_BUILD_ROOT/etc/X11/wmconfig/fdesign
install DESIGN/fdesign $RPM_BUILD_ROOT%{_bindir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf FORMS/Readme Bugs Changes Copyright Readme \
	$RPM_BUILD_ROOT%{_mandir}/man*/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc forms_sngl.ps.gz {Bugs,Changes,Copyright,Readme}.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%attr(644,root,root) %{_libdir}/lib*.a

%files demos
%defattr(644,root,root,755)
%doc FORMS/Readme.gz
%attr(-,root,root) /usr/src/examples/xforms

%files -n fdesign
%defattr(644,root,root)
/etc/X11/wmconfig/fdesign
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
