#
# TODO:
# - metapackage with development tools (glade, bluefish, anjuta, etc.)
# - metapackage 3rd party (everything else ;)
#
Summary:	GNOME Desktop Suite
Summary(pl):	¦rodowisko graficzne GNOME
Name:		metapackage-gnome
Version:	2.12.1
Release:	1
License:	GPL/LGPL
Group:		X11/Applications/Desktop
Requires:	bug-buddy >= 2.12.1
Requires:	cdrtools
Requires:	cdrtools-mkisofs
Requires:	cdrtools-readcd
Requires:	eog >= 2.12.1
Requires:	epiphany >= 1.8.2
Requires:	evince >= 0.4.0-2
Requires:	file-roller >= 2.12.1
Requires:	gcalctool >= 5.6.31
Requires:	gconf-editor >= 2.12.0
Requires:	gedit2 >= 2.12.1
Requires:	gnome-applets-accessx-status >= 1:2.12.1
Requires:	gnome-applets-battstat >= 1:2.12.1
Requires:	gnome-applets-charpicker >= 1:2.12.1
Requires:	gnome-applets-cpufreq >= 1:2.12.1
Requires:	gnome-applets-drivemount >= 1:2.12.1
Requires:	gnome-applets-geyes >= 1:2.12.1
Requires:	gnome-applets-gtik >= 1:2.12.1
Requires:	gnome-applets-gweather >= 1:2.12.1
Requires:	gnome-applets-keyboard >= 1:2.12.1
Requires:	gnome-applets-minicommander >= 1:2.12.1
Requires:	gnome-applets-mixer >= 1:2.12.1
Requires:	gnome-applets-modemlights >= 1:2.12.1
Requires:	gnome-applets-multiload >= 1:2.12.1
Requires:	gnome-applets-stickynotes >= 1:2.12.1
Requires:	gnome-applets-trash >= 1:2.12.1
Requires:	gnome-backgrounds >= 2.12.1
Requires:	gnome-keyring-manager >= 2.12.0
Requires:	gnome-media-cd >= 2.12.0
Requires:	gnome-media-sound-recorder >= 2.12.0
Requires:	gnome-media-volume-control >= 2.12.0
Requires:	gnome-media-vumeter >= 2.12.0
Requires:	gnome-menus >= 2.12.0-2
Requires:	gnome-netstatus >= 2.12.0
Requires:	gnome-nettool >= 1.4.1
Requires:	gnome-panel >= 2.12.1
Requires:	gnome-session >= 2.12.0-2
Requires:	gnome-system-monitor >= 2.12.1
Requires:	gnome-terminal >= 2.12.0
Requires:	gnome-themes-Clearlooks >= 2.12.1
Requires:	gnome-utils-dict >= 1:2.12.1
Requires:	gnome-utils-floppy >= 1:2.12.1
Requires:	gnome-utils-logview >= 1:2.12.1
Requires:	gnome-utils-screenshot >= 1:2.12.1
Requires:	gnome-utils-search-tool >= 1:2.12.1
Requires:	gnome-volume-manager >= 1.5.2
Requires:	gstreamer >= 0.8.11
Requires:	gstreamer-audio-effects >= 0.8.11
Requires:	gstreamer-audiofile >= 0.8.11
Requires:	gstreamer-audio-formats >= 0.8.11
Requires:	gstreamer-audiosink-alsa >= 0.8.11
Requires:	gstreamer-audiosink-esd >= 0.8.11
Requires:	gstreamer-audiosink-oss >= 0.8.11
Requires:	gstreamer-cdparanoia >= 0.8.11
Requires:	gstreamer-GConf >= 0.8.11
Requires:	gstreamer-gnomevfs >= 0.8.11
Requires:	gstreamer-mad >= 0.8.11
Requires:	gstreamer-vorbis >= 0.8.11
Requires:	metacity >= 2:2.12.1
Requires:	nautilus >= 2.12.1
Requires:	nautilus-cd-burner >= 2.12.0
Requires:	sound-juicer >= 2.12.2
Requires:	totem >= 1.2.0-4
Requires:	vino >= 2.12.0
Requires:	xscreensaver-gnome2 >= 4.19-4
Requires:	yelp >= 2.12.1-2
Requires:	zenity >= 2.12.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Desktop suite metapackage.

%description -l pl
Metapakiet ¶rodowiska graficznego GNOME.

