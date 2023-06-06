Summary:	GNOME Desktop Environment with additional packages
Summary(pl.UTF-8):	Środowisko graficzne GNOME z dodatkowymi pakietami
Name:		metapackage-gnome
Version:	43
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
Requires:	gnome-getting-started-docs >= 3.38.0
Requires:	gnome-tour >= 43
Requires:	rhythmbox >= 3.4.7
Requires:	gstreamer-a52dec >= 1.20
Requires:	gstreamer-aac >= 1.20
Requires:	gstreamer-amrnb >= 1.20
Requires:	gstreamer-amrwb >= 1.20
Requires:	gstreamer-ass >= 1.20
Requires:	gstreamer-audio-effects-bad >= 1.20
Requires:	gstreamer-cdio >= 1.20
Requires:	gstreamer-curl >= 1.20
Requires:	gstreamer-dc1394 >= 1.20
Requires:	gstreamer-dts >= 1.20
Requires:	gstreamer-dvdread >= 1.20
Requires:	gstreamer-flite >= 1.20
Requires:	gstreamer-gme >= 1.20
Requires:	gstreamer-gsm >= 1.20
Requires:	gstreamer-kate >= 1.20
Requires:	gstreamer-ladspa >= 1.20
Requires:	gstreamer-lv2 >= 1.20
Requires:	gstreamer-mjpegtools >= 1.20
Requires:	gstreamer-mpeg >= 1.20
Requires:	gstreamer-musepack >= 1.20
Requires:	gstreamer-neon >= 1.20
Requires:	gstreamer-plugins-bad >= 1.20
Requires:	gstreamer-plugins-ugly >= 1.20
Requires:	gstreamer-resindvd >= 1.20
Requires:	gstreamer-rtmp >= 1.20
Requires:	gstreamer-sid >= 1.20
Requires:	gstreamer-sndfile >= 1.20
Requires:	gstreamer-soundtouch >= 1.20
Requires:	gstreamer-videosink-directfb >= 1.20
Requires:	gstreamer-vpx >= 1.20
Requires:	gstreamer-x264 >= 1.20
Requires:	gstreamer-zbar >= 1.20
Requires:	shotwell >= 0.30
Suggests:	tracker >= 2.3
Suggests:	tracker3 >= 3.4
Obsoletes:	metapackage-gnome-extras < 2.22
Obsoletes:	gnome < 2
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
Requires:	at-spi2-atk >= 2.46.0
Requires:	at-spi2-core >= 2.46.0
Requires:	orca >= 43
Provides:	metapackage-gnome-extras-accessibility
Obsoletes:	metapackage-gnome-extras-accessibility < 2.22

%description accessibility
Accessibility packages for GNOME Desktop Environment.

%description accessibility -l pl.UTF-8
Pakiety ułatwień dostępu dla środowiska graficznego GNOME.

%package admin
Summary:	Administration packages for GNOME Desktop Environment
Summary(pl.UTF-8):	Pakiety do zarządzania środowiskiem graficznym GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	gnome-initial-setup >= 43
Requires:	gnome-software >= 43
Obsoletes:	gnome-system-tools < 3.0.1
Obsoletes:	system-tools-backends < 3

%description admin
Administration packages for GNOME Desktop Environment.

%description admin -l pl.UTF-8
Pakiety do zarządzania środowiskiem graficznym GNOME.

