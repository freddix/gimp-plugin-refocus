Summary:	GIMP plug-in sharpening blurred images
Name:		gimp-plugin-refocus
Version:	0.9.0
Release:	1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/sourceforge/refocus/refocus-%{version}.tar.gz
# Source0-md5:	8d4eac4ef45c904fb5e73021696bec94
Patch0:		refocus-gimp-2.0.patch
Patch1:		refocus-gimp-preview.patch
Patch2:		refocus-mirror-fix.patch
Patch3:		refocus-link.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gimp-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		%(gimptool --gimpplugindir)/plug-ins

%description
Refocus is a plug-in for the Gimp. Frequently, when processing images,
e.g. scanning photo's or slides, images become slightly blurred.
The Refocus Gimp plug-in can be used to "refocus" such images.

%prep
%setup -qn refocus-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/refocus

