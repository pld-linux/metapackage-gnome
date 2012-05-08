Summary:	GNOME Desktop Environment with additional packages
Summary(pl.UTF-8):	Środowisko graficzne GNOME z dodatkowymi pakietami
Name:		metapackage-gnome
Version:	3.2.2
Release:	5
License:	GPL/LGPL
Group:		X11/Applications
Requires:	%{name}-accessibility = %{version}-%{release}
Requires:	%{name}-admin = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-desktop = %{version}-%{release}
Requires:	%{name}-devtools = %{version}-%{release}
Requires:	%{name}-games = %{version}-%{release}
Requires:	%{name}-office = %{version}-%{release}
Requires:	banshee >= 2.0.1
#Requires:	epiphany-extension-gwget >= 1.0.1
Requires:	gnome-themes-extras-Darklooks >= 2.22.0
Requires:	gnome-themes-extras-Foxtrot >= 2.22.0
Requires:	gnome-themes-extras-Gion >= 2.22.0
Requires:	gnome-themes-extras-Neu >= 2.22.0
Requires:	gnome-themes-extras-Unity >= 2.22.0
Requires:	gnome-themes-extras-gnome-alternative >= 2.22.0
Requires:	gstreamer-a52dec
Requires:	gstreamer-aac
Requires:	gstreamer-amrnb
Requires:	gstreamer-amrwb
Requires:	gstreamer-ass
Requires:	gstreamer-audio-effects-bad
Requires:	gstreamer-audiosink-nas
Requires:	gstreamer-cdaudio
Requires:	gstreamer-cdio
Requires:	gstreamer-celt
Requires:	gstreamer-curl
Requires:	gstreamer-dc1394
Requires:	gstreamer-dirac
Requires:	gstreamer-dts
Requires:	gstreamer-dvdread
Requires:	gstreamer-flite
Requires:	gstreamer-gme
Requires:	gstreamer-gsettings
Requires:	gstreamer-gsm
Requires:	gstreamer-kate
Requires:	gstreamer-ladspa
Requires:	gstreamer-lame
Requires:	gstreamer-lv2
Requires:	gstreamer-mad
Requires:	gstreamer-mimic
Requires:	gstreamer-mjpegtools
Requires:	gstreamer-mms
Requires:	gstreamer-mpeg
Requires:	gstreamer-musepack
Requires:	gstreamer-musicbrainz
Requires:	gstreamer-mythtv
Requires:	gstreamer-neon
Requires:	gstreamer-ofa
Requires:	gstreamer-opencv
Requires:	gstreamer-plugins-bad
Requires:	gstreamer-plugins-ugly
Requires:	gstreamer-resindvd
Requires:	gstreamer-rtmp
Requires:	gstreamer-schroedinger
Requires:	gstreamer-sid
Requires:	gstreamer-sndfile
Requires:	gstreamer-soundtouch
Requires:	gstreamer-spc
Requires:	gstreamer-timidity
Requires:	gstreamer-videosink-directfb
Requires:	gstreamer-videosink-sdl
Requires:	gstreamer-vp8
Requires:	gstreamer-wildmidi
Requires:	gstreamer-x264
Requires:	gstreamer-xvid
Requires:	gstreamer-zbar
Requires:	gwget >= 1.0.1
Requires:	liferea >= 1.6.3
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
Requires:	at-spi2-atk >= 2.0.1
Requires:	at-spi2-core >= 2.0.1
Requires:	caribou >= 0.2.00
Requires:	dasher >= 4.11
Requires:	gnome-mag >= 0.16.1
Requires:	gnome-speech >= 0.4.23
Requires:	mousetweaks >= 3.2.1
Requires:	orca >= 3.2.2
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
Requires:	sabayon >= 2.30.1

%description admin
Administration packages for GNOME Desktop Environment.

%description admin -l pl.UTF-8
Pakiety do zarządzania środowiskiem graficznym GNOME.

