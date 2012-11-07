Summary:	GNOME Desktop Environment with additional packages
Summary(pl.UTF-8):	Środowisko graficzne GNOME z dodatkowymi pakietami
Name:		metapackage-gnome
Version:	3.6.0
Release:	1
License:	GPL/LGPL
Group:		X11/Applications
Requires:	%{name}-accessibility = %{version}-%{release}
Requires:	%{name}-admin = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-desktop = %{version}-%{release}
Requires:	%{name}-devtools = %{version}-%{release}
Requires:	%{name}-games = %{version}-%{release}
Requires:	%{name}-office = %{version}-%{release}
Requires:	banshee >= 2.6.0
Requires:	gstreamer-a52dec
Requires:	gstreamer-aac
Requires:	gstreamer-amrnb
Requires:	gstreamer-amrwb
Requires:	gstreamer-ass
Requires:	gstreamer-audio-effects-bad
Requires:	gstreamer cdio
Requires:	gstreamer-celt
Requires:	gstreamer-curl
Requires:	gstreamer-dts
Requires:	gstreamer-dvdread
Requires:	gstreamer-flite
Requires:	gstreamer-gme
Requires:	gstreamer-gsm
Requires:	gstreamer-lame
Requires:	gstreamer-mad
Requires:	gstreamer-mimic
Requires:	gstreamer-mjpegtools
Requires:	gstreamer-mms
Requires:	gstreamer-mpeg
Requires:	gstreamer-opencv
Requires:	gstreamer-plugins-bad
Requires:	gstreamer-plugins-ugly
Requires:	gstreamer-resindvd
Requires:	gstreamer-rtmp
Requires:	gstreamer-schroedinger
Requires:	gstreamer-sid
Requires:	gstreamer-soundtouch
Requires:	gstreamer-spc
Requires:	gstreamer-vpx
Requires:	gstreamer-x264
Requires:	gstreamer-zbar
# not ported to gstreamer 1.x
#Requires:	gstreamer-audiosink-nas
#Requires:	gstreamer-cdaudio
#Requires:	gstreamer-dc1394
#Requires:	gstreamer-dirac
#Requires:	gstreamer-gsettings
#Requires:	gstreamer-kate
#Requires:	gstreamer-ladspa
#Requires:	gstreamer-lv2
#Requires:	gstreamer-musepack
#Requires:	gstreamer-musicbrainz
#Requires:	gstreamer-mythtv
#Requires:	gstreamer-neon
#Requires:	gstreamer-ofa
#Requires:	gstreamer-sndfile
#Requires:	gstreamer-timidity
#Requires:	gstreamer-videosink-directfb
#Requires:	gstreamer-videosink-sdl
#Requires:	gstreamer-wildmidi
#Requires:	gstreamer-xvid
Requires:	liferea >= 1.8.9
# shotwell needs vala-0.14 support
#Requires:	shotwell
Suggests:	tracker
Obsoletes:	metapackage-gnome-extras
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Desktop Environment with additional packages (metapackage).

%description -l pl.UTF-8
Środowisko graficzne GNOME z dodatkowymi pakietami (metapakiet).

%package accessibility
Summary:	Accessibility packages for GNOME Desktop Environment
Summary(pl.UTF-8):	Pakiety ułatwień dostępu dla środowiska graficznego GNOME
Group:		X11/Applications/Accessibility
Requires:	%{name}-core = %{version}-%{release}
Requires:	at-spi2-atk >= 2.6.1
Requires:	at-spi2-core >= 2.6.1
Requires:	caribou >= 0.4.2
Requires:	dasher >= 4.11
#Requires:	gnome-mag >= 0.16.1
Requires:	gnome-speech >= 0.4.23
Requires:	mousetweaks >= 3.4.1
Requires:	orca >= 3.4.2
Provides:	metapackage-gnome-extras-accessibility
Obsoletes:	metapackage-gnome-extras-accessibility

%description accessibility
Accessibility packages for GNOME Desktop Environment.

%description accessibility -l pl.UTF-8
Pakiety ułatwień dostępu dla środowiska graficznego GNOME.

%package admin
Summary:	Administration packages for GNOME Desktop Environment
Summary(pl.UTF-8):	Pakiety do zarządzania środowiskiem graficznym GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	pessulus >= 2.30.4
Requires:	sabayon >= 2.22

%description admin
Administration packages for GNOME Desktop Environment.

%description admin -l pl.UTF-8
Pakiety do zarządzania środowiskiem graficznym GNOME.

