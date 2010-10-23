Summary:	GNOME Desktop Environment with additional packages
Summary(pl.UTF-8):	Środowisko graficzne GNOME z dodatkowymi pakietami
Name:		metapackage-gnome
Version:	2.32.0
Release:	1
License:	GPL/LGPL
Group:		X11/Applications
Requires:	%{name}-accessibility = %{version}-%{release}
Requires:	%{name}-admin = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-desktop = %{version}-%{release}
Requires:	%{name}-devtools = %{version}-%{release}
Requires:	%{name}-office = %{version}-%{release}
Requires:	epiphany-extension-gwget >= 1.0.1
Requires:	gnome-color-manager >= 2.30.1
Requires:	gnome-games-extra-data-glines >= 2.30.0
Requires:	gnome-games-extra-data-gnobots2 >= 2.30.0
Requires:	gnome-games-extra-data-iagno >= 2.30.0
Requires:	gnome-games-extra-data-mahjongg >= 2.30.0
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
Requires:	gwget >= 1.0.1
Requires:	liferea >= 1.6.3
Requires:	rhythmbox >= 0.12.8
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
Requires:	dasher >= 4.11
Requires:	gnome-applet-colorblind >= 0.16.1
Requires:	gnome-mag >= 0.16.1
Requires:	gnome-speech >= 0.4.23
Requires:	gok >= 2.30.0
Requires:	mousetweaks >= 2.30.1
Requires:	orca >= 2.30.1
Suggests:	gnome-themes-HighContrast >= 2.30.1
Suggests:	gnome-themes-HighContrast-SVG >= 2.30.1
Suggests:	gnome-themes-HighContrastInverse >= 2.30.1
Suggests:	gnome-themes-HighContrastLargePrint >= 2.30.1
Suggests:	gnome-themes-HighContrastLargePrintInverse >= 2.30.1
Suggests:	gnome-themes-LargePrint >= 2.30.1
Suggests:	gnome-themes-LowContrast >= 2.30.1
Suggests:	gnome-themes-LowContrastLargePrint >= 2.30.1
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
Requires:	pessulus >= 2.30.0
Requires:	sabayon >= 2.22.1

%description admin
Administration packages for GNOME Desktop Environment.

%description admin -l pl.UTF-8
Pakiety do zarządzania środowiskiem graficznym GNOME.

%package core
Summary:	The core components of the GNOME Desktop Environment
Summary(pl.UTF-8):	Podstawowe składniki środowiska graficznego GNOME
Group:		X11/Applications
Requires:	eog >= 2.32.0
Requires:	fam
Requires:	gedit2 >= 2.30.4
Requires:	gnome-control-center >= 1:2.32.0
Requires:	gnome-desktop >= 2.32.0
Requires:	gnome-icon-theme >= 2.30.2
Requires:	gnome-keyring >= 2.32.0
Requires:	gnome-packagekit >= 2.32.0
Requires:	gnome-panel >= 2.32.0
Requires:	gnome-session >= 1:2.32.0
Requires:	gnome-settings-daemon >= 2.32.0
Requires:	gnome-terminal >= 2.32.0
Requires:	gtk2-engines >= 1:2.20.0
Requires:	nautilus >= 2.32.0
Requires:	xdg-menus
Requires:	yelp >= 2.30.2
Suggests:	gnome-menus >= 2.30.4
Suggests:	metacity >= 2:2.30.1
# Just suggest some TTF font
Suggests:	fonts-TTF-RedHat-liberation

%description core
The core components of the GNOME Desktop Environment.

%description core -l pl.UTF-8
Podstawowe składniki środowiska graficznego GNOME.