%package core
Summary:	The core components of the GNOME Desktop Environment
Summary(pl.UTF-8):	Podstawowe składniki środowiska graficznego GNOME
Group:		X11/Applications
Requires:	PackageKit-gtk3-module
Requires:	dconf >= 0.7.5
Requires:	eog >= 3.2.2
Requires:	gedit >= 3.2.6
Requires:	gnome-control-center >= 1:3.2.2
Requires:	gnome-desktop >= 3.2.1
Requires:	gnome-icon-theme >= 3.2.1
Requires:	gnome-icon-theme-symbolic >= 3.2.2
Requires:	gnome-keyring >= 3.2.2
Requires:	gnome-panel >= 3.2.1
Requires:	gnome-screensaver >= 3.2.1
Requires:	gnome-session >= 1:3.2.1
Requires:	gnome-settings-daemon >= 1:3.2.2
Requires:	gnome-shell >= 3.2.2
Requires:	gnome-terminal >= 3.2.1
Requires:	gnome-themes-standard >= 3.2.1
Requires:	gsettings-desktop-schemas >= 3.2.0
Requires:	gvfs >= 1.8.1
Requires:	mutter >= 3.2.2
Requires:	nautilus >= 3.2.1
Requires:	xdg-menus
Requires:	yelp >= 3.2.1
Suggests:	gnome-menus >= 3.2.0
Suggests:	metacity >= 2:2.34.1
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
Requires:	brasero >= 3.2.0
Requires:	bug-buddy >= 2.32.0
Requires:	cheese >= 3.2.2
Requires:	dconf-editor >= 0.7.5
Requires:	ekiga >= 3.2.7
Requires:	empathy >= 3.2.2
Requires:	eog-plugins >= 3.2.2
Requires:	epiphany >= 3.2.1
Requires:	epiphany-extensions >= 3.2.0
Requires:	evince >= 3.2.1
Requires:	evolution >= 3.2.3
Requires:	evolution-addressbook >= 3.2.3
Requires:	evolution-calendar >= 3.2.3
Requires:	evolution-mail >= 3.2.3
Requires:	file-roller >= 3.2.2
Requires:	gcalctool >= 6.0.0
Requires:	gconf-editor >= 3.0.1
Requires:	gdm >= 2:3.2.1
Requires:	gedit-plugins >= 3.2.1
Requires:	gnome-backgrounds >= 3.2.0
Requires:	gnome-bluetooth >= 3.2.2
Requires:	gnome-color-manager >= 3.2.2
Requires:	gnome-disk-utility >= 3.0.2
Requires:	gnome-icon-theme-extras >= 3.0.0
Requires:	gnome-packagekit >= 3.2.1
Suggests:	%{name}-games = %{version}-%{release}
# not fully ported yet
#Requires:	gnome-media-sound-recorder >= 2.30.0
#Requires:	gnome-media-volume-control >= 2.30.0
#Requires:	gnome-netstatus >= 3.0.0
Requires:	gnome-nettool >= 3.0.1
Requires:	gnome-power-manager >= 3.2.1
Requires:	gnome-system-monitor >= 3.2.1
Requires:	gnome-system-tools >= 3.0.0
Requires:	gnome-tweak-tool
Requires:	gnome-user-docs >= 3.2.2
Requires:	gnome-utils-baobab >= 1:3.2.1
Requires:	gnome-utils-dictionary >= 1:3.2.1
Requires:	gnome-utils-font-viewer >= 1:3.2.1
Requires:	gnome-utils-logview >= 1:3.2.1
Requires:	gnome-utils-screenshot >= 1:3.2.1
Requires:	gnome-utils-search-tool >= 1:3.2.1
Requires:	grilo-plugins
Requires:	gstreamer
Requires:	gstreamer-GConf
Requires:	gstreamer-audio-effects-base
Requires:	gstreamer-audio-effects-good
Requires:	gstreamer-audio-formats
Requires:	gstreamer-audiosink-alsa
Requires:	gstreamer-audiosink-oss
Requires:	gstreamer-cairo
Requires:	gstreamer-cdparanoia
Requires:	gstreamer-dv
Requires:	gstreamer-flac
Requires:	gstreamer-gdkpixbuf
Requires:	gstreamer-gnomevfs
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
Requires:	gucharmap >= 3.2.2
Requires:	nautilus-extension-brasero >= 3.2.0
Requires:	nautilus-extension-evince >= 3.2.1
# not fully ported yet
#Requires:	nautilus-extension-seahorse >= 2.30.1
Requires:	nautilus-sendto >= 3.0.0
Requires:	nautilus-sendto-cd-burner >= 3.0.0
Requires:	nautilus-sendto-empathy >= 3.2.2
Requires:	nautilus-sendto-evolution >= 3.0.0
Requires:	nautilus-sendto-gnome-bluetooth >= 3.2.2
Requires:	nautilus-sendto-upnp >= 3.0.0
Requires:	seahorse >= 3.2.2
# not fully ported yet
#Requires:	seahorse-plugins >= 2.30.1
Requires:	sound-juicer >= 2.32.0
Requires:	tomboy >= 1.4.0
Requires:	totem >= 3.2.1
Requires:	totem-gromit >= 3.2.1
Requires:	totem-im-status >= 3.2.1
Requires:	totem-iplayer >= 3.2.1
Requires:	totem-lirc >= 3.2.1
Requires:	totem-opensubtitles >= 3.2.1
Requires:	totem-publish >= 3.2.1
Requires:	totem-youtube >= 3.2.1
Requires:	vinagre >= 3.2.2
Requires:	vino >= 3.2.2
Requires:	zenity >= 3.2.0
# alacarte is not fully ported yest
# gnome-menus is optional, so has to be alacarte
#Suggests:	alacarte >= 0.13.1
Suggests:	browser-plugin-totem >= 3.2.1
Suggests:	evolution-exchange >= 3.2.3
Suggests:	evolution-webcal >= 2.32.0
Suggests:	pam-pam_gnome_keyring >= 3.2.2
Suggests:	gnome-themes-Clearlooks >= 3.0.0
Suggests:	gnome-themes-ClearlooksClassic >= 3.0.0
Suggests:	gnome-themes-Crux >= 3.0.0
Suggests:	gnome-themes-Glider >= 3.0.0
Suggests:	gnome-themes-Glossy >= 3.0.0
Suggests:	gnome-themes-Inverted >= 3.0.0
Suggests:	gnome-themes-Mist >= 3.0.0