%package core
Summary:	The core components of the GNOME Desktop Environment
Summary(pl.UTF-8):	Podstawowe składniki środowiska graficznego GNOME
Group:		X11/Applications
Requires:	PackageKit-gtk3-module
Requires:	dconf >= 0.14.0
Requires:	eog >= 3.6.1
Requires:	gedit >= 3.6.1
Requires:	gnome-control-center >= 1:3.6.2
Requires:	gnome-desktop >= 3.6.1
Requires:	gnome-icon-theme >= 3.6.0
Requires:	gnome-icon-theme-symbolic >= 3.6.0
Requires:	gnome-keyring >= 3.6.1
Requires:	gnome-panel >= 3.6.0
Requires:	gnome-screensaver >= 3.6.1
Requires:	gnome-session >= 1:3.6.1
Requires:	gnome-settings-daemon >= 1:3.6.1
Requires:	gnome-shell >= 3.6.1
Requires:	gnome-terminal >= 3.6.1
Requires:	gnome-themes-standard >= 3.6.1
Requires:	gsettings-desktop-schemas >= 3.6.0
Requires:	gvfs >= 1.14.1
Requires:	mutter >= 3.6.1
Requires:	nautilus >= 3.6.2
Requires:	xdg-menus
Requires:	yelp >= 3.6.1
Suggests:	gnome-menus >= 3.6.0
# Default GNOME font
Suggests:	fonts-OTF-Cantarell

%description core
The core components of the GNOME Desktop Environment.

%description core -l pl.UTF-8
Podstawowe składniki środowiska graficznego GNOME.

%package desktop
Summary:	GNOME Desktop Environment
Summary(pl.UTF-8):	Środowisko graficzne GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	brasero >= 3.6.0
#Requires:	abrt-desktop >= 2.0.15
Requires:	cheese >= 3.6.1
Requires:	dconf-editor >= 0.14.0
Requires:	ekiga >= 3.9.90
Requires:	empathy >= 3.6.1
Requires:	eog-plugins >= 3.6.1
Requires:	epiphany >= 3.6.1
Requires:	epiphany-extensions >= 3.6.0
Requires:	evince >= 3.6.1
Requires:	evolution >= 3.6.1
Requires:	evolution-addressbook >= 3.6.1
Requires:	evolution-calendar >= 3.6.1
Requires:	evolution-mail >= 3.6.1
Requires:	file-roller >= 3.6.1.1
Requires:	gcalctool >= 6.6.1
Requires:	gconf-editor >= 3.0.1
Requires:	gdm >= 2:3.6.1
Requires:	gnome-backgrounds >= 3.6.1
Requires:	gnome-bluetooth >= 3.6.0
Requires:	gnome-color-manager >= 3.6.0
Requires:	gnome-disk-utility >= 3.6.1
Requires:	gnome-icon-theme-extras >= 3.4.0
Requires:	gnome-packagekit >= 3.6.0
Suggests:	%{name}-games = %{version}-%{release}
# not fully ported yet
#Requires:	gnome-media-sound-recorder >= 2.30.0
#Requires:	gnome-media-volume-control >= 2.30.0
#Requires:	gnome-netstatus >= 3.0.0
Requires:	gnome-nettool >= 3.0.1
Requires:	gnome-power-manager >= 3.6.0
Requires:	gnome-system-monitor >= 3.6.1
Requires:	gnome-system-tools >= 3.0.0
Requires:	gnome-tweak-tool >= 3.6.1
Requires:	gnome-user-docs >= 3.6.1
Requires:	gstreamer
Requires:	gstreamer-audio-effects-base
Requires:	gstreamer-audio-effects-good
Requires:	gstreamer-audio-formats
Requires:	gstreamer-audiosink-alsa
# not yet in gstreamer 1.x
#Requires:	gstreamer-cairo
Requires:	gstreamer-cdparanoia
Requires:	gstreamer-dv
Requires:	gstreamer-flac
Requires:	gstreamer-gdkpixbuf
Requires:	gstreamer-imagesink-x
Requires:	gstreamer-imagesink-xv
Requires:	gstreamer-jack
Requires:	gstreamer-libpng
Requires:	gstreamer-libvisual
Requires:	gstreamer-pango
Requires:	gstreamer-plugins-base
Requires:	gstreamer-plugins-good
Requires:	gstreamer-pulseaudio
Requires:	gstreamer-raw1394
Requires:	gstreamer-shout2
Requires:	gstreamer-soup
Requires:	gstreamer-speex
Requires:	gstreamer-taglib
Requires:	gstreamer-theora
Requires:	gstreamer-v4l2
Requires:	gstreamer-video-effects
Requires:	gstreamer-videosink-aa
Requires:	gstreamer-videosink-libcaca
Requires:	gstreamer-visualisation
Requires:	gstreamer-vorbis
Requires:	gstreamer-wavpack
Requires:	gstreamer-ximagesrc
Requires:	gucharmap >= 3.6.0
Requires:	nautilus-extension-brasero >= 3.6.0
Requires:	nautilus-extension-evince >= 3.6.1
# not fully ported yet
#Requires:	nautilus-extension-seahorse >= 2.30.1
Requires:	nautilus-sendto >= 3.6.0
Requires:	nautilus-sendto-cd-burner >= 3.6.0
Requires:	nautilus-sendto-empathy >= 3.6.1
Requires:	nautilus-sendto-evolution >= 3.6.0
Requires:	nautilus-sendto-gnome-bluetooth >= 3.6.0
Requires:	nautilus-sendto-upnp >= 3.6.0
Requires:	seahorse >= 3.6.2
# not fully ported yet
#Requires:	seahorse-plugins >= 2.30.1
Requires:	sound-juicer >= 3.4.0
Requires:	gnote >= 3.6.0
Requires:	totem >= 3.6.0
Requires:	totem-gromit >= 3.6.0
Requires:	totem-im-status >= 3.6.0
Requires:	totem-lirc >= 3.6.0
Requires:	totem-opensubtitles >= 3.6.0
Requires:	vinagre >= 3.6.1
Requires:	vino >= 3.6.1
Requires:	zenity >= 3.6.0
# gnome-menus is optional, so has to be alacarte
Suggests:	alacarte >= 0.13.2
Suggests:	browser-plugin-totem >= 3.6.0
Suggests:	evolution-ews >= 3.6.0
Suggests:	evolution-plugin-mail-notification >= 5.4
Suggests:	gnome-mail-notification >= 5.4
Suggests:	gstreamer-audiosink-oss
Suggests:	pam-pam_gnome_keyring >= 3.6.1

