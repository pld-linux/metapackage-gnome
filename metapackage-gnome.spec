Summary:	GNOME Desktop Environment with additional packages
Summary(pl.UTF-8):	Środowisko graficzne GNOME z dodatkowymi pakietami
Name:		metapackage-gnome
Version:	3.38.0
Release:	2
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
Requires:	gnome-tour >= 3.38.0
Requires:	rhythmbox >= 3.4.4
Requires:	gstreamer-a52dec >= 1.16
Requires:	gstreamer-aac >= 1.16
Requires:	gstreamer-amrnb >= 1.16
Requires:	gstreamer-amrwb >= 1.16
Requires:	gstreamer-ass >= 1.16
Requires:	gstreamer-audio-effects-bad >= 1.16
Requires:	gstreamer-cdio >= 1.16
Requires:	gstreamer-curl >= 1.16
Requires:	gstreamer-dc1394 >= 1.16
Requires:	gstreamer-dts >= 1.16
Requires:	gstreamer-dvdread >= 1.16
Requires:	gstreamer-flite >= 1.16
Requires:	gstreamer-gme >= 1.16
Requires:	gstreamer-gsm >= 1.16
Requires:	gstreamer-kate >= 1.16
Requires:	gstreamer-ladspa >= 1.16
Requires:	gstreamer-lv2 >= 1.16
Requires:	gstreamer-mjpegtools >= 1.16
Requires:	gstreamer-mms >= 1.16
Requires:	gstreamer-mpeg >= 1.16
Requires:	gstreamer-musepack >= 1.16
Requires:	gstreamer-neon >= 1.16
Requires:	gstreamer-ofa >= 1.16
Requires:	gstreamer-plugins-bad >= 1.16
Requires:	gstreamer-plugins-ugly >= 1.16
Requires:	gstreamer-resindvd >= 1.16
Requires:	gstreamer-rtmp >= 1.16
Requires:	gstreamer-sid >= 1.16
Requires:	gstreamer-sndfile >= 1.16
Requires:	gstreamer-soundtouch >= 1.16
Requires:	gstreamer-videosink-directfb >= 1.16
Requires:	gstreamer-vpx >= 1.16
Requires:	gstreamer-x264 >= 1.16
Requires:	gstreamer-zbar >= 1.16
Requires:	shotwell >= 0.30
Suggests:	tracker >= 2.3
Suggests:	tracker3 >= 3.0
Obsoletes:	metapackage-gnome-extras
Obsoletes:	gnome
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
Requires:	at-spi2-atk >= 2.38.0
Requires:	at-spi2-core >= 2.38.0
Requires:	mousetweaks >= 3.32.0
Requires:	orca >= 3.38.0
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
Requires:	gnome-initial-setup >= 3.38.0
Requires:	gnome-software >= 3.38.0

%description admin
Administration packages for GNOME Desktop Environment.

%description admin -l pl.UTF-8
Pakiety do zarządzania środowiskiem graficznym GNOME.