%description desktop
GNOME Desktop Environment.

%description desktop -l pl.UTF-8
Środowisko graficzne GNOME.

%package devtools
Summary:	Developer tools for GNOME Desktop Environment
Summary(pl.UTF-8):	Narzędzia programisty dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	accerciser >= 1.10.1
Requires:	anjuta >= 1:3.2.2
# not fully ported yet
#Requires:	anjuta-extras >= 2.30.1.0
Requires:	devhelp >= 3.2.0
Requires:	glade >= 3.10.0
Requires:	gnome-devel-docs >= 3.2.1

%description devtools
Developer tools for GNOME Desktop Environment.

%description devtools -l pl.UTF-8
Narzędzia programisty dla środowiska graficznego GNOME.

%package games
Summary:	Games for GNOME Desktop Environment
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	aisleriot
Requires:	gnome-games-extra-data-glines >= 3.2.0
Requires:	gnome-games-extra-data-gnobots2 >= 3.2.0
Requires:	gnome-games-extra-data-iagno >= 3.2.0
Requires:	gnome-games-extra-data-mahjongg >= 3.2.0
Requires:	gnome-games-glchess >= 1:3.2.1
Requires:	gnome-games-glines >= 1:3.2.1
Requires:	gnome-games-gnect >= 1:3.2.1
Requires:	gnome-games-gnibbles >= 1:3.2.1
Requires:	gnome-games-gnobots2 >= 1:3.2.1
Requires:	gnome-games-gnomine >= 1:3.2.1
Requires:	gnome-games-gnotravex >= 1:3.2.1
Requires:	gnome-games-gnotski >= 1:3.2.1
Requires:	gnome-games-gtali >= 1:3.2.1
Requires:	gnome-games-iagno >= 1:3.2.1
Requires:	gnome-games-lightsoff >= 1:3.2.1
Requires:	gnome-games-mahjongg >= 1:3.2.1
Requires:	gnome-games-quadrapassel >= 1:3.2.1
Requires:	gnome-games-sudoku >= 1:3.2.1
Requires:	gnome-games-swell-foop >= 1:3.2.1

%description games
Games for GNOME Desktop Environment.

%package office
Summary:	Office suite for GNOME Desktop Environment
Summary(pl.UTF-8):	Pakiety biurowe dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	abiword >= 1:2.4.6
Requires:	dia >= 1:0.96.1
Requires:	gimp >= 1:2.4.6
Requires:	glabels >= 2.2.8
Requires:	gnumeric >= 1:1.8.0
Requires:	inkscape >= 0.46
Requires:	planner >= 0.14.2

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
