Summary:	GNOME Desktop Environment with additional packages
Summary(pl.UTF-8):	Środowisko graficzne GNOME z dodatkowymi pakietami
Name:		metapackage-gnome
Version:	2.22.3
Release:	2
License:	GPL/LGPL
Group:		X11/Applications
Requires:	%{name}-accessibility = %{version}-%{release}
Requires:	%{name}-admin = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-desktop = %{version}-%{release}
Requires:	%{name}-devtools = %{version}-%{release}
Requires:	%{name}-office = %{version}-%{release}
Requires:	brasero >= 0.7.1
Requires:	epiphany-extension-gwget >= 0.99
Requires:	gnome-games-extra-data >= 2.22.0
Requires:	gnome-mount >= 0.8
Requires:	gnome-themes-extras-Darklooks >= 2.22.0
Requires:	gnome-themes-extras-Foxtrot >= 2.22.0
Requires:	gnome-themes-extras-Gion >= 2.22.0
Requires:	gnome-themes-extras-Neu >= 2.22.0
Requires:	gnome-themes-extras-Unity >= 2.22.0
Requires:	gnome-themes-extras-gnome-alternative >= 2.22.0
Requires:	gstreamer-a52dec
Requires:	gstreamer-aac
Requires:	gstreamer-audio-effects-bad
Requires:	gstreamer-audiosink-alsaspdif
Requires:	gstreamer-audiosink-nas
Requires:	gstreamer-cdaudio
Requires:	gstreamer-dts
Requires:	gstreamer-dvdread
Requires:	gstreamer-gsm
Requires:	gstreamer-jack
Requires:	gstreamer-ladspa
Requires:	gstreamer-lame
Requires:	gstreamer-mad
Requires:	gstreamer-mjpegtools
Requires:	gstreamer-mms
Requires:	gstreamer-mpeg
Requires:	gstreamer-musepack
Requires:	gstreamer-musicbrainz
Requires:	gstreamer-mythtv
Requires:	gstreamer-neon
Requires:	gstreamer-plugins-bad
Requires:	gstreamer-plugins-ugly
Requires:	gstreamer-sid
Requires:	gstreamer-sndfile
Requires:	gstreamer-soundtouch
Requires:	gstreamer-spc
Requires:	gstreamer-timidity
Requires:	gstreamer-videosink-directfb
Requires:	gstreamer-videosink-sdl
Requires:	gstreamer-wildmidi
Requires:	gstreamer-x264
Requires:	gstreamer-xvid
Requires:	gwget >= 0.99
Requires:	liferea >= 1.4.16
Requires:	rhythmbox >= 0.11.5
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
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	gnome-mag >= 0.15.0
Requires:	gnome-speech >= 0.4.19
Requires:	gok >= 1.3.7
Requires:	orca >= 2.22.2
Suggests:	gnome-themes-HighContrast >= 2.22.2
Suggests:	gnome-themes-HighContrast-SVG >= 2.22.2
Suggests:	gnome-themes-HighContrastInverse >= 2.22.2
Suggests:	gnome-themes-HighContrastLargePrint >= 2.22.2
Suggests:	gnome-themes-HighContrastLargePrintInverse >= 2.22.2
Suggests:	gnome-themes-LargePrint >= 2.22.2
Suggests:	gnome-themes-LowContrast >= 2.22.2
Suggests:	gnome-themes-LowContrastLargePrint >= 2.22.2
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
Requires:	pessulus >= 2.16.4
Requires:	sabayon >= 2.22.0

%description admin
Administration packages for GNOME Desktop Environment.

%description admin -l pl.UTF-8
Pakiety do zarządzania środowiskiem graficznym GNOME.

%package core
Summary:	The core components of the GNOME Desktop Environment
Summary(pl.UTF-8):	Podstawowe składniki środowiska graficznego GNOME
Group:		X11/Applications
Requires:	eog >= 2.22.3
Requires:	fam
Requires:	gedit2 >= 2.22.3
Requires:	gnome-control-center >= 1:2.22.2.1
Requires:	gnome-desktop >= 2.22.3
Requires:	gnome-icon-theme >= 2.22.0
Requires:	gnome-panel >= 2.22.2
Requires:	gnome-session >= 2.22.3
Requires:	gnome-terminal >= 2.22.3
Requires:	gtk2-engines >= 1:2.14.3
Requires:	nautilus >= 2.22.4
Requires:	xdg-menus
Requires:	yelp >= 2.22.1
Suggests:	gnome-menus >= 2.22.2
Suggests:	metacity >= 2:2.22.0

