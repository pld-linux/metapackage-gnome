Summary:	GNOME Desktop Suite
Summary(pl):	¦rodowisko graficzne GNOME
Name:		metapackage-gnome
Version:	2.8
Release:	1
License:	GPL
Group:		X11/Applications/Desktop
Requires:	gnome-desktop >= 2.8
Requires:	gnome-session >= 2.8
Requires:	gnome-terminal >= 2.8
Requires:	nautilus >= 2.8
Requires:	hal >= 0.4.0
Requires:	xscreensaver-gnome2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Desktop suite metapackage.

%description -l pl
Metapakiet ¶rodowiska graficznego GNOME.

%files
