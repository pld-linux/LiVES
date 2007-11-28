# TODO
# - weed plugins don't work - segfault in weed_plugin_info_init
#   (looks like #1743701 #1645153)
# - lots platform-independent left in %{_libdir}
# - python encoders installed in _bindir
# - check -plugins-* descriptions
# - build with OSC support (http://www.cnmat.berkeley.edu/OpenSoundControl/index.html)
# - build with frei0r support (www.piksel.org/frei0r)
# - create spec for http://www.flyn.org/projects/qtutils/index.html and package qtutils_encoder
# - create spec for http://sswf.sourceforge.net and package sswf_encoder

# Conditional build:
%bcond_without	sdl		# build without SDL plugin
%bcond_without	mjpeg		# build without mjpegtools plugin
%bcond_without	libvisual	# disable libvisual support
%bcond_without	jack		# without JACKD support
%bcond_without	dvgrab		# build without dv grabbing support

%define		_sname		lives

Summary:	LiVES - the Linux Video Editing System
Summary(pl.UTF-8):	LiVES - Linuksowy System Edycji Video
Name:		LiVES
Version:	0.9.8.6
Release:	0.4
License:	GPL v3
Group:		X11/Applications/Multimedia
Source0:	http://www.xs4all.nl/%7Esalsaman/lives/current/%{name}-%{version}.tar.bz2
# Source0-md5:	c73aed9b2da4fc74d51f9e92fae7439d
Source1:	%{name}.desktop
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-automake.patch
Patch2:		%{name}-without_sdl.patch
Patch3:		%{name}-defined_python_plugins_dir.patch
URL:		http://www.xs4all.nl/~salsaman/lives/
%{?with_sdl:BuildRequires:	SDL-devel}
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-devel >= 0.14.1
BuildRequires:	gtk+2-devel >= 2.0.0
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
%{?with_dvgrab:BuildRequires:	libavc1394-devel}
BuildRequires:	liboil-devel
%{?with_dvgrab:BuildRequires:	libraw1394-devel}
BuildRequires:	libtheora-devel
BuildRequires:	libtool
%{?with_libvisual:BuildRequires:	libvisual-devel}
%{?with_mjpeg:BuildRequires:	mjpegtools-devel}
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-util-imake
Requires:	ogmtools
Requires:	python >= 1:2.3
# required either mplayer or sox
Requires:	sox
Suggests:	ImageMagick >= 5
Suggests:	cdda2wav
Suggests:	dbgrab
Suggests:	mplayer >= 0.90rc1
Suggests:	xmms
Suggests:	xorg-app-xset
Suggests:	%{name}-plugins-encoders = %{version}-%{release}
Suggests:	%{name}-plugins-rendered = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		python_plugins_dir %{_datadir}/%{_sname}/plugins/python/
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
Summary:	Plugins for LiVES (metapackage)
Summary(pl.UTF-8):	Wtyczki dla LiVES (metapakiet)
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugins-encoders-perl = %{version}-%{release}
Requires:	%{name}-plugins-encoders-python = %{version}-%{release}
Requires:	%{name}-plugins-playback = %{version}-%{release}
Requires:	%{name}-plugins-rendered = %{version}-%{release}
Requires:	%{name}-plugins-RFXscripts = %{version}-%{release}
Requires:	%{name}-plugins-weed = %{version}-%{release}

%description plugins
Plugins for LiVES (metapackage).

%description plugins -l pl.UTF-8
Wtyczki (plugins) dla LiVES (metapakiet).

%package plugins-encoders-perl
Summary:	Perl encoders plugins for LiVES
Summary(pl.UTF-8):	Perlowe wtyczki kodujące dla LiVES
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	ImageMagick > 5
Requires:	dv
Requires:	ffmpeg
Requires:	ghostscript
Requires:	mjpegtools
Requires:	perl-base
Requires:	transcode
Requires:	vorbis-tools

%description plugins-encoders-perl
Perl encoders plugins for LiVES.

%description plugins-encoders-perl -l pl.UTF-8
Perlowe wtyczki (plugins) kodujące dla LiVES.

%package plugins-encoders-python
Summary:	Pythonowe encoders plugins for LiVES
Summary(pl.UTF-8):	Pythonowe wtyczki kodujące dla LiVES
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	python

%description plugins-encoders-python
Python encoders plugins for LiVES.

%description plugins-encoders-python -l pl.UTF-8
Pythonowe wtyczki (plugins) kodujące dla LiVES.

%package plugins-playback
Summary:	Playback plugins for LiVES
Summary(pl.UTF-8):	Wtyczki odtwarzające dla LiVES
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description plugins-playback
Playback plugins for LiVES.

%description plugins-playback -l pl.UTF-8
Wtyczki (plugins) odtwarzające dla LiVES.

%package plugins-rendered
Summary:	Rendered plugins for LiVES
Summary(pl.UTF-8):	Wtyczki rendered dla LiVES
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	ImageMagick >= 5

%description plugins-rendered
Rendered plugins for LiVES.

%description plugins-rendered -l pl.UTF-8
Wtyczki (plugins) rendered dla LiVES.

%package plugins-RFXscripts
Summary:	RFXscripts plugins for LiVES
Summary(pl.UTF-8):	Wtyczki RFXscripts dla LiVES
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description plugins-RFXscripts
RFXscripts plugins for LiVES.