%description core
The core components of the GNOME Desktop Environment.

%description core -l pl.UTF-8
Podstawowe składniki środowiska graficznego GNOME.

%package desktop
Summary:	GNOME Desktop Environment
Summary(pl.UTF-8):	Środowisko graficzne GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	alacarte >= 0.11.5
Requires:	bug-buddy >= 2.22.0
Requires:	cheese >= 2.22.3
Requires:	dasher >= 4.6.1
Requires:	ekiga >= 2.0.11
Requires:	epiphany >= 2.22.2
Requires:	epiphany-extensions >= 2.22.2
Requires:	evince >= 2.22.2
Requires:	evolution >= 2.22.3.1
Requires:	evolution-addressbook >= 2.22.3.1
Requires:	evolution-calendar >= 2.22.3.1
Requires:	evolution-mail >= 2.22.3.1
Requires:	evolution-pilot >= 2.22.3.1
Requires:	file-roller >= 2.22.4
Requires:	gcalctool >= 2.22.3
Requires:	gconf-editor >= 2.22.0
Requires:	gdm >= 1:2.20.7
Requires:	gedit-plugins >= 2.22.2
Requires:	gnome-applet-deskbar >= 2.22.3
Requires:	gnome-applet-fast-user-switch >= 2.22.0
Requires:	gnome-applets-accessx-status >= 1:2.22.3
Requires:	gnome-applets-battstat >= 1:2.22.3
Requires:	gnome-applets-charpicker >= 1:2.22.3
Requires:	gnome-applets-cpufreq >= 1:2.22.3
Requires:	gnome-applets-drivemount >= 1:2.22.3
Requires:	gnome-applets-geyes >= 1:2.22.3
Requires:	gnome-applets-gweather >= 1:2.22.3
Requires:	gnome-applets-invest >= 1:2.22.3
Requires:	gnome-applets-keyboard >= 1:2.22.3
Requires:	gnome-applets-minicommander >= 1:2.22.3
Requires:	gnome-applets-mixer >= 1:2.22.3
Requires:	gnome-applets-modemlights >= 1:2.22.3
Requires:	gnome-applets-multiload >= 1:2.22.3
Requires:	gnome-applets-stickynotes >= 1:2.22.3
Requires:	gnome-applets-trash >= 1:2.22.3
Requires:	gnome-backgrounds >= 2.22.0
Requires:	gnome-games-blackjack >= 1:2.22.3
Requires:	gnome-games-glchess >= 1:2.22.3
Requires:	gnome-games-glines >= 1:2.22.3
Requires:	gnome-games-gnect >= 1:2.22.3
Requires:	gnome-games-gnibbles >= 1:2.22.3
Requires:	gnome-games-gnobots2 >= 1:2.22.3
Requires:	gnome-games-gnometris >= 1:2.22.3
Requires:	gnome-games-gnomine >= 1:2.22.3
Requires:	gnome-games-gnotravex >= 1:2.22.3
Requires:	gnome-games-gnotski >= 1:2.22.3
Requires:	gnome-games-gtali >= 1:2.22.3
Requires:	gnome-games-iagno >= 1:2.22.3
Requires:	gnome-games-mahjongg >= 1:2.22.3
Requires:	gnome-games-same-gnome >= 1:2.22.3
Requires:	gnome-games-sol >= 1:2.22.3
Requires:	gnome-games-sudoku >= 1:2.22.3
Requires:	gnome-keyring >= 2.22.3
Requires:	gnome-media-cd >= 2.22.0
Requires:	gnome-media-cddb >= 2.22.0
Requires:	gnome-media-sound-recorder >= 2.22.0
Requires:	gnome-media-volume-control >= 2.22.0
Requires:	gnome-media-vumeter >= 2.22.0
Requires:	gnome-netstatus >= 2.12.1
Requires:	gnome-nettool >= 2.22.0
Requires:	gnome-power-manager >= 2.22.1
Requires:	gnome-screensaver >= 2.22.2
Requires:	gnome-system-monitor >= 2.22.3
Requires:	gnome-system-tools >= 2.22.0
Requires:	gnome-user-docs >= 2.22.1
Requires:	gnome-utils-baobab >= 1:2.20.0.1
Requires:	gnome-utils-dictionary >= 1:2.20.0.1
Requires:	gnome-utils-floppy >= 1:2.20.0.1
Requires:	gnome-utils-logview >= 1:2.20.0.1
Requires:	gnome-utils-screenshot >= 1:2.20.0.1
Requires:	gnome-utils-search-tool >= 1:2.20.0.1
Requires:	gnome-volume-manager >= 2.22.5
Requires:	gstreamer
Requires:	gstreamer-GConf
Requires:	gstreamer-audio-effects-base
Requires:	gstreamer-audio-effects-good
Requires:	gstreamer-audio-formats
Requires:	gstreamer-audiosink-alsa
Requires:	gstreamer-audiosink-esd
Requires:	gstreamer-audiosink-oss
Requires:	gstreamer-cairo
Requires:	gstreamer-cdio
Requires:	gstreamer-cdparanoia
Requires:	gstreamer-dv
Requires:	gstreamer-flac
Requires:	gstreamer-gdkpixbuf
Requires:	gstreamer-gnomevfs
Requires:	gstreamer-hal
Requires:	gstreamer-imagesink-x
Requires:	gstreamer-imagesink-xv
Requires:	gstreamer-libpng
Requires:	gstreamer-libvisual
Requires:	gstreamer-pango
Requires:	gstreamer-plugins-base
Requires:	gstreamer-plugins-good
Requires:	gstreamer-raw1394
Requires:	gstreamer-shout2
Requires:	gstreamer-speex
Requires:	gstreamer-taglib
Requires:	gstreamer-theora
Requires:	gstreamer-video-effects
Requires:	gstreamer-videosink-aa
Requires:	gstreamer-videosink-libcaca
Requires:	gstreamer-visualisation
Requires:	gstreamer-vorbis
Requires:	gstreamer-wavpack
Requires:	gstreamer-ximagesrc
Requires:	gucharmap >= 2.22.3
Requires:	nautilus-cd-burner >= 2.22.1
Requires:	nautilus-extension-evince >= 2.22.2
Requires:	seahorse >= 2.22.3
Requires:	sound-juicer >= 2.22.0
Requires:	tomboy >= 0.10.2
Requires:	totem >= 2.22.2
Requires:	vinagre >= 0.5.0
Requires:	vino >= 2.22.2
Requires:	zenity >= 2.22.1
Suggests:	evolution-exchange >= 2.22.3
Suggests:	evolution-webcal
Suggests:	gnome-games-servers >= 1:2.22.3
Suggests:	gnome-keyring-pam >= 2.22.3
Suggests:	gnome-themes-Clearlooks >= 2.22.2
Suggests:	gnome-themes-ClearlooksClassic >= 2.22.2
Suggests:	gnome-themes-Crux >= 2.22.2
Suggests:	gnome-themes-Glider >= 2.22.2
Suggests:	gnome-themes-Glossy >= 2.22.2
Suggests:	gnome-themes-Inverted >= 2.22.2
Suggests:	gnome-themes-Mist >= 2.22.2

%description desktop
GNOME Desktop Environment.

%description desktop -l pl.UTF-8
Środowisko graficzne GNOME.

%package devtools
Summary:	Developer tools for GNOME Desktop Environment
Summary(pl.UTF-8):	Narzędzia programisty dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	accerciser >= 1.2.0
Requires:	anjuta >= 1:2.4.2
Requires:	devhelp >= 0.19.1
Requires:	glade3 >= 3.4.5
Requires:	gnome-devel-docs >= 2.22.0

%description devtools
Developer tools for GNOME Desktop Environment.

%description devtools -l pl.UTF-8
Narzędzia programisty dla środowiska graficznego GNOME.

%package office
Summary:	Office suite for GNOME Desktop Environment
Summary(pl.UTF-8):	Pakiety biurowe dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	abiword >= 1:2.4.6
Requires:	dia >= 1:0.96.1
Requires:	gimp >= 1:2.4.6
Requires:	glabels >= 2.2.1
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

%files office
%defattr(644,root,root,755)
