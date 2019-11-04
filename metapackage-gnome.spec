Summary:	GNOME Desktop Environment with additional packages
Summary(pl.UTF-8):	Środowisko graficzne GNOME z dodatkowymi pakietami
Name:		metapackage-gnome
Version:	3.34.0
Release:	3
License:	GPL/LGPL
Group:		X11/Applications
Requires:	%{name}-accessibility = %{version}-%{release}
Requires:	%{name}-admin = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-desktop = %{version}-%{release}
Requires:	%{name}-devtools = %{version}-%{release}
Requires:	%{name}-games = %{version}-%{release}
Requires:	%{name}-office = %{version}-%{release}
Requires:	banshee >= 2.6.2
Requires:	gstreamer-a52dec
Requires:	gstreamer-aac
Requires:	gstreamer-amrnb
Requires:	gstreamer-amrwb
Requires:	gstreamer-ass
Requires:	gstreamer-audio-effects-bad
Requires:	gstreamer-cdio
Requires:	gstreamer-curl
Requires:	gstreamer-dc1394
Requires:	gstreamer-dts
Requires:	gstreamer-dvdread
Requires:	gstreamer-flite
Requires:	gstreamer-gme
Requires:	gstreamer-gsm
Requires:	gstreamer-kate
Requires:	gstreamer-ladspa
Requires:	gstreamer-lv2
Requires:	gstreamer-mjpegtools
Requires:	gstreamer-mms
Requires:	gstreamer-mpeg
Requires:	gstreamer-musepack
Requires:	gstreamer-neon
Requires:	gstreamer-ofa
Requires:	gstreamer-plugins-bad
Requires:	gstreamer-plugins-ugly
Requires:	gstreamer-resindvd
Requires:	gstreamer-rtmp
Requires:	gstreamer-sid
Requires:	gstreamer-sndfile
Requires:	gstreamer-soundtouch
Requires:	gstreamer-videosink-directfb
Requires:	gstreamer-vpx
Requires:	gstreamer-x264
Requires:	gstreamer-zbar
Requires:	liferea >= 1.10.13
Requires:	shotwell
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
Requires:	at-spi2-atk >= 2.34.0
Requires:	at-spi2-core >= 2.34.0
Requires:	caribou >= 0.4.21
Requires:	dasher >= 4.11
Requires:	gnome-speech >= 0.4.23
Requires:	mousetweaks >= 3.12.0
Requires:	orca >= 3.24.0
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
Requires:	dconf >= 0.34.0
Requires:	eog >= 3.34.1
Requires:	gedit >= 3.30.2
Requires:	gnome-control-center >= 1:3.34.0
Requires:	gnome-desktop >= 3.34.0
Requires:	gnome-icon-theme >= 3.12.0
Requires:	gnome-icon-theme-symbolic >= 3.12.0
Requires:	gnome-keyring >= 3.28.0
Requires:	gnome-screensaver >= 3.6.1
Requires:	gnome-session >= 1:3.34.1
Requires:	gnome-settings-daemon >= 1:3.34.1
Requires:	gnome-shell >= 3.34.1
Requires:	gnome-terminal >= 3.30.2
Requires:	gnome-themes-standard >= 3.22.3
Requires:	gsettings-desktop-schemas >= 3.34.0
Requires:	gvfs >= 1.42.1
Requires:	mutter >= 3.34.1
Requires:	nautilus >= 3.34.1
Requires:	xdg-menus
Requires:	yelp >= 3.28.0
Suggests:	gnome-menus >= 3.32.0
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
Requires:	brasero >= 3.12.0
#Requires:	abrt-desktop >= 2.0.15
Requires:	cheese >= 3.34.0
Requires:	dconf-editor >= 3.34.2
Requires:	ekiga >= 4.0.1
Requires:	empathy >= 3.12.14
Requires:	eog-plugins >= 3.26.3
Requires:	epiphany >= 3.30.2
Requires:	evince >= 3.34.1
Requires:	evolution >= 3.34.1
Requires:	evolution-addressbook >= 3.34.1
Requires:	evolution-calendar >= 3.34.1
Requires:	evolution-mail >= 3.34.1
Requires:	file-roller >= 3.24.1
Requires:	gnome-calculator >= 3.30.1
Requires:	gdm >= 2:3.14.1
Requires:	gnome-backgrounds >= 3.30.0
Requires:	gnome-bluetooth >= 3.34.0
Requires:	gnome-color-manager >= 3.30.0
Requires:	gnome-disk-utility >= 3.24.1
Requires:	gnome-icon-theme-extras >= 3.12.0
Requires:	gnome-packagekit >= 3.24.0
Suggests:	%{name}-games = %{version}-%{release}
Requires:	gnome-nettool >= 3.8.1
Requires:	gnome-power-manager >= 3.32.0
Requires:	gnome-system-monitor >= 3.30.0
Requires:	gnome-system-tools >= 3.0.0
Requires:	gnome-tweaks >= 3.34.0
Requires:	gnome-user-docs >= 3.26.1
Requires:	gstreamer
Requires:	gstreamer-audio-effects-base
Requires:	gstreamer-audio-effects-good
Requires:	gstreamer-audio-formats
Requires:	gstreamer-audiosink-alsa
Requires:	gstreamer-cairo
Requires:	gstreamer-cdparanoia
Requires:	gstreamer-dv
Requires:	gstreamer-flac
Requires:	gstreamer-gdkpixbuf
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
Requires:	gucharmap >= 12.0.1
Requires:	nautilus-extension-brasero >= 3.12.2
Requires:	nautilus-extension-evince >= 3.34.1
# not fully ported yet
#Requires:	nautilus-extension-seahorse >= 2.30.1
Requires:	seahorse >= 3.34
# not fully ported yet
#Requires:	seahorse-plugins >= 2.30.1
Requires:	sound-juicer >= 3.24.0
Requires:	gnote >= 3.24.0
Requires:	totem >= 3.34.1
Requires:	totem-im-status >= 3.34.0
Requires:	totem-opensubtitles >= 3.34.0
Requires:	vinagre >= 3.22.0
Requires:	vino >= 3.22.0
Requires:	zenity >= 3.32.0
Suggests:	evolution-ews >= 3.34.1
Suggests:	evolution-plugin-mail-notification >= 5.4-23
Suggests:	gnome-mail-notification >= 5.4-23
Suggests:	pam-pam_gnome_keyring >= 3.34.0

