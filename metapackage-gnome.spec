# TODO:
#	- send to builders: 
#		- poppler
#		- evince
#		- gnome-games-extra-data
#		- gstreamer-plugins
#	- write extras summary/desc
#
Summary:	GNOME Desktop Suite
Summary(pl):	¦rodowisko graficzne GNOME
Name:		metapackage-gnome
Version:	2.10.1
Release:	0.1
License:	GPL/LGPL
Group:		X11/Applications/Desktop
Requires:	epiphany >= 1.6.3-1
Requires:	eog >= 2.10.0-2
Requires:	file-roller >= 2.10.3-1
Requires:	gcalctool >= 5.5.42-1
Requires:	gedit2 >= 2.10.2-1
Requires:	ggv >= 2.8.4-3
Requires:	gnome-applets-accessx-status >= 2.10.1-3
Requires:	gnome-applets-battstat >= 2.10.1-3
Requires:	gnome-applets-charpicker >= 2.10.1-3
Requires:	gnome-applets-cpufreq >= 2.10.1-3
Requires:	gnome-applets-drivemount >= 2.10.1-3
Requires:	gnome-applets-geyes >= 2.10.1-3
Requires:	gnome-applets-gtik >= 2.10.1-3
Requires:	gnome-applets-gweather >= 2.10.1-3
Requires:	gnome-applets-keyboard >= 2.10.1-3
Requires:	gnome-applets-minicommander >= 2.10.1-3
Requires:	gnome-applets-mixer >= 2.10.1-3
Requires:	gnome-applets-modemlights >= 2.10.1-3
Requires:	gnome-applets-multiload >= 2.10.1-3
Requires:	gnome-applets-stickynotes >= 2.10.1-3
Requires:	gnome-applets-trash >= 2.10.1-3
Requires:	gnome-media-cd >= 2.10.2-1
Requires:	gnome-media-sound-recorder >= 2.10.2-1
Requires:	gnome-media-volume-control >= 2.10.2-1
Requires:	gnome-media-vumeter >= 2.10.2-1
Requires:	gnome-panel >= 2.10.1-2
Requires:	gnome-session >= 2.10.0-2
Requires:	gnome-terminal >= 2.10.0-3
Requires:	gnome-utils-dict >= 2.10.1-1
Requires:	gnome-utils-floppy >= 2.10.1-1
Requires:	gnome-utils-logview >= 2.10.1-1
Requires:	gnome-utils-screenshot >= 2.10.1-1
Requires:	gnome-utils-search-tool >= 2.10.1-1
Requires:	gnome-volume-manager >= 1.2.2-1
Requires:	gpdf >= 2.10.0-2
Requires:	gstreamer >= 0.8.10-1
Requires:	gstreamer-aac >= 0.8.8-3
Requires:	gstreamer-audio-effects >= 0.8.8-3
Requires:	gstreamer-audiofile >= 0.8.8-3
Requires:	gstreamer-audio-formats >= 0.8.8-3
Requires:	gstreamer-audiosink-alsa >= 0.8.8-3
Requires:	gstreamer-audiosink-esd >= 0.8.8-3
Requires:	gstreamer-audiosink-oss >= 0.8.8-3
Requires:	gstreamer-cdparanoia >= 0.8.8-3
Requires:	gstreamer-flac >= 0.8.8-3
Requires:	gstreamer-GConf >= 0.8.8-3
Requires:	gstreamer-gnomevfs >= 0.8.8-3
Requires:	gstreamer-mad >= 0.8.8-3
Requires:	gstreamer-mms >= 0.8.8-3
Requires:	gstreamer-vorbis >= 0.8.8-3
Requires:	metacity >= 2.10.1-1
Requires:	nautilus >= 2.10.1-4
Requires:	totem >= 1.0.1-3
Requires:	yelp >= 2.6.5-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Desktop suite metapackage.

%description -l pl
Metapakiet ¶rodowiska graficznego GNOME.

