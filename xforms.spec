Summary:	Graphical user interface toolkit for X Window Systems
Summary(pl):	Narzêdzia do tworzenia GUI dla X Window
Summary(pt_BR):	Biblioteca de Widgets para o X
Name:		xforms
Version:	1.0
Release:	3
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ncmir.ucsd.edu/pub/xforms/OpenSource/%{name}-%{version}-release.tgz
# Source0-md5: aed46678c9278dc68b7e6224661aa1c7
Source1:	ftp://einstein.phys.uwm.edu/pub/xforms/DOC/forms_sngl.ps.gz
# Source1-md5:	759f8a9f8f9d5ff8751814b44bbe07f6
Patch0:		%{name}-demo.patch
Patch1:		%{name}-make.patch
URL:		http://world.std.com/~xforms/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
# according to warning in README - old headers may break it
BuildConflicts:	xforms-devel < 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libforms1

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%define		_noautoreqdep	libGL.so.1

%description
XForms is a GUI toolkit based on Xlib for X Window Systems. It
features a rich set of objects, such as buttons, sliders, and menus
etc. integrated into an easy and efficient object/event callback
execution model that allows fast and easy construction of
X-applications. In addition, the library is extensible and new objects
can easily be created and added to the library.

%description -l pl
XForms jest zbiorem narzêdzi bazuj±cym na Xlib do tworzenia GUI dla
Systemów X Window. Jego zalety to bogata ilo¶æ obiektów takich jak
przyciski, menu itp. zintegrowane w prosty i efektywny model, który
pozwala na szybkie i ³atwe tworzenie X-aplikacji.

%description -l pt_BR
XForms é uma biblioteca de widgets para o X.

%package devel
Summary:	XForms - header files and development documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja bibliteki XForms
Summary(pt_BR):	Arquivos de cabeçalho para desenvolvedores XForms
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	XFree86-devel
Obsoletes:	libforms1-devel

%description devel
XForms - header files and development documentation.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja bibliteki XForms.

%description devel -l pt_BR
Este pacote contém arquivos de cabeçalho e ferramentas para
desenvolvedores XForms.

%package static
Summary:	XForms static libraries
Summary(pl):	Biblioteki statyczne XForms
Summary(pt_BR):	Biblioteca estática para desenvolvedores XForms
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	libforms1-static-devel

%description static
XForms static libraries.

%description static -l pl
Biblioteki statyczne XForms.

%description static -l pt_BR
Este pacote contém a versão estática da biblioteca XForms.

%package GL
Summary:	XForms GL canvas library
Summary(pl):	Biblioteka dodaj±ca obs³ugê GL do XForms
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL

%description GL
XForms GL canvas library.

%description GL -l pl
Biblioteka dodaj±ca obs³ugê GL do XForms.

%package GL-devel
Summary:	XForms GL canvas library headers
Summary(pl):	Nag³ówki biblioteki dodaj±cej obs³ugê GL do XForms
Group:		X11/Development/Libraries
Requires:	%{name}-GL = %{version}
Requires:	%{name}-devel = %{version}
Requires:	OpenGL-devel

%description GL-devel
XForms GL canvas library header files.

%description GL-devel -l pl
Pliki nag³ówkowe biblioteki dodaj±cej obs³ugê GL do XForms.

%package GL-static
Summary:	XForms GL canvas static library
Summary(pl):	Statyczna biblioteka dodaj±ca obs³ugê GL do XForms
Group:		X11/Development/Libraries
Requires:	%{name}-GL-devel = %{version}

%description GL-static
XForms GL canvas static library.

%description GL-static -l pl
Statyczna biblioteka dodaj±ca obs³ugê GL do XForms.

%package demos
Summary:	XForms library demo programs
Summary(pl):	Programy demonstracyjne u¿ywaj±ce biblioteki XForms
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description demos
Demos using the XForms library.

%description demos -l pl
Programy demonstracyjne u¿ywaj±ce biblioteki XForms.

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
program code. When compiled, linked with the XForms Library, and
executed, the generated code would, at run time (or print time for
PostScript output), construct the exact same interfaces as those seen
within fdesign.

%description -n fdesign -l pl
fdesign to GUI pomagaj±ce stworzyæ graficzny interfejs u¿ytkownika za
pomoc± edytora WYSIWYG pozwalaj±cego u¿ytkownikowi na bezpo¶rednie
manipulowanie ró¿nymi obiektami, takimi jak przyciski, suwaki, menu
itp. Po skonstruowaniu odpowiadaj±cego UI u¿ytkownik mo¿e zapisaæ
zaprojektowany interfejs do zewnêtrznego pliku zawieraj±cego czê¶æ
kodu programu. Po skompilowaniu i skonsolidowaniu z bibliotek± XForms,
uruchomiony program utworzy (lub wydrukuje w przypadku wyj¶cia do
PostScriptu) dok³adnie ten sam interfejs, który by³ widoczny w
fdesign.

%prep
%setup -q -n %{name}-%{version}-release
%patch0 -p1
%patch1 -p1
install %{SOURCE1} .

%build
xmkmf -a

%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir},%{_mandir}/man5}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT

install lib/xforms.5 $RPM_BUILD_ROOT%{_mandir}/man5
echo ".so xforms.5" > $RPM_BUILD_ROOT%{_mandir}/man5/forms.5

cp -a demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
rm -f $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/{.depend,01Readme,*.{os2,bak,orig,o}}

find $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} -type f -perm -0700 | \
	sed -e "s@^$RPM_BUILD_ROOT@%attr(755,root,root) @" > %{name}-demosbin.list

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   GL -p /sbin/ldconfig
%postun GL -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc 00README Changes Copyright
%attr(755,root,root) %{_libdir}/libforms.so.*.*
%attr(755,root,root) %{_libdir}/libflimage.so.*.*
%{_mandir}/man5/*

%files devel
%defattr(644,root,root,755)
%doc forms_sngl.ps.gz
%attr(755,root,root) %{_libdir}/libforms.so
%attr(755,root,root) %{_libdir}/libflimage.so
%{_includedir}/forms.h
%{_includedir}/flimage.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libforms.a
%{_libdir}/libflimage.a

%files GL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libformsGL.so.*.*

%files GL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libformsGL.so
%{_includedir}/glcanvas.h

%files GL-static
%defattr(644,root,root,755)
%{_libdir}/libformsGL.a

%files demos -f %{name}-demosbin.list
%defattr(644,root,root,755)
%doc demos/01Readme
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/fd
%{_examplesdir}/%{name}-%{version}/*akefile*
%{_examplesdir}/%{name}-%{version}/*.[1ch]
%{_examplesdir}/%{name}-%{version}/*.fd
%{_examplesdir}/%{name}-%{version}/*.menu
%{_examplesdir}/%{name}-%{version}/*.ps
%{_examplesdir}/%{name}-%{version}/*.x[bp]m
%{_examplesdir}/%{name}-%{version}/xyover

%files -n fdesign
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
