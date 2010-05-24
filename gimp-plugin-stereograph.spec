Summary:	Stereograph GIMP plug-in
Summary(pl.UTF-8):	Wtyczka do tworzenia stereogramów dla GIMP-a
Name:		gimp-plugin-stereograph
Version:	1.5
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://trific.ath.cx/Ftp//gimp/stereograph/stereograph-gimp-%{version}.tar.bz2
# Source0-md5:	22c6b3924823de3153b4b7c13d51e2d2
URL:		http://trific.ath.cx/software/gimp-plugins/stereograph/
BuildRequires:	gimp-devel >= 1:2.2.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	pkgconfig
Requires:	gimp >= 1:2.2.0
Requires:	gtk+2 >= 2:2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define		gimpplugindir	%(gimptool --gimpplugindir)/plug-ins

%description
This is a GIMP plug-in interface to the Stereograph, a high quality
Single Image Stereogram (SIS) generator by Fabian Januszewski.

%description -l pl.UTF-8
To jest wtyczka do GIMP-a używająca interfejsu programu Stereograph,
generatora wysokiej jakości pojedynczych obrazów stereogramowych (SIS)
Fabiana Januszewskiego.

%prep
%setup -q -n stereograph-gimp-%{version}

%build
%{__make} \
		CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{gimpplugindir}
install stereograph $RPM_BUILD_ROOT%{gimpplugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README README.hacking
%attr(755,root,root) %{gimpplugindir}/stereograph