%package extras
Summary:	Write me
Summary(pl):	Write me
Group:		X11/Applications/Desktop
Requires:	%{name} = %{version}-%{release}
Requires:	bug-buddy >= 2.10.0-4
Requires:	dasher >= 3.2.15-2
Requires:	epiphany-extensions >= 1.6.3-1
Requires:	evince >= 0.3.1-1
Requires:	evolution-calendar >= 2.2.2-2
Requires:	evolution-mail >= 2.2.2-2
Requires:	evolution-webcal >= 2.2.1-1
Requires:	gconf-editor >= 2.10.0-3
Requires:	gdm >= 1:2.6.0.9-2
Requires:	gthumb >= 2.6.5-1
Requires:	gnome-backgrounds >= 2.10.1-1
Requires:	gnome-games-blackjack >= 1:2.10.1-1
Requires:	gnome-games-extra-data-glines >= 2.10.0-2
Requires:	gnome-games-extra-data-gnobots2 >= 2.10.0-2
Requires:	gnome-games-extra-data-gnometris >= 2.10.0-2
Requires:	gnome-games-extra-data-iagno >= 2.10.0-2
Requires:	gnome-games-extra-data-mahjongg >= 2.10.0-2
Requires:	gnome-games-extra-data-same-gnome >= 2.10.0-2
Requires:	gnome-games-gataxx >= 1:2.10.1-1
Requires:	gnome-games-glines >= 1:2.10.1-1
Requires:	gnome-games-gnect >= 1:2.10.1-1
Requires:	gnome-games-gnibbles >= 1:2.10.1-1
Requires:	gnome-games-gnobots2 >= 1:2.10.1-1
Requires:	gnome-games-gnometris >= 1:2.10.1-1
Requires:	gnome-games-gnomine >= 1:2.10.1-1
Requires:	gnome-games-gnotravex >= 1:2.10.1-1
Requires:	gnome-games-gnotski >= 1:2.10.1-1
Requires:	gnome-games-gtali >= 1:2.10.1-1
Requires:	gnome-games-iagno >= 1:2.10.1-1
Requires:	gnome-games-mahjongg >= 1:2.10.1-1
Requires:	gnome-games-same-gnome >= 1:2.10.1-1
Requires:	gnome-games-sol >= 1:2.10.1-1
Requires:	gnome-games-stones >= 1:2.10.1-1
Requires:	gnome-mag >= 0.12.0-1
Requires:	gnome-mail-notification >= 1.1-5
Requires:	gnome-netstatus >= 2.10.0-3
Requires:	gnome-speech >= 0.3.7-1
Requires:	gnome-system-monitor >= 2.10.1-1
Requires:	gnome-themes-Crux >= 2.10.1-1
Requires:	gnome-themes-extras-Amaranth >= 0.8.1-1
Requires:	gnome-themes-extras-Gorilla >= 0.8.1-1
Requires:	gnome-themes-extras-Lush >= 0.8.1-1
Requires:	gnome-themes-extras-Nuvola >= 0.8.1-1
Requires:	gnome-themes-extras-Wasp >= 0.8.1-1
Requires:	gnome-themes-Flat-Blue >= 2.10.1-1
Requires:	gnome-themes-Glider >= 2.10.1-1
Requires:	gnome-themes-Grand-Canyon >= 2.10.1-1
Requires:	gnome-themes-HighContrast >= 2.10.1-1
Requires:	gnome-themes-HighContrastInverse >= 2.10.1-1
Requires:	gnome-themes-HighContrastLargePrint >= 2.10.1-1
Requires:	gnome-themes-HighContrastLargePrintInverse >= 2.10.1-1
Requires:	gnome-themes-LargePrint >= 2.10.1-1
Requires:	gnome-themes-LowContrast >= 2.10.1-1
Requires:	gnome-themes-LowContrastLargePrint >= 2.10.1-1
Requires:	gnome-themes-Mist >= 2.10.1-1
Requires:	gnome-themes-Ocean-Dream >= 2.10.1-1
Requires:	gnome-themes-Sandwish >= 2.10.1-1
Requires:	gnome-themes-Sandy >= 2.10.1-1
Requires:	gnome-themes-Simple >= 2.10.1-1
Requires:	gnome-themes-Smokey >= 2.10.1-1
Requires:	gnome-themes-Smokey-Blue >= 2.10.1-1
Requires:	gnome-themes-Smokey-Red >= 2.10.1-1
Requires:	gnome-themes-Traditional >= 2.10.1-1
Requires:	gnopernicus >= 0.10.9-1
Requires:	gok >= 1.0.3-2
Requires:	goobox >= 0.9.91-1
Requires:	metacity-themes-AgingGorilla >= 2.10.1-1
Requires:	metacity-themes-Atlanta >= 2.10.1-1
Requires:	metacity-themes-Bright >= 2.10.1-1
Requires:	metacity-themes-Crux >= 2.10.1-1
Requires:	metacity-themes-Esco >= 2.10.1-1
Requires:	metacity-themes-Metabox >= 2.10.1-1
Requires:	metacity-themes-Simple >= 2.10.1-1
Requires:	nautilus-cd-burner >= 2.10.1-1
Requires:	rhythmbox >= 0.8.8-4
Requires:	sound-juicer >= 2.10.1-1
Requires:	vino >= 2.10.0-3
Requires:	ximian-connector >= 2.2.2-2

%description extras
Write me.

%description extras -l pl
Write me.

%files

%files extras