%description desktop
GNOME Desktop Environment.

%description desktop -l pl.UTF-8
Środowisko graficzne GNOME.

%package devtools
Summary:	Developer tools for GNOME Desktop Environment
Summary(pl.UTF-8):	Narzędzia programisty dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	accerciser >= 3.22.0
Requires:	anjuta >= 1:3.16.0
Requires:	anjuta-extras >= 3.4.0
Requires:	devhelp >= 3.26.1
Requires:	glade >= 3.22.1
Requires:	gnome-devel-docs >= 3.22.1

%description devtools
Developer tools for GNOME Desktop Environment.

%description devtools -l pl.UTF-8
Narzędzia programisty dla środowiska graficznego GNOME.

%package games
Summary:	Games for GNOME Desktop Environment
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	aisleriot
Requires:	five-or-more
Requires:	four-in-a-row
Requires:	gnome-chess
Requires:	gnome-klotski
Requires:	gnome-mahjongg
Requires:	gnome-mines
Requires:	gnome-nibbles
Requires:	gnome-robots
Requires:	gnome-sudoku
Requires:	gnome-tetravex
Requires:	iagno
Requires:	lightsoff
Requires:	quadrapassel
Requires:	swell-foop
Requires:	tali

%description games
Games for GNOME Desktop Environment.

%package office
Summary:	Office suite for GNOME Desktop Environment
Summary(pl.UTF-8):	Pakiety biurowe dla środowiska graficznego GNOME
Group:		X11/Applications
Requires:	%{name}-core = %{version}-%{release}
Requires:	abiword >= 1:3.0.2
Requires:	dia >= 1:0.97.3
Requires:	gimp >= 1:2.10.10
Requires:	glabels >= 3.4.1
Requires:	gnumeric >= 1:1.12.45
Requires:	inkscape >= 0.92.3

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