%description plugins-RFXscripts -l pl.UTF-8
Wtyczki (plugins) RFXscripts dla LiVES.

%package plugins-weed
Summary:	Weed plugins for LiVES
Summary(pl.UTF-8):	Wtyczki weed dla LiVES
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description plugins-weed
Weed plugins for LiVES.

%description plugins-weed -l pl.UTF-8
Wtyczki (plugins) weed dla LiVES.

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
%{!?with_sdl:%patch2 -p1}
%patch3 -p1

sed -i -e "#^PYTHON_PLUGINS_DIR#s#^.*#PYTHON_PLUGINS_DIR = %{python_plugins_dir}/#" \
	lives-plugins/plugins/encoders/multi_encoder

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{!?with_dvgrab:--disable-dvgrab} \
	%{!?with_sdl:--disable-sdl}
%{__make} \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install -d $RPM_BUILD_ROOT%{_datadir}/lives/plugins/effects/rendered
for i in lives-plugins/plugins/effects/RFXscripts/*.script ; do
	./build-lives-rfx-plugin $i $RPM_BUILD_ROOT%{_datadir}/lives/plugins/effects/rendered
done

%{__make} install \
	marcosencodersdir=%{python_plugins_dir} \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_bindir}/autolives.pl
%attr(755,root,root) %{_bindir}/build-lives-rfx-plugin
%attr(755,root,root) %{_bindir}/build-lives-rfx-plugin-multi
%attr(755,root,root) %{_bindir}/lives
%attr(755,root,root) %{_bindir}/lives-exe
%attr(755,root,root) %{_bindir}/midistart
%attr(755,root,root) %{_bindir}/midistop
%attr(755,root,root) %{_bindir}/sendOSC
%attr(755,root,root) %{_bindir}/smogrify
%dir %{_datadir}/%{_sname}
%dir %{_datadir}/%{_sname}/plugins
%dir %{_datadir}/%{_sname}/plugins/effects
%dir %{_datadir}/%{_sname}/plugins/encoders
%dir %{_libdir}/%{_sname}
%dir %{_libdir}/%{_sname}/plugins
%dir %{_libdir}/%{_sname}/plugins/effects
%{_datadir}/%{_sname}/icons
%{_datadir}/%{_sname}/default.keymap
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{_sname}.xpm
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

%files plugins-encoders-perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/%{_sname}/plugins/encoders/encodedv_encoder
%attr(755,root,root) %{_datadir}/%{_sname}/plugins/encoders/ffmpeg_encoder
%attr(755,root,root) %{_datadir}/%{_sname}/plugins/encoders/mencoder_encoder
%attr(755,root,root) %{_datadir}/%{_sname}/plugins/encoders/mjpegtools_encoder
%attr(755,root,root) %{_datadir}/%{_sname}/plugins/encoders/pdf_encoder
#%attr(755,root,root) %{_datadir}/%{_sname}/plugins/encoders/qtutils_encoder
#%attr(755,root,root) %{_datadir}/%{_sname}/plugins/encoders/sswf_encoder
%attr(755,root,root) %{_datadir}/%{_sname}/plugins/encoders/transcode_encoder
 

%files plugins-encoders-python
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/%{_sname}/plugins/encoders/multi_encoder
%attr(755,root,root) %{python_plugins_dir}

%files plugins-playback
%defattr(644,root,root,755)
%dir %{_libdir}/%{_sname}/plugins/playback
%dir %{_libdir}/%{_sname}/plugins/playback/video
%{?with_sdl:%attr(755,root,root) %{_libdir}/%{_sname}/plugins/playback/video/SDLp}
%{?with_mjpeg:%attr(755,root,root) %{_libdir}/%{_sname}/plugins/playback/video/yuv4mpeg_stream}

%files plugins-rendered
%defattr(644,root,root,755)
%dir %{_datadir}/%{_sname}/plugins/effects/rendered
%attr(755,root,root) %{_datadir}/%{_sname}/plugins/effects/rendered/*

%files plugins-RFXscripts
%defattr(644,root,root,755)
%dir %{_datadir}/%{_sname}/plugins/effects/RFXscripts
%attr(755,root,root) %{_datadir}/%{_sname}/plugins/effects/RFXscripts/*.script

%files plugins-weed
%dir %{_libdir}/%{_sname}/plugins/effects/realtime
%dir %{_libdir}/%{_sname}/plugins/effects/realtime/weed
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/alien_overlay.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/audio_volume.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/blurzoom.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/bump2d.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/ccorrect.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/colorkey.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/compositor.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/deinterlace.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/edge.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/fg_bg_removal.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/fireTV.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/gdk_fast_resize.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/haip.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/layout_blends.wo
%{?with_libvisual:%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/libvis.wo}
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/lifeTV.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/mirrors.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/multi_blends.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/negate.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/noise.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/onedTV.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/plasma.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/posterise.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/rippleTV.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/rotozoom.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/simple_blend.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/slide_over.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/targeted_zoom.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/textfun.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/vertigo.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/videowall.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/warpTV.wo
%attr(755,root,root) %{_libdir}/%{_sname}/plugins/effects/realtime/weed/xeffect.wo
