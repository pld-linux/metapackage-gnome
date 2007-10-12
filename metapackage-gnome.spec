#
# TODO:
# - metapackage with development tools (glade, bluefish, anjuta, etc.)
# - metapackage 3rd party (everything else ;)
# - maybe group like here: http://ftp.gnome.org/pub/GNOME/teams/releng/2.18.0/versions ?
#
Summary:	GNOME Desktop Suite
Summary(pl.UTF-8):	Środowisko graficzne GNOME
Name:		metapackage-gnome
Version:	2.20.0
Release:	1
License:	GPL/LGPL
Group:		X11/Applications
Requires:	alacarte >= 0.11.3
Requires:	bug-buddy >= 2.20.0
Requires:	cdrtools
Requires:	cdrtools-mkisofs
Requires:	cdrtools-readcd
Requires:	eog >= 2.20.0
Requires:	epiphany >= 2.20.0
Requires:	epiphany-extension-gwget >= 0.99
Requires:	epiphany-extensions >= 2.20.0
Requires:	evince >= 2.20.0
Requires:	eel >= 2.20.0
Requires:	evolution >= 2.12.0
Requires:	evolution-addressbook >= 2.12.0
Requires:	evolution-mail >= 2.12.0
Requires:	file-roller >= 2.20.0
Requires:	gcalctool >= 5.20.1
Requires:	gconf-editor >= 2.20.0
Requires:	gedit2 >= 2.20.0
Requires:	gnome-applet-deskbar >= 2.20.0
Requires:	gnome-applets-accessx-status >= 1:2.20.0
Requires:	gnome-applets-battstat >= 1:2.20.0
Requires:	gnome-applets-charpicker >= 1:2.20.0
Requires:	gnome-applets-cpufreq >= 1:2.20.0
Requires:	gnome-applets-drivemount >= 1:2.20.0
Requires:	gnome-applets-geyes >= 1:2.20.0
Requires:	gnome-applets-gweather >= 1:2.20.0
Requires:	gnome-applets-invest >= 1:2.20.0
Requires:	gnome-applets-keyboard >= 1:2.20.0
Requires:	gnome-applets-minicommander >= 1:2.20.0
Requires:	gnome-applets-mixer >= 1:2.20.0
Requires:	gnome-applets-modemlights >= 1:2.20.0
Requires:	gnome-applets-multiload >= 1:2.20.0
Requires:	gnome-applets-stickynotes >= 1:2.20.0
Requires:	gnome-applets-trash >= 1:2.20.0
Requires:	gnome-backgrounds >= 2.20.0
Requires:	gnome-common >= 2.20.0
Requires:	gnome-commander >= 1.2.4
Requires:	gnome-control-center >= 2.20.0
Requires:	gnome-desktop >= 2.20.0
Requires:	gnome-icon-theme >= 2.20.0
Requires:	gnome-keyring >= 2.20.0
Requires:	gnome-keyring-manager >= 2.20.0
#Requires:	gnome-mail-notification >= 4.1
Requires:	gnome-media-cd >= 2.20.1
Requires:	gnome-media-cddb >= 2.20.1
Requires:	gnome-media-sound-recorder >= 2.20.1
Requires:	gnome-media-volume-control >= 2.20.1
Requires:	gnome-media-vumeter >= 2.20.1
Requires:	gnome-menus >= 2.20.0
Requires:	gnome-netstatus >= 2.12.1
Requires:	gnome-nettool >= 2.20.0
Requires:	gnome-panel >= 2.20.0.1
Requires:	gnome-power-manager >= 2.20.0
Requires:	gnome-screensaver >= 2.20.0
Requires:	gnome-session >= 2.20.0
Requires:	gnome-system-monitor >= 2.20.0
Requires:	gnome-system-tools >= 2.20.0
Requires:	gnome-terminal >= 2.18.0
Requires:	gnome-themes-Clearlooks >= 2.20.0
Requires:	gnome-themes-ClearlooksClassic >= 2.20.0
Requires:	gnome-utils >= 1:2.20.0
Requires:	gnome-utils-baobab >= 1:2.20.0
Requires:	gnome-utils-dictionary >= 1:2.20.0
Requires:	gnome-utils-floppy >= 1:2.20.0
Requires:	gnome-utils-logview >= 1:2.20.0
Requires:	gnome-utils-screenshot >= 1:2.20.0
Requires:	gnome-utils-search-tool >= 1:2.20.0
Requires:	gnome-volume-manager >= 2.17.0
Requires:	gstreamer >= 0.10.14
Requires:	gstreamer-GConf >= 0.10.6
Requires:	gstreamer-audio-effects-base >= 0.10.14
Requires:	gstreamer-audio-effects-good >= 0.10.6
Requires:	gstreamer-audio-formats >= 0.10.6
Requires:	gstreamer-audiosink-alsa >= 0.10.14
Requires:	gstreamer-audiosink-alsaspdif >= 0.10.5
Requires:	gstreamer-audiosink-esd >= 0.10.6
Requires:	gstreamer-audiosink-oss >= 0.10.6
Requires:	gstreamer-cdparanoia >= 0.10.14
Requires:	gstreamer-ffmpeg >= 0.10.2
Requires:	gstreamer-hal >= 0.10.6
Requires:	gstreamer-gnomevfs >= 0.10.14
Requires:	gstreamer-imagesink-x >= 0.10.14
Requires:	gstreamer-imagesink-xv >= 0.10.14
Requires:	gstreamer-libvisual >= 0.10.14
Requires:	gstreamer-mad >= 0.10.6
Requires:	gstreamer-neon >= 0.10.5
Requires:	gstreamer-pango >= 0.10.14
Requires:	gstreamer-plugins-base >= 0.10.14
Requires:	gstreamer-plugins-good >= 0.10.6
Requires:	gstreamer-theora >= 0.10.14
Requires:	gstreamer-vorbis >= 0.10.14
Requires:	gstreamer-x264 >= 0.10.5
Requires:	gstreamer-xvid >= 0.10.5
Requires:	gucharmap >= 1.10.0
Requires:	gwget >= 0.99
Requires:	icon-naming-utils >= 0.8.6
Requires:	metacity >= 2.20.0
Requires:	nautilus >= 2.20.0
Requires:	nautilus-cd-burner >= 2.20.0
Requires:	nautilus-extension-evince
Requires:	nautilus-sendto >= 0.10
Requires:	nautilus-sendto-evolution
Requires:	rarian >= 0.6.0
Requires:	seahorse >= 2.20
Requires:	sound-juicer >= 2.20.0
Requires:	system-tools-backends >= 2.4.0
Requires:	startup-notification >= 0.9
Requires:	tomboy >= 0.8.0
Requires:	totem >= 2.20.0
Requires:	vino >= 2.20.0
Requires:	yelp >= 2.20.0
Requires:	zenity >= 2.20.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Desktop suite metapackage.

