Summary:	GNOME Desktop Environment with additional packages
Summary(pl.UTF-8):	Środowisko graficzne GNOME z dodatkowymi pakietami
Name:		metapackage-gnome
Version:	2.22.1
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
Requires:	liferea >= 1.4.15
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
Requires:	gnome-mag >= 0.14.10
Requires:	gnome-speech >= 0.4.18
Requires:	gok >= 1.3.6
Requires:	orca >= 2.22.1
Suggests:	gnome-themes-HighContrast >= 2.22.0
Suggests:	gnome-themes-HighContrast-SVG >= 2.22.0
Suggests:	gnome-themes-HighContrastInverse >= 2.22.0
Suggests:	gnome-themes-HighContrastLargePrint >= 2.22.0
Suggests:	gnome-themes-HighContrastLargePrintInverse >= 2.22.0
Suggests:	gnome-themes-LargePrint >= 2.22.0
Suggests:	gnome-themes-LowContrast >= 2.22.0
Suggests:	gnome-themes-LowContrastLargePrint >= 2.22.0
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
Requires:	eog >= 2.22.1
Requires:	fam
Requires:	gedit2 >= 2.22.1
Requires:	gnome-control-center >= 2.22.1
Requires:	gnome-desktop >= 2.22.1
Requires:	gnome-icon-theme >= 2.22.0
Requires:	gnome-menus >= 2.22.1
Requires:	gnome-panel >= 2.22.1.3
Requires:	gnome-session >= 2.22.1
Requires:	gnome-terminal >= 2.22.1
Requires:	gtk2-engines >= 2.14.1
Requires:	nautilus >= 2.22.2
Requires:	yelp >= 2.22.1
Suggests:	metacity >= 2.22.0

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
Requires:	cheese >= 2.22.0
Requires:	dasher >= 4.6.1
Requires:	ekiga >= 2.0.11
Requires:	epiphany >= 2.22.0
Requires:	epiphany-extensions >= 2.22.0
Requires:	evince >= 2.22.0
Requires:	evolution >= 2.22.0
Requires:	evolution-addressbook >= 2.22.0
Requires:	evolution-calendar >= 2.22.0
Requires:	evolution-mail >= 2.22.0
Requires:	evolution-pilot >= 2.22.0
Requires:	file-roller >= 2.22.0
Requires:	gcalctool >= 2.22.0
Requires:	gconf-editor >= 2.22.0
Requires:	gdm >= 1:2.20.0
Requires:	gedit-plugins >= 2.22.1
Requires:	gnome-applet-deskbar >= 2.22.0
Requires:	gnome-applet-fast-user-switch >= 2.22.0
Requires:	gnome-applets-accessx-status >= 2.22.1
Requires:	gnome-applets-battstat >= 2.22.1
Requires:	gnome-applets-charpicker >= 2.22.1
Requires:	gnome-applets-cpufreq >= 2.22.1
Requires:	gnome-applets-drivemount >= 2.22.1
Requires:	gnome-applets-geyes >= 2.22.1
Requires:	gnome-applets-gweather >= 2.22.1
Requires:	gnome-applets-invest >= 2.22.1
Requires:	gnome-applets-keyboard >= 2.22.1
Requires:	gnome-applets-minicommander >= 2.22.1
Requires:	gnome-applets-mixer >= 2.22.1
Requires:	gnome-applets-modemlights >= 2.22.1
Requires:	gnome-applets-multiload >= 2.22.1
Requires:	gnome-applets-stickynotes >= 2.22.1
Requires:	gnome-applets-trash >= 2.22.1
Requires:	gnome-backgrounds >= 2.22.0
Requires:	gnome-games-blackjack >= 2.22.1.1
Requires:	gnome-games-glchess >= 2.22.1.1
Requires:	gnome-games-glines >= 2.22.1.1
Requires:	gnome-games-gnect >= 2.22.1.1
Requires:	gnome-games-gnibbles >= 2.22.1.1
Requires:	gnome-games-gnobots2 >= 2.22.1.1
Requires:	gnome-games-gnometris >= 2.22.1.1
Requires:	gnome-games-gnomine >= 2.22.1.1
Requires:	gnome-games-gnotravex >= 2.22.1.1
Requires:	gnome-games-gnotski >= 2.22.1.1
Requires:	gnome-games-gtali >= 2.22.1.1
Requires:	gnome-games-iagno >= 2.22.1.1
Requires:	gnome-games-mahjongg >= 2.22.1.1
Requires:	gnome-games-same-gnome >= 2.22.1.1
Requires:	gnome-games-sol >= 2.22.1.1
Requires:	gnome-games-sudoku >= 2.22.1.1
Requires:	gnome-keyring >= 2.22.0
Requires:	gnome-media-cd >= 2.22.0
Requires:	gnome-media-cddb >= 2.22.0
Requires:	gnome-media-sound-recorder >= 2.22.0
Requires:	gnome-media-volume-control >= 2.22.0
Requires:	gnome-media-vumeter >= 2.22.0
Requires:	gnome-netstatus >= 2.12.0
Requires:	gnome-nettool >= 2.22.0
Requires:	gnome-power-manager >= 2.22.0
Requires:	gnome-screensaver >= 2.22.0
Requires:	gnome-system-monitor >= 2.22.0
Requires:	gnome-system-tools >= 2.22.0
Requires:	gnome-user-docs >= 2.22.0
Requires:	gnome-utils-baobab >= 2.22.1
Requires:	gnome-utils-dictionary >= 2.22.1
Requires:	gnome-utils-floppy >= 2.22.1
Requires:	gnome-utils-logview >= 2.22.1
Requires:	gnome-utils-screenshot >= 2.22.1
Requires:	gnome-utils-search-tool >= 2.22.1
Requires:	gnome-volume-manager >= 2.22.0
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
Requires:	gucharmap >= 2.22.0
Requires:	nautilus-cd-burner >= 2.22.0
Requires:	nautilus-extension-evince >= 2.22.0
Requires:	seahorse >= 2.22.0
Requires:	sound-juicer >= 2.22.0
Requires:	tomboy >= 0.8.0
Requires:	totem >= 2.22.0
Requires:	vinagre >= 0.5.0
Requires:	vino >= 2.22.0
Requires:	zenity >= 2.22.0
Suggests:	evolution-exchange >= 2.22.0
Suggests:	evolution-webcal
Suggests:	gnome-games-servers >= 2.22.1.1
Suggests:	gnome-keyring-pam >= 2.22.0
Suggests:	gnome-themes-Clearlooks >= 2.22.0
Suggests:	gnome-themes-ClearlooksClassic >= 2.22.0
Suggests:	gnome-themes-Crux >= 2.22.0
Suggests:	gnome-themes-Glider >= 2.22.0
Suggests:	gnome-themes-Glossy >= 2.22.0
Suggests:	gnome-themes-Inverted >= 2.22.0
Suggests:	gnome-themes-Mist >= 2.22.0

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
Requires:	anjuta >= 2.4.0
Requires:	devhelp >= 0.19
Requires:	glade3 >= 3.4.3
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
Requires:	gimp >= 2.4.5
Requires:	glabels >= 2.1.3
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
