
%define		theme	kstatus
%define		fileid	19827

Summary:	superkaramba - kstatus theme
Summary(pl):	superkaramba - motyw kstatus
Name:		superkaramba-theme-%{theme}
Version:	1.1
Release:	0.1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/%{fileid}-%{theme}-%{version}.tar.gz
# Source0-md5:	7c516813edfbcb93178a1316e8d11ea7
URL:		http://karraskal.deviantart.com/
Requires:	superkaramba >= 0.36
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define 	_kstatusdir 	/themes/superkaramba/kstatus

%description
kstatus theme for superkaramba. Features :
 - User@hostname Output
 - Kernel Version Output
 - KDE Version Output
 - CPU Usage Stats with progress bar indicator
 - CPU Model / Clockspeed / Cache Detection
 - RAM / Swapfile Usage with progress bar indicator
 - Hard Disk Drive Monitor (default 4 partitions)
 - Network Traffic Monitor
 - IP Address Output
 - Uptime / Time / Date Output
 - XMMS - Currently Playing and Time of Track Information
 - XMMS Controls - Skip back, Play, Stop, Pause and Skip Forward

%description -l pl
Motyw kstatus dla superkaramby. Wy¶wietlane informacje :
 - User@hostname
 - Wersja kernela
 - Wersja KDE
 - Obci±¿enie procesora
 - Model / zegar / cache procesora
 - Obci±¿enie pamiêci RAM i pliku wymiany
 - Monitor dysków
 - Monitor sieci
 - Uptime, czas, data
 - XMMS - info o odtwarzanej ¶cie¿ce
 - Kontrolki XMMS

%prep
%setup -q -n %{theme}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}%{_kstatusdir}
cp -r * $RPM_BUILD_ROOT%{_datadir}%{_kstatusdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%{_datadir}%{_kstatusdir}/