%package extras
Summary:	Metapackage to install additional packages for GNOME Desktop
Summary(pl):	Metapakiet instaluj±cy dodatkowe pakiety dla ¶rodowiska graficznego GNOME
Group:		X11/Applications/Desktop
Requires:	%{name} = %{version}-%{release}
Requires:	dasher >= 3.2.18
Requires:	epiphany-extensions >= 1.8.1
Requires:	evolution-calendar >= 2.4.1
Requires:	evolution-exchange >= 2.4.1
Requires:	evolution-mail >= 2.4.1
Requires:	evolution-webcal >= 2.4.1
Requires:	gdm >= 1:2.8.0.5
Requires:	gnome-games-blackjack >= 1:2.12.1
Requires:	gnome-games-extra-data-glines >= 2.12.0
Requires:	gnome-games-extra-data-gnobots2 >= 2.12.0
Requires:	gnome-games-extra-data-gnometris >= 2.12.0
Requires:	gnome-games-extra-data-iagno >= 2.12.0
Requires:	gnome-games-extra-data-mahjongg >= 2.12.0
Requires:	gnome-games-extra-data-same-gnome >= 2.12.0
Requires:	gnome-games-gataxx >= 1:2.12.1
Requires:	gnome-games-glines >= 1:2.12.1
Requires:	gnome-games-gnect >= 1:2.12.1
Requires:	gnome-games-gnibbles >= 1:2.12.1
Requires:	gnome-games-gnobots2 >= 1:2.12.1
Requires:	gnome-games-gnometris >= 1:2.12.1
Requires:	gnome-games-gnomine >= 1:2.12.1
Requires:	gnome-games-gnotravex >= 1:2.12.1
Requires:	gnome-games-gnotski >= 1:2.12.1
Requires:	gnome-games-gtali >= 1:2.12.1
Requires:	gnome-games-iagno >= 1:2.12.1
Requires:	gnome-games-mahjongg >= 1:2.12.1
Requires:	gnome-games-same-gnome >= 1:2.12.1
Requires:	gnome-games-sol >= 1:2.12.1
Requires:	gnome-games-stones >= 1:2.12.1
Requires:	gnome-mail-notification >= 2.0-2
Requires:	gnome-themes-Crux >= 2.12.1
Requires:	gnome-themes-extras-Amaranth >= 0.8.1
Requires:	gnome-themes-extras-Gorilla >= 0.8.1
Requires:	gnome-themes-extras-Lush >= 0.8.1
Requires:	gnome-themes-extras-Nuvola >= 0.8.1
Requires:	gnome-themes-extras-Wasp >= 0.8.1
Requires:	gnome-themes-Flat-Blue >= 2.12.1
Requires:	gnome-themes-Glider >= 2.12.1
Requires:	gnome-themes-Grand-Canyon >= 2.12.0
Requires:	gnome-themes-Mist >= 2.12.0
Requires:	gnome-themes-Ocean-Dream >= 2.12.0
Requires:	gnome-themes-Sandwish >= 2.12.0
Requires:	gnome-themes-Sandy >= 2.12.0
Requires:	gnome-themes-Simple >= 2.12.0
Requires:	gnome-themes-Smokey >= 2.12.0
Requires:	gnome-themes-Smokey-Blue >= 2.12.0
Requires:	gnome-themes-Smokey-Red >= 2.12.0
Requires:	gnome-themes-Traditional >= 2.12.0
Requires:	gstreamer-aac >= 0.8.11
Requires:	gstreamer-flac >= 0.8.11
Requires:	gstreamer-mms >= 0.8.11
Requires:	gthumb >= 2.6.8
Requires:	metacity-themes-AgingGorilla >= 2:2.12.0
Requires:	metacity-themes-Atlanta >= 2:2.12.0
Requires:	metacity-themes-Bright >= 2:2.12.0
Requires:	metacity-themes-Crux >= 2:2.12.0
Requires:	metacity-themes-Esco >= 2:2.12.0
Requires:	metacity-themes-Metabox >= 2:2.12.0
Requires:	metacity-themes-Simple >= 2:2.12.0
Requires:	rhythmbox >= 0.8.8-4

%description extras
Metapackage to install additional packages for GNOME Desktop.

%description extras -l pl
Metapakiet instaluj±cy dodatkowe pakiety dla ¶rodowiska graficznego
GNOME.

%package extras-accessibility
Summary:	Accessibility packages for GNOME Desktop
Summary(pl):	Pakiety u³atwieñ dostêpu dla ¶rodowiska graficznego GNOME
Group:		X11/Applications/Desktop
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-mag >= 0.12.2
Requires:	gnome-speech >= 0.3.7
Requires:	gnome-themes-HighContrast >= 2.12.0
Requires:	gnome-themes-HighContrastInverse >= 2.12.0
Requires:	gnome-themes-HighContrastLargePrint >= 2.12.0
Requires:	gnome-themes-HighContrastLargePrintInverse >= 2.12.0
Requires:	gnome-themes-LargePrint >= 2.12.0
Requires:	gnome-themes-LowContrast >= 2.12.0
Requires:	gnome-themes-LowContrastLargePrint >= 2.12.0
Requires:	gnopernicus >= 0.11.6
Requires:	gok >= 1.0.5

%description extras-accessibility
Accessibility packages for GNOME Desktop.

%description extras-accessibility -l pl
Pakiety u³atwieñ dostêpu dla ¶rodowiska graficznego GNOME.

%package office
Summary:	Office suite for GNOME Desktop
Summary(pl):	Pakiety biurowe dla ¶rodowiska graficznego GNOME
Group:		X11/Applications/Desktop
Requires:	%{name} = %{version}-%{release}
Requires:	abiword >= 1:2.2.9
Requires:	dia >= 1:0.94-8
Requires:	glabels >= 2.0.2-3
Requires:	gnumeric >= 1:1.4.3-5

%description office
Office packages for GNOME Desktop.

%description office -l pl
Pakiety biurowe dla ¶rodowiska graficznego GNOME.

%files
%files extras
%files extras-accessibility
%files office