%description -l pl.UTF-8
Metapakiet środowiska graficznego GNOME.

%package extras
Summary:	Metapackage to install additional packages for GNOME Desktop
Summary(pl.UTF-8):	Metapakiet instalujący dodatkowe pakiety dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	dasher >= 4.6.0
Requires:	ekiga >= 2.0.11
Requires:	evolution-calendar >= 2.12.0
Requires:	evolution-exchange >= 2.12.0
Requires:	evolution-pilot >= 2.12.0
Requires:	evolution-rss >= 0.0.4
Requires:	evolution-webcal >= 2.10.0
Requires:	gdm >= 1:2.20.0
Requires:	gnome-applet-fast-user-switch >= 2.20.0
Requires:	gnome-games >= 1:2.20.0.1
Requires:	gnome-games-blackjack >= 1:2.20.0.1
Requires:	gnome-games-extra-data >= 2.20.0
Requires:	gnome-games-extra-data-glines >= 2.20.0
Requires:	gnome-games-extra-data-gnobots2 >= 2.20.0
Requires:	gnome-games-extra-data-gnometris >= 2.20.0
Requires:	gnome-games-extra-data-iagno >= 2.20.0
Requires:	gnome-games-extra-data-mahjongg >= 2.20.0
Requires:	gnome-games-extra-data-same-gnome >= 2.20.0
Requires:	gnome-games-glchess >= 1:2.20.0.1
Requires:	gnome-games-glines >= 1:2.20.0.1
Requires:	gnome-games-gnect >= 1:2.20.0.1
Requires:	gnome-games-gnibbles >= 1:2.20.0.1
Requires:	gnome-games-gnobots2 >= 1:2.20.0.1
Requires:	gnome-games-gnometris >= 1:2.20.0.1
Requires:	gnome-games-gnomine >= 1:2.20.0.1
Requires:	gnome-games-gnotravex >= 1:2.20.0.1
Requires:	gnome-games-gnotski >= 1:2.20.0.1
Requires:	gnome-games-gtali >= 1:2.20.0.1
Requires:	gnome-games-iagno >= 1:2.20.0.1
Requires:	gnome-games-mahjongg >= 1:2.20.0.1
Requires:	gnome-games-same-gnome >= 1:2.20.0.1
Requires:	gnome-games-sol >= 1:2.20.0.1
Requires:	gnome-games-sudoku >= 1:2.20.0.1
Requires:	gnome-themes-Crux >= 2.20.0
Requires:	gnome-themes-Glider >= 2.20.0
Requires:	gnome-themes-Glossy >= 2.20.0
Requires:	gnome-themes-Inverted >= 2.20.0
Requires:	gnome-themes-Mist >= 2.20.0
Requires:	gnome-themes-extras-Darklooks >= 2.20
Requires:	gnome-themes-extras-Foxtrot >= 2.20
Requires:	gnome-themes-extras-Gion >= 2.20
Requires:	gnome-themes-extras-Neu >= 2.20
Requires:	gstreamer-a52dec >= 0.10.6
Requires:	gstreamer-aac >= 0.10.5
Requires:	gstreamer-audio-effects-bad >= 0.10.5
Requires:	gstreamer-bluetooth >= 3.18
Requires:	gstreamer-cairo >= 0.10.6
Requires:	gstreamer-cdaudio >= 0.10.5
Requires:	gstreamer-cdio >= 0.10.6
Requires:	gstreamer-dts >= 0.10.5
Requires:	gstreamer-dv >= 0.10.6
Requires:	gstreamer-dvdread >= 0.10.6
Requires:	gstreamer-flac >= 0.10.6
Requires:	gstreamer-gdkpixbuf >= 0.10.6
Requires:	gstreamer-gnonlin >= 0.10.9
Requires:	gstreamer-gsm >= 0.10.5
Requires:	gstreamer-imagesink-gl >= 0.10.5
Requires:	gstreamer-jack >= 0.10.5
Requires:	gstreamer-ladspa >= 0.10.5
Requires:	gstreamer-lame >= 0.10.6
Requires:	gstreamer-libpng >= 0.10.6
Requires:	gstreamer-mjpegtools >= 0.10.5
Requires:	gstreamer-mms >= 0.10.5
Requires:	gstreamer-mpeg >= 0.10.6
Requires:	gstreamer-musepack >= 0.10.5
Requires:	gstreamer-musicbrainz >= 0.10.5
Requires:	gstreamer-mythtv >= 0.10.5
Requires:	gstreamer-pitfdll >= 0.9cvs
Requires:	gstreamer-plugins-bad >= 0.10.5
Requires:	gstreamer-plugins-ugly >= 0.10.6
Requires:	gstreamer-raw1394 >= 0.10.6
Requires:	gstreamer-shout2 >= 0.10.6
Requires:	gstreamer-sid >= 0.10.6
Requires:	gstreamer-sndfile >= 0.10.5
Requires:	gstreamer-soundtouch >= 0.10.5
Requires:	gstreamer-spc >= 0.10.5
Requires:	gstreamer-speex >= 0.10.6
Requires:	gstreamer-taglib >= 0.10.6
Requires:	gstreamer-timidity >= 0.10.5
Requires:	gstreamer-video-effects >= 0.10.6
Requires:	gstreamer-videosink-aa >= 0.10.6
Requires:	gstreamer-videosink-directfb >= 0.10.5
Requires:	gstreamer-videosink-libcaca >= 0.10.6
Requires:	gstreamer-videosink-sdl >= 0.10.5
Requires:	gstreamer-visualisation >= 0.10.6
Requires:	gstreamer-wavpack >= 0.10.6
Requires:	gstreamer-wildmidi >= 0.10.5
Requires:	gstreamer-ximagesrc >= 0.10.6
Requires:	gthumb >= 2.10.6
Requires:	metacity-themes-AgingGorilla >= 2:2.20.0
Requires:	metacity-themes-Atlanta >= 2:2.20.0
Requires:	metacity-themes-Bright >= 2:2.20.0
Requires:	metacity-themes-Crux >= 2:2.20.0
Requires:	metacity-themes-Esco >= 2:2.20.0
Requires:	metacity-themes-Metabox >= 2:2.20.0
Requires:	metacity-themes-Simple >= 2:2.20.0
Requires:	nautilus-actions >= 1.4
Requires:	rhythmbox >= 0.11.2

