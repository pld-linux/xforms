Summary:     Graphical user interface toolkit for X Window Systems
Name:        xforms
Version:     0.88
Release:     6
Copyright:   noncommercial distributable (see Copyright)
Group:       Development/Libraries
Source0:     ftp://einstein.phys.uwm.edu/pub/xforms/linux/elf/bxform-088-glibc.tgz
Source1:     ftp://einstein.phys.uwm.edu/pub/xforms/linux-sparc/bxform-088.sparc.tgz
Source2:     ftp://einstein.phys.uwm.edu/pub/xforms/linux-alpha/elf/bxform-088.alpha.tgz
Source3:     ftp://einstein.phys.uwm.edu/pub/xforms/DOC/forms_sngl.ps.gz
Source10:    fdesign.wmconfig
Patch0:      bxform-088-mkconfig.patch
Patch1:      bxform-088-1-config.patch
BuildRoot:   /tmp/%{name}-%{version}-root
URL:         http://bragg.phys.uwm.edu/xforms/

%ifarch alpha
AutoReqProv: 0
Requires: libc.so.6.1
%endif

%description
XForms is a GUI toolkit based on Xlib for X Window Systems. It features a
rich set of objects, such as buttons, sliders, and menus etc.  integrated
into an easy and efficient object/event callback execution model that allows
fast and easy construction of X-applications. In addition, the library is
extensible and new objects can easily be created and added to the library.

%package demos
Group:       Development/Libraries
Summary:     xforms library demo programs
Requires:    %{name} = %{version}, %{name}-devel = %{version}

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
%ifarch i386
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
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/{lib/xforms,X11R6/{lib,bin,include,man/man{1,5}}}}

make	install \
	BIN_DIR=$RPM_BUILD_ROOT/usr/X11R6/bin \
	LIB_DIR=$RPM_BUILD_ROOT/usr/X11R6/lib \
	MAN1_DIR=$RPM_BUILD_ROOT/usr/X11R6/man/man1 \
	MAN5_DIR=$RPM_BUILD_ROOT/usr/X11R6/man/man5 \
	HEADER_DIR=$RPM_BUILD_ROOT/usr/X11R6/include
ln -sf libforms.so.%{version} $RPM_BUILD_ROOT/usr/X11R6/lib/libforms.so

cp -a contrib $RPM_BUILD_ROOT%{_libdir}/xforms
install mkconfig.h $RPM_BUILD_ROOT%{_libdir}/xforms
cp -a DEMOS $RPM_BUILD_ROOT%{_libdir}/xforms
install FORMS/gl.c $RPM_BUILD_ROOT%{_libdir}/xforms

install %{SOURCE10} $RPM_BUILD_ROOT/etc/X11/wmconfig/fdesign
install DESIGN/fdesign $RPM_BUILD_ROOT/usr/X11R6/bin

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc forms_sngl.ps.gz Bugs Changes Copyright Readme
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*
/usr/X11R6/man/man5/*

%files devel
%defattr(644,root,root,755)
/usr/X11R6/lib/lib*.so
/usr/X11R6/include/*.h

%files static
%attr(644,root,root) /usr/X11R6/lib/lib*.a

%files demos
%defattr(644,root,root,755)
%doc FORMS/Readme
%attr(-,root,root) %{_libdir}/xforms/

%files -n fdesign
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/fdesign
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/man/man1/*

%changelog
* Fri Sep 25 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.88-6]
- addes static subpackage.

* Wed May  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.88-5]
- added -q %setup parameter,
- Changed Provides to libforms.so.0.86,
- added Require infos in subpackages,
- added using %%{name} and %%{version} macros in Buildroot,
- added using $RPM_OPT_FLAGS during compilation,
- spec file rewrited for using Buildroot,
- added generating separated package with fdisign,
- /usr/X11R6/lib/lib*.so moved to devel
- added %clean section,
- added URL,
- added %defattr and %attr macros in %files (allows building package from
  non-root account).

* Mon Dec  8 1997 Otto Hammersmith <otto@redhat.com>
- fixed alpha library dependency problems.

* Sun Dec  7 1997 Otto Hammersmith <otto@redhat.com>
- add provides for the .81 libs

* Tue Dec  2 1997 Otto Hammersmith <otto@redhat.com>
- buildrooted

* Wed Nov 19 1997 Otto Hammersmith <otto@redhat.com>
- updated to 0.88

* Tue Apr 8 1997 Michael Fulbright <msf@redhat.com>
- Updated package to version 0.86.