%description desktop
GNOME Desktop Environment.

%description desktop -l pl.UTF-8
Środowisko graficzne GNOME.

%package devtools
Summary:	Developer tools for GNOME Desktop Environment
Summary(pl.UTF-8):	Narzędzia programisty dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	accerciser >= 1.12.1
Requires:	anjuta >= 1:3.6.1
Requires:	anjuta-extras >= 3.4.0
Requires:	devhelp >= 3.6.0
Requires:	glade >= 3.14.1
Requires:	gnome-devel-docs >= 3.6.1

%description devtools
Developer tools for GNOME Desktop Environment.

%description devtools -l pl.UTF-8
Narzędzia programisty dla środowiska graficznego GNOME.

%package games
Summary:	Games for GNOME Desktop Environment
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	aisleriot
Requires:	gnome-games-glchess >= 1:3.6.1
Requires:	gnome-games-glines >= 1:3.6.1
Requires:	gnome-games-gnect >= 1:3.6.1
Requires:	gnome-games-gnibbles >= 1:3.6.1
Requires:	gnome-games-gnobots2 >= 1:3.6.1
Requires:	gnome-games-gnomine >= 1:3.6.1
Requires:	gnome-games-gnotravex >= 1:3.6.1
Requires:	gnome-games-gnotski >= 1:3.6.1
Requires:	gnome-games-gtali >= 1:3.6.1
Requires:	gnome-games-iagno >= 1:3.6.1
Requires:	gnome-games-lightsoff >= 1:3.6.1
Requires:	gnome-games-mahjongg >= 1:3.6.1
Requires:	gnome-games-quadrapassel >= 1:3.6.1
Requires:	gnome-games-sudoku >= 1:3.6.1
Requires:	gnome-games-swell-foop >= 1:3.6.1

%description games
Games for GNOME Desktop Environment.

%package office
Summary:	Office suite for GNOME Desktop Environment
Summary(pl.UTF-8):	Pakiety biurowe dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	abiword >= 1:2.8.6
Requires:	dia >= 1:0.97.2
Requires:	gimp >= 1:2.8.2
Requires:	glabels >= 3.0.1
Requires:	gnumeric >= 1:1.10.17
Requires:	inkscape >= 0.48.2
Requires:	planner >= 0.14.6

%description office
Office packages for GNOME Desktop Environment.

%description office -l pl.UTF-8
Pakiety biurowe dla środowiska graficznego GNOME.

%prep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files accessibility
%defattr(644,root,root,755)

%files admin
%defattr(644,root,root,755)

%files core
%defattr(644,root,root,755)

%files desktop
%defattr(644,root,root,755)

%files devtools
%defattr(644,root,root,755)

%files games
%defattr(644,root,root,755)

%files office
%defattr(644,root,root,755)
