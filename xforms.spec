Summary:	Graphical user interface toolkit for X Window Systems
Summary(pl):	Narzêdzia do tworzenia GUI dla X Window
Name:		xforms
Version:	0.89
Release:	3
License:	noncommercial distributable (see Copyright)
Group:		X11/Libraries
Source0:	ftp://ncmir.ucsd.edu:/pub/xforms/linux-i386/elf/bxform-089-glibc2.1-x86.tgz
Source2:	ftp://ncmir.ucsd.edu:/pub/xforms/linux-alpha/bxform-089-glibc2.1-alpha.tgz
Source3:	ftp://ncmir.ucsd.edu:/pub/xforms/linux-sparc/bxform-089-glibc2.1-sparc.tgz
Source4:	ftp://einstein.phys.uwm.edu/pub/xforms/DOC/forms_sngl.ps.gz
Patch0:		bxform-mkconfig.patch
Patch1:		bxform-config.patch
BuildRequires:	XFree86-devel
Exclusivearch:	%{ix86} alpha sparc sparc64
URL:		http://world.std.com/~xforms/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XForms is a GUI toolkit based on Xlib for X Window Systems. It
features a rich set of objects, such as buttons, sliders, and menus
etc. integrated into an easy and efficient object/event callback
execution model that allows fast and easy construction of
X-applications. In addition, the library is extensible and new objects
can easily be created and added to the library.

%description -l pl
XForms jest zbiorem narzêdzi bazuj±cym na Xlib do tworzenia GUI dla
Systemów X Windows. Jego zalety to bogata ilo¶æ obiektów takich jak
przyciski, menu itp. zintegrowane w prosty i efektywny model, który
pozwala na szybkie i ³atwe tworzenie X-aplikacji.

%package demos
Summary:	xforms library demo programs
Summary(pl):	programy demo u¿ywaj±ce biblioteki XForms
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description demos
Demos using the XForms library.

%description demos -l pl
Dema u¿ywaj±ce biblioteki XForms.

%package devel
Summary:	xforms - header files and development documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja bibliteki XForms
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	XFree86-devel

%description devel
Xforms - header files and development documentation.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja bibliteki XForms.

%package static
Summary:	xforms static libraries
Summary(pl):	Biblioteki statyczne XForms
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Xforms static libraries.

%description static -l pl
Biblioteki statyczne XForms.

%package -n fdesign
Summary:	fdesign - Forms Library User Interface Designer
Summary(pl):	fdesign - Projektant GUI
Group:		X11/Development/Tools
Requires:	%{name} = %{version}

%description -n fdesign
fdesign is a GUI builder that helps the construction of graphical user
interface in a WYSIWYG (what you see is what you get) way by allowing
the user to directly manipulate various objects, such as buttons,
sliders and menus etc. Once a satisfactory UI is constructed, the user
can save the composed interface into an external file containing some
program code. When compiled, linked with the Forms Library, and
executed, the generated code would, at run time (or print time for
PostScript output), construct the exact same interfaces as those seen
within fdesign.

%description -n fdesign -l pl
fdesign to GUI pomagaj±ce stworzyæ graficzny interfejs u¿ytkownika za
pomoc± edytora WYSIWYG pozwalaj±cego u¿ytkownikowi na bezpo¶rednie
manipulacje obiektami itp.

%prep
%ifarch %{ix86}
%setup -q -T -n xforms -b 0
%endif

%ifarch alpha
%setup -q -T -n xforms -b 2
%endif

%ifarch sparc sparc64
%setup -q -T -n xforms -b 3
%endif

%patch0 -p1
%patch1 -p1
install %{SOURCE4} .

%build
%{__make} demo CCFLAG="%{rpmcflags}"; %{__make} clean
rm -f DEMOS/*.orig

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/src/examples/xforms} \
	$RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir},%{_mandir}/man{1,5}}

%{__make} install \
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
install FORMS/glcanvas.c $RPM_BUILD_ROOT/usr/src/examples/xforms

install DESIGN/fdesign $RPM_BUILD_ROOT%{_bindir}

gzip -9nf FORMS/Readme Bugs Changes Copyright Readme

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
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files demos
%defattr(644,root,root,755)
%doc FORMS/Readme.gz
%attr(-,root,root) /usr/src/examples/xforms

%files -n fdesign
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