%package core
Summary:	The core components of the GNOME Desktop Environment
Summary(pl.UTF-8):	Podstawowe składniki środowiska graficznego GNOME
Group:		X11/Applications
Requires:	PackageKit-gtk3-module
Requires:	adwaita-icon-theme >= 3.38.0
Requires:	dconf >= 0.38.0
Requires:	eog >= 3.38.0
Requires:	gedit >= 3.38.0
Requires:	gnome-control-center >= 1:3.38.0
Requires:	gnome-desktop >= 3.38.0
Requires:	gnome-keyring >= 3.36.0
Requires:	gnome-session >= 1:3.38.0
Requires:	gnome-settings-daemon >= 1:3.38.0
Requires:	gnome-shell >= 3.38.0
Requires:	gnome-terminal >= 3.38.0
Requires:	gsettings-desktop-schemas >= 3.38.0
Requires:	gvfs >= 1.46.0
Requires:	mutter >= 3.38.0
Requires:	nautilus >= 3.38.0
Requires:	xdg-menus
Requires:	yelp >= 3.38.0
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
Requires:	NetworkManager >= 2:1.26.0
Requires:	brasero >= 3.12.0
#Requires:	abrt-desktop >= 2.14.0
Requires:	cheese >= 3.38.0
Requires:	dconf-editor >= 3.38.0
Requires:	eog-plugins >= 3.26.3
Requires:	epiphany >= 3.34.0
Requires:	evince >= 3.38.0
Requires:	evolution >= 3.38.0
Requires:	evolution-addressbook >= 3.38.0
Requires:	evolution-calendar >= 3.38.0
Requires:	evolution-mail >= 3.38.0
Requires:	file-roller >= 3.38.0
Requires:	gnome-calculator >= 3.38.0
Requires:	gnome-calendar >= 3.38.0
Requires:	gdm >= 2:3.38.0
Requires:	gnome-backgrounds >= 3.38.0
Requires:	gnome-bluetooth >= 3.34.0
Requires:	gnome-color-manager >= 3.36.0
Requires:	gnome-connections >= 3.38.0
Requires:	gnome-disk-utility >= 3.38.0
Requires:	gnome-packagekit >= 3.32.0
Requires:	gnome-power-manager >= 3.32.0
Requires:	gnome-remote-desktop >= 0.1
Requires:	gnome-system-monitor >= 3.38.0
Requires:	gnome-tweaks >= 3.34.0
Requires:	gnome-user-docs >= 3.38.0
Requires:	gstreamer >= 1.16
Requires:	gstreamer-audio-effects-base >= 1.16
Requires:	gstreamer-audio-effects-good >= 1.16
Requires:	gstreamer-audio-formats >= 1.16
Requires:	gstreamer-audiosink-alsa >= 1.16
Requires:	gstreamer-cairo >= 1.16
Requires:	gstreamer-cdparanoia >= 1.16
Requires:	gstreamer-dv >= 1.16
Requires:	gstreamer-flac >= 1.16
Requires:	gstreamer-gdkpixbuf >= 1.16
Requires:	gstreamer-imagesink-x >= 1.16
Requires:	gstreamer-imagesink-xv >= 1.16
Requires:	gstreamer-jack >= 1.16
Requires:	gstreamer-libpng >= 1.16
Requires:	gstreamer-libvisual >= 1.16
Requires:	gstreamer-pango >= 1.16
Requires:	gstreamer-plugins-base >= 1.16
Requires:	gstreamer-plugins-good >= 1.16
Requires:	gstreamer-pulseaudio >= 1.16
Requires:	gstreamer-raw1394 >= 1.16
Requires:	gstreamer-shout2 >= 1.16
Requires:	gstreamer-soup >= 1.16
Requires:	gstreamer-speex >= 1.16
Requires:	gstreamer-taglib >= 1.16
Requires:	gstreamer-theora >= 1.16
Requires:	gstreamer-v4l2 >= 1.16
Requires:	gstreamer-video-effects >= 1.16
Requires:	gstreamer-videosink-aa >= 1.16
Requires:	gstreamer-videosink-libcaca >= 1.16
Requires:	gstreamer-visualisation >= 1.16
Requires:	gstreamer-vorbis >= 1.16
Requires:	gstreamer-wavpack >= 1.16
Requires:	gstreamer-ximagesrc >= 1.16
Requires:	gucharmap >= 12.0.0
Requires:	nautilus-extension-brasero >= 3.12.2
Requires:	nautilus-extension-evince >= 3.38.0
Requires:	polari >= 3.38.0
Requires:	seahorse >= 3.38.0
Requires:	seahorse-gnome-shell-search >= 3.38.0
Requires:	sound-juicer >= 3.38.0
Requires:	gnote >= 3.38.0
Requires:	totem >= 3.38.0
Requires:	totem-im-status >= 3.38.0
Requires:	totem-opensubtitles >= 3.38.0
Requires:	zenity >= 3.32.0
Suggests:	%{name}-games = %{version}-%{release}
# or linphone?
Suggests:	ekiga >= 4.0.1
Suggests:	evolution-ews >= 3.38.0
Suggests:	pam-pam_gnome_keyring >= 3.36.0

%description desktop
GNOME Desktop Environment.

%description desktop -l pl.UTF-8
Środowisko graficzne GNOME.

%package devtools
Summary:	Developer tools for GNOME Desktop Environment
Summary(pl.UTF-8):	Narzędzia programisty dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	accerciser >= 3.38.0
Requires:	anjuta >= 1:3.34.0
Requires:	anjuta-extras >= 3.26.0
Requires:	devhelp >= 3.38.0
Requires:	glade >= 3.28.0
Requires:	gnome-devel-docs >= 3.38.0

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
Requires:	gnome-chess >= 3.38.0
Requires:	gnome-games >= 1:3.38.0
Requires:	gnome-klotski >= 3.38.0
Requires:	gnome-mahjongg >= 3.38.0
Requires:	gnome-mines >= 3.36.0
Requires:	gnome-nibbles >= 3.38.0
Requires:	gnome-robots >= 3.38.0
Requires:	gnome-sudoku >= 3.38.0
Requires:	gnome-taquin >= 3.38.0
Requires:	gnome-tetravex >= 3.38.0
Requires:	hitori >= 3.38.0
Requires:	iagno >= 3.38.0
Requires:	lightsoff >= 3.38.0
Requires:	quadrapassel >= 3.38.0
Requires:	swell-foop >= 3.34
Requires:	tali >= 3.38.0
Obsoletes:	gnome-games-blackjack
Obsoletes:	gnome-games-gataxx
# gataxx -> iagno?
Obsoletes:	gnome-games-servers
Obsoletes:	gnome-games-stones

%description games
Games for GNOME Desktop Environment.

%description games -l pl.UTF-8
Gry dla środowiska graficznego GNOME.

%package office
Summary:	Office suite for GNOME Desktop Environment
Summary(pl.UTF-8):	Pakiety biurowe dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	abiword >= 1:3.0.2
Requires:	dia >= 1:0.97.3
Requires:	gimp >= 1:2.10.20
Requires:	glabels >= 3.4.1
Requires:	gnumeric >= 1:1.12.48
Requires:	inkscape >= 1.0

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
