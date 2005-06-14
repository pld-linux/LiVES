
%define		_sname		lives
%define		_pre		pre3

Summary:	LiVES - the Linux Video Editing System
Summary(pl):	LiVES - Linuksowy System Edycji Video
Name:		LiVES
Version:	0.9.5
Release:	0.%{_pre}.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.xs4all.nl/%7Esalsaman/lives/current/%{name}-%{version}-%{_pre}.tar.bz2
# Source0-md5:	722f848a002084bb8f520a85ea5be756
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.am-path.patch
URL:		http://www.xs4all.nl/~salsaman/lives/
BuildRequires:	SDL-devel
BuildRequires:	automake >= 1:1.7
BuildRequires:	autoconf >= 2.57
BuildRequires:	gettext-devel >= 0.14.1
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libtheora-devel
BuildRequires:	libtool
BuildRequires:	libvisual-devel
BuildRequires:	mjpegtools-devel
BuildRequires:	pkgconfig
Requires:	%{name}-plugins = %{version}-%{release}
Requires:	ImageMagick >= 5
Requires:	ffmpeg
Requires:	mplayer >= 0.90rc1
Requires:	ogmtools
Requires:	perl-base
Requires:	python >= 1:2.3
Requires:	sox
Requires:	transcode
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	%{_datadir}/%{_sname}/themes

%description
LiVES began as the Linux Video Editing System. Since it now runs on
more operating systems, LiVES is a Video Editing System. It is
designed to be simple to use, yet powerful. It is small in size, yet
it has many advanced features.

%description -l pl
LiVES zaczyna³ jako Linuksowy System Edycji Video. Obecnie mo¿na
równie¿ uruchomiæ go na wiêkszej liczbie systemów operacyjnych.
Zaprojektowany zosta³ tak, by byæ zarówno prostym w u¿yciu jak
i mimo niewielkiego rozmiaru posiadaæ zaawansowane funkcje.

%package plugins
Summary:	Plugins for LiVES
Summary(pl):	Wtyczki dla LiVES
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description plugins
Plugins for LiVES.

%description plugins -l pl
Wtyczki (plugins) dla LiVES.

%package themes
Summary:	Themes for LiVES
Summary(pl):	Motywy dla LiVES
Group:		Themes/GTK+
Requires:	%{name} = %{version}-%{release}

%description themes
Themes for LiVES.

%description themes -l pl
Motywy dla LiVES.

%prep
%setup -q -n %{_sname}-%{version}-%{_pre}
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make} \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_datadir}/lives/plugins/effects/rendered
for i in lives-plugins/plugins/effects/RFXscripts/*.script ; do
	./build-lives-rfx-plugin $i $RPM_BUILD_ROOT%{_datadir}/lives/plugins/effects/rendered
done

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_docdir}/%{_sname}-%{version}-%{_pre} \
	$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%find_lang %{_sname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{_sname}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS CHANGELOG FEATURES GETTING.STARTED NEWS RFX OMC
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{_sname}
%{_datadir}/%{_sname}/icons
%{_desktopdir}/%{name}.desktop
%dir %{_themesdir}
%{_themesdir}/default

%files themes
%defattr(644,root,root,755)
%{_themesdir}/camera
%{_themesdir}/cutting_room
%{_themesdir}/greenish
%{_themesdir}/pinks
%{_themesdir}/sunburst
%{_themesdir}/editor

%files plugins
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/%{_sname}/plugins
