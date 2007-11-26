# TODO
# - unfortunately it crashes in weed_plugin_info_init (alien_overlay.wo)
# - some platform-independent left in %{_libdir}
# - LiVES req LiVES-plugins which req LiVES; it sucks

%define		_sname		lives

Summary:	LiVES - the Linux Video Editing System
Summary(pl.UTF-8):	LiVES - Linuksowy System Edycji Video
Name:		LiVES
Version:	0.9.8.6
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.xs4all.nl/%7Esalsaman/lives/current/%{name}-%{version}.tar.bz2
# Source0-md5:	c73aed9b2da4fc74d51f9e92fae7439d
Source1:	%{name}.desktop
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-automake.patch
URL:		http://www.xs4all.nl/~salsaman/lives/
BuildRequires:	SDL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-devel >= 0.14.1
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libtheora-devel
BuildRequires:	libtool
BuildRequires:	libvisual-devel
BuildRequires:	mjpegtools-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-util-imake
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

# workaround for the next change
%define		_localedir	%{_usr}/share/locale
# platform-dependent plugins in %{_datadir}
%define		_datadir	%{_libdir}
%define		_themesdir	%{_datadir}/%{_sname}/themes
# shared objects without .so (e.g. SDL), which we don't want to provide
%define		_noautoprovfiles	^%{_datadir}/%{_sname}/.*

%description
LiVES began as the Linux Video Editing System. Since it now runs on
more operating systems, LiVES is a Video Editing System. It is
designed to be simple to use, yet powerful. It is small in size, yet
it has many advanced features.

%description -l pl.UTF-8
LiVES zaczynał jako Linuksowy System Edycji Video. Obecnie można
również uruchomić go na większej liczbie systemów operacyjnych.
Zaprojektowany został tak, by być zarówno prostym w użyciu jak i mimo
niewielkiego rozmiaru posiadać zaawansowane funkcje.

%package plugins
Summary:	Plugins for LiVES
Summary(pl.UTF-8):	Wtyczki dla LiVES
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description plugins
Plugins for LiVES.

%description plugins -l pl.UTF-8
Wtyczki (plugins) dla LiVES.

%package themes
Summary:	Themes for LiVES
Summary(pl.UTF-8):	Motywy dla LiVES
Group:		Themes/GTK+
Requires:	%{name} = %{version}-%{release}

%description themes
Themes for LiVES.

%description themes -l pl.UTF-8
Motywy dla LiVES.

%prep
%setup -qn %{_sname}-%{version}
%patch0 -p1
%patch1 -p1

# wrrr
sed -i -e 's,/share/,/%{_lib}/,' po/pxgettext po/make_rfx_builtin_list.pl

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
# hack: DATADIRNAME defined too late in configure
%configure \
	DATADIRNAME=share
%{__make} \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_datadir}/lives/plugins/effects/rendered
for i in lives-plugins/plugins/effects/RFXscripts/*.script ; do
	./build-lives-rfx-plugin $i $RPM_BUILD_ROOT%{_datadir}/lives/plugins/effects/rendered
done

# hack: override localedir because of redefined datadir
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	localedir=%{_localedir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_docdir}/%{_sname}-%{version} \
	$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

mv -f $RPM_BUILD_ROOT%{_localedir}/de{_DE,}
mv -f $RPM_BUILD_ROOT%{_localedir}/nl{_NL,}

%find_lang %{_sname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{_sname}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog FEATURES GETTING.STARTED NEWS RFX OMC
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{_sname}
%{_datadir}/%{_sname}/icons
%{_datadir}/%{_sname}/default.keymap
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
