
%define		_sname		lives
%define		_pre		pre6
%define		_themesdir	%{_datadir}/%{_sname}/themes

Summary:	LiVES is the Linux Video Editing System
Summary(pl):	LiVEA jest Linuksowym Systemem Edycji Video
Name:		LiVES
Version:	0.9.1
Release:	0.%{_pre}.2
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.xs4all.nl/%7Esalsaman/lives/current/%{name}-%{version}-%{_pre}-src.tar.bz2
# Source0-md5:	8088d0f11b92a3792b9feb6338c11aa4
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.in-path.patch
Patch1:		%{name}-plugins-python.patch
URL:		http://www.xs4all.nl/~salsaman/lives/
BuildRequires:	freetype-devel
BuildRequires:	gtk+2-devel
BuildRequires:	pango-devel
Requires:	ImageMagick
Requires:	gdk-pixbuf
Requires:	libjpeg
Requires:	mplayer >= 0.90rc1
Requires:	perl
Requires:	python >= 1:2.3
Requires:	%{name}-plugins = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LiVES began as the Linux Video Editing System. Since it now runs on
more operating systems, LiVES is a Video Editing System. It is
designed to be simple to use, yet powerful. It is small in size, yet
it has many advanced features.

%description -l pl
LiVES zaczyna³ jako Linuksowy System Edycji Video. Obecnie mo¿na
równie¿ uruchomiæ go na wiêkszej ilo¶ci systemów operacyjnych. 
Zaprojektowany zosta³ tak, by byæ zarówno prostym w u¿yciu jak
i mimo niewielkiego rozmiaru posiadaæ zaawansowane funkcje.

%package plugins
Summary:	Plugins for LiVES
Summary(pl):	Wtyczki dla LiVES
Group:		X11/Applications/Multimedia

%description plugins
Plugins for LiVES.

%description plugins -l pl
Wtyczki (plugins) dla LiVES.

%package themes
Summary:	Themes for LiVES
Summary(pl):	Motywy dla LiVES
Group:		Themes/GTK+

%description themes
Themes for LiVES.

%description themes -l pl
Motywy dla LiVES.

%prep
%setup -q -n %{name}-%{version}-%{_pre}
gzip -dc %{_sname}-plugins-%{version}-%{_pre}.tar.gz | tar -xf -
gzip -dc %{_sname}-themes-%{version}-%{_pre}.tar.gz | tar -xf -
%patch0 -p1
%patch1 -p0

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/%{_sname},%{_desktopdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -r plugins $RPM_BUILD_ROOT%{_datadir}/%{_sname}/
cp -r themes $RPM_BUILD_ROOT%{_datadir}/%{_sname}/
cp -r icons $RPM_BUILD_ROOT%{_datadir}/%{_sname}/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{_sname}/icons
%{_desktopdir}/%{name}.desktop
%{_themesdir}/default

%files themes
%defattr(644,root,root,755)
%{_themesdir}/camera
%{_themesdir}/cutting_room
%{_themesdir}/greenish
%{_themesdir}/pinks
%{_themesdir}/sunburst

%files plugins
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/%{_sname}/plugins
