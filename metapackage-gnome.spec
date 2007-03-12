#
# TODO:
# - metapackage with development tools (glade, bluefish, anjuta, etc.)
# - metapackage 3rd party (everything else ;)
#
Summary:	GNOME Desktop Suite
Summary(pl.UTF-8):	Środowisko graficzne GNOME
Name:		metapackage-gnome
Version:	2.14
Release:	3
License:	GPL/LGPL
Group:		X11/Applications
Requires:	bug-buddy >= 2.14.0
Requires:	cdrtools
Requires:	cdrtools-mkisofs
Requires:	cdrtools-readcd
Requires:	control-center >= 2.14.1
Requires:	eog >= 2.14.1
Requires:	epiphany >= 2.14.1
Requires:	epiphany-extension-gwget >= 0.98
Requires:	epiphany-extensions >= 2.14.1
Requires:	evince >= 0.5.2
Requires:	evolution >= 2.6.1
Requires:	evolution-addressbook >= 2.6.1
Requires:	evolution-mail >= 2.6.1
Requires:	file-roller >= 2.14.1
Requires:	gcalctool >= 5.7.32
Requires:	gconf-editor >= 2.14.0
Requires:	gedit2 >= 2.14.2
Requires:	gnome-applet-deskbar >= 2.14.1.1
Requires:	gnome-applets-accessx-status >= 1:2.14.1
Requires:	gnome-applets-battstat >= 1:2.14.1
Requires:	gnome-applets-charpicker >= 1:2.14.1
Requires:	gnome-applets-cpufreq >= 1:2.14.1
Requires:	gnome-applets-drivemount >= 1:2.14.1
Requires:	gnome-applets-geyes >= 1:2.14.1
Requires:	gnome-applets-gtik >= 1:2.14.1
Requires:	gnome-applets-gweather >= 1:2.14.1
Requires:	gnome-applets-keyboard >= 1:2.14.1
Requires:	gnome-applets-mixer >= 1:2.14.1
Requires:	gnome-applets-modemlights >= 1:2.14.1
Requires:	gnome-applets-multiload >= 1:2.14.1
Requires:	gnome-applets-stickynotes >= 1:2.14.1
Requires:	gnome-applets-trash >= 1:2.14.1
Requires:	gnome-backgrounds >= 2.14.1
Requires:	gnome-commander >= 1.2.0
Requires:	gnome-keyring-manager >= 2.14.0
Requires:	gnome-mail-notification >= 2.0-3
Requires:	gnome-media-cd >= 2.14.0
Requires:	gnome-media-cddb >= 2.14.0
Requires:	gnome-media-sound-recorder >= 2.14.0
Requires:	gnome-media-volume-control >= 2.14.0
Requires:	gnome-media-vumeter >= 2.14.0
Requires:	gnome-menus >= 2.14.0
Requires:	gnome-netstatus >= 2.12.0
Requires:	gnome-nettool >= 2.14.1
Requires:	gnome-panel >= 2.14.1
Requires:	gnome-power-manager >= 2.14.3
Requires:	gnome-screensaver >= 2.14.1
Requires:	gnome-session >= 2.14.1
Requires:	gnome-system-monitor >= 2.14.1
Requires:	gnome-system-tools >= 2.14.0
Requires:	gnome-terminal >= 2.14.1
Requires:	gnome-themes-Clearlooks >= 2.14.0
Requires:	gnome-utils-dictionary >= 1:2.14.0
Requires:	gnome-utils-floppy >= 1:2.14.0
Requires:	gnome-utils-logview >= 1:2.14.0
Requires:	gnome-utils-screenshot >= 1:2.14.0
Requires:	gnome-utils-search-tool >= 1:2.14.0
Requires:	gnome-volume-manager >= 1.5.15
Requires:	gstreamer >= 0.10.5
Requires:	gstreamer-GConf >= 0.10.2
Requires:	gstreamer-audio-effects-base >= 0.10.6
Requires:	gstreamer-audio-effects-good >= 0.10.2
Requires:	gstreamer-audio-formats >= 0.10.2
Requires:	gstreamer-audiosink-alsa >= 0.10.6
Requires:	gstreamer-audiosink-esd >= 0.10.2
Requires:	gstreamer-audiosink-oss >= 0.10.2
Requires:	gstreamer-cdparanoia >= 0.10.6
Requires:	gstreamer-ffmpeg >= 0.10.1
Requires:	gstreamer-gnomevfs >= 0.10.6
Requires:	gstreamer-imagesink-x >= 0.10.6
Requires:	gstreamer-imagesink-xv >= 0.10.6
Requires:	gstreamer-libvisual >= 0.10.6
Requires:	gstreamer-mad >= 0.10.3
Requires:	gstreamer-plugins-base >= 0.10.6
Requires:	gstreamer-plugins-good >= 0.10.2
Requires:	gstreamer-theora >= 0.10.6
Requires:	gstreamer-vorbis >= 0.10.6
Requires:	gucharmap >= 1.6.0
Requires:	gwget >= 0.98
Requires:	metacity >= 2:2.14.2
Requires:	nautilus >= 2.14.1
Requires:	nautilus-cd-burner >= 2.14.1
Requires:	nautilus-extension-evince >= 0.5.2
Requires:	nautilus-sendto >= 0.5
Requires:	nautilus-sendto-evolution >= 0.5
Requires:	sound-juicer >= 2.14.2
Requires:	totem >= 1.4.0
Requires:	vino >= 2.13.5
Requires:	yelp >= 2.14.1
Requires:	zenity >= 2.14.1
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
Requires:	dasher >= 4.0.2
Requires:	evolution-calendar >= 2.6.1
Requires:	evolution-exchange >= 2.6.1
Requires:	evolution-webcal >= 2.6.0
Requires:	gdm >= 1:2.14.5
Requires:	gnome-applet-fast-user-switch >= 2.14.1
Requires:	gnome-games >= 1:2.14.1
Requires:	gnome-games-blackjack >= 1:2.14.1
Requires:	gnome-games-extra-data >= 2.14.0
Requires:	gnome-games-extra-data-glines >= 2.14.0
Requires:	gnome-games-extra-data-gnobots2 >= 2.14.0
Requires:	gnome-games-extra-data-gnometris >= 2.14.0
Requires:	gnome-games-extra-data-iagno >= 2.14.0
Requires:	gnome-games-extra-data-mahjongg >= 2.14.0
Requires:	gnome-games-extra-data-same-gnome >= 2.14.0
Requires:	gnome-games-gataxx >= 1:2.14.1
Requires:	gnome-games-glines >= 1:2.14.1
Requires:	gnome-games-gnect >= 1:2.14.1
Requires:	gnome-games-gnibbles >= 1:2.14.1
Requires:	gnome-games-gnobots2 >= 1:2.14.1
Requires:	gnome-games-gnometris >= 1:2.14.1
Requires:	gnome-games-gnomine >= 1:2.14.1
Requires:	gnome-games-gnotravex >= 1:2.14.1
Requires:	gnome-games-gnotski >= 1:2.14.1
Requires:	gnome-games-gtali >= 1:2.14.1
Requires:	gnome-games-iagno >= 1:2.14.1
Requires:	gnome-games-mahjongg >= 1:2.14.1
Requires:	gnome-games-same-gnome >= 1:2.14.1
Requires:	gnome-games-sol >= 1:2.14.1
Requires:	gnome-themes-Crux >= 2.14.0
Requires:	gnome-themes-Flat-Blue >= 2.14.0
Requires:	gnome-themes-Glider >= 2.14.0
Requires:	gnome-themes-Grand-Canyon >= 2.14.0
Requires:	gnome-themes-Mist >= 2.14.0
Requires:	gnome-themes-Ocean-Dream >= 2.14.0
Requires:	gnome-themes-Sandwish >= 2.14.0
Requires:	gnome-themes-Sandy >= 2.14.0
Requires:	gnome-themes-Simple >= 2.14.0
Requires:	gnome-themes-Smokey >= 2.14.0
Requires:	gnome-themes-Smokey-Blue >= 2.14.0
Requires:	gnome-themes-Smokey-Red >= 2.14.0
Requires:	gnome-themes-Traditional >= 2.14.0
Requires:	gnome-themes-extras-Amaranth >= 0.9.0-2
Requires:	gnome-themes-extras-Gorilla >= 0.9.0-2
Requires:	gnome-themes-extras-Lush >= 0.9.0-2
Requires:	gnome-themes-extras-Nuvola >= 0.9.0-2
Requires:	gnome-themes-extras-Wasp >= 0.9.0-2
Requires:	gstreamer-aac >= 0.10.1
Requires:	gstreamer-audio-effects-bad >= 0.10.1
Requires:	gstreamer-dts >= 0.10.1
Requires:	gstreamer-dv >= 0.10.2
Requires:	gstreamer-dvdread >= 0.10.3
Requires:	gstreamer-flac >= 0.10.2
Requires:	gstreamer-gsm >= 0.10.1
Requires:	gstreamer-imagesink-gl >= 0.10.1
Requires:	gstreamer-lame >= 0.10.3
Requires:	gstreamer-libpng >= 0.10.2
Requires:	gstreamer-mms >= 0.10.1
Requires:	gstreamer-mpeg >= 0.10.3
Requires:	gstreamer-musepack >= 0.10.1
Requires:	gstreamer-plugins-bad >= 0.10.1
Requires:	gstreamer-plugins-ugly >= 0.10.3
Requires:	gstreamer-raw1394 >= 0.10.2
Requires:	gstreamer-shout2 >= 0.10.2
Requires:	gstreamer-sid >= 0.10.3
Requires:	gstreamer-speex >= 0.10.2
Requires:	gstreamer-swfdec >= 0.10.1
Requires:	gstreamer-video-effects >= 0.10.2
Requires:	gstreamer-videosink-aa >= 0.10.2
Requires:	gstreamer-videosink-directfb >= 0.10.1
Requires:	gstreamer-videosink-libcaca >= 0.10.2
Requires:	gstreamer-videosink-sdl >= 0.10.1
Requires:	gstreamer-visualisation >= 0.10.2
Requires:	gstreamer-wavpack >= 0.10.1
Requires:	gstreamer-xvid >= 0.10.1
Requires:	gthumb >= 2.6.8
Requires:	metacity-themes-AgingGorilla >= 2:2.14.3
Requires:	metacity-themes-Atlanta >= 2:2.14.3
Requires:	metacity-themes-Bright >= 2:2.14.3
Requires:	metacity-themes-Crux >= 2:2.14.3
Requires:	metacity-themes-Esco >= 2:2.14.3
Requires:	metacity-themes-Metabox >= 2:2.14.3
Requires:	metacity-themes-Simple >= 2:2.14.3
Requires:	nautilus-actions >= 1.2
Requires:	rhythmbox >= 0.9.4.1

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
Requires:	gnome-mag >= 0.12.4
Requires:	gnome-speech >= 0.3.10
Requires:	gnome-themes-HighContrast >= 2.14.0
Requires:	gnome-themes-HighContrastInverse >= 2.14.0
Requires:	gnome-themes-HighContrastLargePrint >= 2.14.0
Requires:	gnome-themes-HighContrastLargePrintInverse >= 2.14.0
Requires:	gnome-themes-LargePrint >= 2.14.0
Requires:	gnome-themes-LowContrast >= 2.14.0
Requires:	gnome-themes-LowContrastLargePrint >= 2.14.0
Requires:	gnopernicus >= 1.0.4
Requires:	gok >= 1.0.10

%description extras-accessibility
Accessibility packages for GNOME Desktop.

%description extras-accessibility -l pl.UTF-8
Pakiety ułatwień dostępu dla środowiska graficznego GNOME.

%package office
Summary:	Office suite for GNOME Desktop
Summary(pl.UTF-8):	Pakiety biurowe dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	abiword >= 1:2.2.9
Requires:	dia >= 1:0.94-8
Requires:	glabels >= 2.0.2-3
Requires:	gnumeric >= 1:1.4.3-5

%description office
Office packages for GNOME Desktop.

%description office -l pl.UTF-8
Pakiety biurowe dla środowiska graficznego GNOME.

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