%package core
Summary:	The core components of the GNOME Desktop Environment
Summary(pl.UTF-8):	Podstawowe składniki środowiska graficznego GNOME
Group:		X11/Applications
Requires:	PackageKit-gtk3-module
Requires:	adwaita-icon-theme >= 43
Requires:	dconf >= 0.40.0
Requires:	eog >= 43
Requires:	gedit >= 43
Requires:	gnome-control-center >= 1:43
Requires:	gnome-desktop >= 43
Requires:	gnome-keyring >= 42
Requires:	gnome-session >= 1:43
Requires:	gnome-settings-daemon >= 1:43
Requires:	gnome-shell >= 43
Requires:	gnome-terminal >= 3.44
Requires:	gsettings-desktop-schemas >= 43
Requires:	gvfs >= 1.50.0
Requires:	mutter >= 43
Requires:	nautilus >= 43
Requires:	xdg-menus
Requires:	yelp >= 42
Suggests:	gnome-menus >= 3.36.0
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
Requires:	NetworkManager >= 2:1.40.0
Requires:	brasero >= 3.12.0
#Requires:	abrt-desktop >= 2.14.0
Requires:	cheese >= 43
Requires:	dconf-editor >= 43
Requires:	eog-plugins >= 42
Requires:	epiphany >= 43
Requires:	evince >= 43
Requires:	evolution >= 3.46.0
Requires:	evolution-addressbook >= 3.46.0
Requires:	evolution-calendar >= 3.46.0
Requires:	evolution-mail >= 3.46.0
Requires:	file-roller >= 43
Requires:	gnome-calculator >= 43
Requires:	gnome-calendar >= 43
Requires:	gdm >= 2:43
Requires:	gnome-backgrounds >= 43
Requires:	gnome-bluetooth >= 42
Requires:	gnome-color-manager >= 3.36.0
Requires:	gnome-connections >= 43
Requires:	gnome-disk-utility >= 43
Requires:	gnome-packagekit >= 43
Requires:	gnome-power-manager >= 43
Requires:	gnome-remote-desktop >= 43
Requires:	gnome-system-monitor >= 42
Requires:	gnome-tweaks >= 40
Requires:	gnome-user-docs >= 43
Requires:	gstreamer >= 1.20
Requires:	gstreamer-audio-effects-base >= 1.20
Requires:	gstreamer-audio-effects-good >= 1.20
Requires:	gstreamer-audio-formats >= 1.20
Requires:	gstreamer-audiosink-alsa >= 1.20
Requires:	gstreamer-cairo >= 1.20
Requires:	gstreamer-cdparanoia >= 1.20
Requires:	gstreamer-dv >= 1.20
Requires:	gstreamer-flac >= 1.20
Requires:	gstreamer-gdkpixbuf >= 1.20
Requires:	gstreamer-imagesink-x >= 1.20
Requires:	gstreamer-imagesink-xv >= 1.20
Requires:	gstreamer-jack >= 1.20
Requires:	gstreamer-libpng >= 1.20
Requires:	gstreamer-libvisual >= 1.20
Requires:	gstreamer-pango >= 1.20
Requires:	gstreamer-plugins-base >= 1.20
Requires:	gstreamer-plugins-good >= 1.20
Requires:	gstreamer-pulseaudio >= 1.20
Requires:	gstreamer-raw1394 >= 1.20
Requires:	gstreamer-shout2 >= 1.20
Requires:	gstreamer-soup >= 1.20
Requires:	gstreamer-speex >= 1.20
Requires:	gstreamer-taglib >= 1.20
Requires:	gstreamer-theora >= 1.20
Requires:	gstreamer-v4l2 >= 1.20
Requires:	gstreamer-video-effects >= 1.20
Requires:	gstreamer-videosink-aa >= 1.20
Requires:	gstreamer-videosink-libcaca >= 1.20
Requires:	gstreamer-visualisation >= 1.20
Requires:	gstreamer-vorbis >= 1.20
Requires:	gstreamer-wavpack >= 1.20
Requires:	gstreamer-ximagesrc >= 1.20
Requires:	gucharmap >= 12.0.0
Requires:	nautilus-extension-brasero >= 3.12.2
# not ported to nautilus4 in GNOME 43
#Requires:	nautilus-extension-evince >= 3.38.0
Requires:	polari >= 43
Requires:	seahorse >= 43
Requires:	seahorse-gnome-shell-search >= 43
Requires:	sound-juicer >= 3.38.0
Requires:	gnote >= 43
Requires:	totem >= 43
Requires:	totem-im-status >= 43
Requires:	totem-opensubtitles >= 43
Requires:	zenity >= 3.42.0
Suggests:	%{name}-games = %{version}-%{release}
# ekiga is dead, linphone is qt-based now; what instead?
#Suggests:	ekiga >= 4.0.1
Suggests:	evolution-ews >= 3.46.0
Suggests:	pam-pam_gnome_keyring >= 42

%description desktop
GNOME Desktop Environment.

%description desktop -l pl.UTF-8
Środowisko graficzne GNOME.

%package devtools
Summary:	Developer tools for GNOME Desktop Environment
Summary(pl.UTF-8):	Narzędzia programisty dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	accerciser >= 3.40.0
Requires:	anjuta >= 1:3.34.0
Requires:	anjuta-extras >= 3.26.0
Requires:	devhelp >= 43
Requires:	glade >= 3.40.0
Requires:	gnome-devel-docs >= 40

%description devtools
Developer tools for GNOME Desktop Environment.

%description devtools -l pl.UTF-8
Narzędzia programisty dla środowiska graficznego GNOME.

%package games
Summary:	Games for GNOME Desktop Environment
Summary(pl.UTF-8):	Gry dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	aisleriot >= 3.22
Requires:	five-or-more >= 3.32
Requires:	four-in-a-row >= 3.38.0
Requires:	gnome-2048 >= 3.38.0
Requires:	gnome-chess >= 43
Requires:	gnome-games >= 1:40
Requires:	gnome-klotski >= 3.38.0
Requires:	gnome-mahjongg >= 3.38.0
Requires:	gnome-mines >= 40
Requires:	gnome-nibbles >= 3.38.0
Requires:	gnome-robots >= 40
Requires:	gnome-sudoku >= 43
Requires:	gnome-taquin >= 3.38.0
Requires:	gnome-tetravex >= 3.38.0
Requires:	hitori >= 3.38.0
Requires:	iagno >= 3.38.0
Requires:	lightsoff >= 40
Requires:	quadrapassel >= 40
Requires:	swell-foop >= 41
Requires:	tali >= 40
Obsoletes:	gnome-games-blackjack < 1:2.30
Obsoletes:	gnome-games-gataxx < 1:2.18
# gataxx -> iagno?
Obsoletes:	gnome-games-servers < 1:2.30
Obsoletes:	gnome-games-stones < 1:2.14

%description games
Games for GNOME Desktop Environment.

%description games -l pl.UTF-8
Gry dla środowiska graficznego GNOME.

%package office
Summary:	Office suite for GNOME Desktop Environment
Summary(pl.UTF-8):	Pakiety biurowe dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	abiword >= 1:3.0.5
Requires:	dia >= 1:0.97.3
Requires:	gimp >= 1:2.10.32
Requires:	glabels >= 3.4.1
Requires:	gnumeric >= 1:1.12.55
Requires:	inkscape >= 1.2

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