%description extras
Metapackage to install additional packages for GNOME Desktop.

%description extras -l pl.UTF-8
Metapakiet instalujący dodatkowe pakiety dla środowiska graficznego
GNOME.

%package extras-accessibility
Summary:	Accessibility packages for GNOME Desktop
Summary(pl.UTF-8):	Pakiety ułatwień dostępu dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	accerciser >= 1.0.0
Requires:	gnome-mag >= 0.14.10
Requires:	gnome-speech >= 0.4.16
Requires:	gnome-themes-HighContrast >= 2.20.0
Requires:	gnome-themes-HighContrast-SVG >= 2.20.0
Requires:	gnome-themes-HighContrastInverse >= 2.20.0
Requires:	gnome-themes-HighContrastLargePrint >= 2.20.0
Requires:	gnome-themes-HighContrastLargePrintInverse >= 2.20.0
Requires:	gnome-themes-LargePrint >= 2.20.0
Requires:	gnome-themes-LowContrast >= 2.20.0
Requires:	gnome-themes-LowContrastLargePrint >= 2.20.0
Requires:	orca >= 2.20.0.1
Requires:	gok >= 1.3.4

%description extras-accessibility
Accessibility packages for GNOME Desktop.

%description extras-accessibility -l pl.UTF-8
Pakiety ułatwień dostępu dla środowiska graficznego GNOME.

%package office
Summary:	Office suite for GNOME Desktop
Summary(pl.UTF-8):	Pakiety biurowe dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	abiword >= 1:2.4.6
Requires:	dia >= 1:0.96.1
Requires:	glabels >= 2.1.3
Requires:	gnumeric >= 1:1.7.12

%description office
Office packages for GNOME Desktop.

%description office -l pl.UTF-8
Pakiety biurowe dla środowiska graficznego GNOME.

%package admin
Summary:	Administration packages for GNOME Desktop
Summary(pl.UTF-8):	Pakiety do zarządzania środowiskiem graficznym GNOME
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	pessulus >= 2.16.3
Requires:	sabayon >= 2.20.1

%description admin
Administration packages for GNOME Desktop.

%description admin -l pl.UTF-8
Pakiety do zarządzania środowiskiem graficznym GNOME.

%prep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%files extras
%defattr(644,root,root,755)
%files extras-accessibility
%defattr(644,root,root,755)
%files office
%defattr(644,root,root,755)
%files admin
%defattr(644,root,root,755)