%package desktop
Summary:	GNOME Desktop Environment
Summary(pl.UTF-8):	Środowisko graficzne GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	brasero >= 2.32.0
Requires:	bug-buddy >= 2.32.0
Requires:	cheese >= 2.32.0
Requires:	ekiga >= 2.0.11
Requires:	empathy >= 2.32.0
Requires:	eog-plugins >= 2.30.0
Requires:	epiphany >= 2.30.2
Requires:	epiphany-extensions >= 2.30.0
Requires:	evince >= 2.32.0
Requires:	evolution >= 2.32.0
Requires:	evolution-addressbook >= 2.32.0
Requires:	evolution-calendar >= 2.32.0
Requires:	evolution-mail >= 2.32.0
Requires:	file-roller >= 2.32.0
Requires:	gcalctool >= 5.32.0
Requires:	gconf-editor >= 2.30.0
Requires:	gdm >= 2:2.32.0
Requires:	gdm-user-switch-applet >= 2:2.32.0
Requires:	gedit-plugin-seahorse >= 2.30.1
Requires:	gedit-plugins >= 2.30.0
Requires:	gnome-applet-deskbar >= 2.30.0
Requires:	gnome-applet-hamster >= 2.30.1
Requires:	gnome-applet-seahorse >= 2.30.1
Requires:	gnome-applets-accessx-status >= 1:2.32.0
Requires:	gnome-applets-battstat >= 1:2.32.0
Requires:	gnome-applets-charpicker >= 1:2.32.0
Requires:	gnome-applets-cpufreq >= 1:2.32.0
Requires:	gnome-applets-drivemount >= 1:2.32.0
Requires:	gnome-applets-geyes >= 1:2.32.0
Requires:	gnome-applets-gweather >= 1:2.32.0
Requires:	gnome-applets-invest >= 1:2.32.0
Requires:	gnome-applets-minicommander >= 1:2.32.0
Requires:	gnome-applets-mixer >= 1:2.32.0
Requires:	gnome-applets-multiload >= 1:2.32.0
Requires:	gnome-applets-stickynotes >= 1:2.32.0
Requires:	gnome-applets-trash >= 1:2.32.0
Requires:	gnome-backgrounds >= 2.32.0
Requires:	gnome-bluetooth >= 2.32.0
Requires:	gnome-disk-utility >= 2.32.0
Requires:	gnome-games-glchess >= 1:2.32.0
Requires:	gnome-games-glines >= 1:2.32.0
Requires:	gnome-games-gnect >= 1:2.32.0
Requires:	gnome-games-gnibbles >= 1:2.32.0
Requires:	gnome-games-gnobots2 >= 1:2.32.0
Requires:	gnome-games-gnomine >= 1:2.32.0
Requires:	gnome-games-gnotravex >= 1:2.32.0
Requires:	gnome-games-gnotski >= 1:2.32.0
Requires:	gnome-games-gtali >= 1:2.32.0
Requires:	gnome-games-iagno >= 1:2.32.0
Requires:	gnome-games-lightsoff >= 1:2.32.0
Requires:	gnome-games-mahjongg >= 1:2.32.0
Requires:	gnome-games-quadrapassel >= 1:2.32.0
Requires:	gnome-games-sol >= 1:2.32.0
Requires:	gnome-games-sudoku >= 1:2.32.0
Requires:	gnome-games-swell-foop >= 1:2.32.0
Requires:	gnome-icon-theme-extras >= 2.30.1
Requires:	gnome-media-sound-recorder >= 2.30.0
Requires:	gnome-media-volume-control >= 2.30.0
Requires:	gnome-netstatus >= 2.26.0
Requires:	gnome-nettool >= 2.30.0
Requires:	gnome-power-manager >= 2.32.0
Requires:	gnome-screensaver >= 2.30.0
Requires:	gnome-system-monitor >= 2.28.0
Requires:	gnome-system-tools >= 2.30.1
Requires:	gnome-user-docs >= 2.30.1
Requires:	gnome-utils-baobab >= 1:2.30.0
Requires:	gnome-utils-dictionary >= 1:2.30.0
Requires:	gnome-utils-logview >= 1:2.30.0
Requires:	gnome-utils-screenshot >= 1:2.30.0
Requires:	gnome-utils-search-tool >= 1:2.30.0
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
Requires:	gstreamer-hal
Requires:	gstreamer-imagesink-x
Requires:	gstreamer-imagesink-xv
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
Requires:	gstreamer-video-effects
Requires:	gstreamer-videosink-aa
Requires:	gstreamer-videosink-libcaca
Requires:	gstreamer-visualisation
Requires:	gstreamer-vorbis
Requires:	gstreamer-wavpack
Requires:	gstreamer-ximagesrc
Requires:	gucharmap >= 2.32.0
Requires:	nautilus-extension-brasero >= 2.32.0
Requires:	nautilus-extension-evince >= 2.32.0
Requires:	nautilus-extension-seahorse >= 2.30.1
Requires:	nautilus-sendto >= 2.32.0
Requires:	nautilus-sendto-cd-burner >= 2.32.0
Requires:	nautilus-sendto-empathy >= 2.30.0
Requires:	nautilus-sendto-evolution >= 2.32.0
Requires:	nautilus-sendto-gnome-bluetooth >= 2.32.0
Requires:	nautilus-sendto-upnp >= 2.32.0
Requires:	seahorse >= 2.30.1
Requires:	seahorse-plugins >= 2.30.1
Requires:	sound-juicer >= 2.28.2
Requires:	swfdec-gnome >= 2.30.0
Requires:	tomboy >= 1.4.0
Requires:	totem >= 2.32.0
Requires:	vinagre >= 2.30.3
Requires:	vino >= 2.32.0
Requires:	zenity >= 2.32.0
# gnome-menus is optional, so has to be alacarte
Suggests:	alacarte >= 0.13.1
Suggests:	browser-plugin-totem >= 2.30.2
Suggests:	evolution-exchange >= 2.32.0
Suggests:	evolution-webcal >= 2.32.0
Suggests:	gnome-keyring-pam >= 2.30.1
Suggests:	gnome-themes-Clearlooks >= 2.32.0
Suggests:	gnome-themes-ClearlooksClassic >= 2.32.0
Suggests:	gnome-themes-Crux >= 2.32.0
Suggests:	gnome-themes-Glider >= 2.32.0
Suggests:	gnome-themes-Glossy >= 2.32.0
Suggests:	gnome-themes-Inverted >= 2.32.0
Suggests:	gnome-themes-Mist >= 2.32.0

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
Requires:	anjuta >= 1:2.30.1.0
Requires:	anjuta-extras >= 2.30.1.0
Requires:	devhelp >= 2.30.0
Requires:	glade3 >= 3.6.7
Requires:	gnome-devel-docs >= 2.30.1

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

%files office
%defattr(644,root,root,755)
