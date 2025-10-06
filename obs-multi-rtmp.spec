%global optflags %{optflags} -Wno-error -Wno-deprecated-literal-operator
%global optflags %{optflags} -Wno-error=deprecated-declarations

Summary:	OBS multi-site streaming plugin
Name:		obs-multi-rtmp
Version:	0.7.3.1
Release:	1
License:	GPLv2.0
Group:		Video
Url:		https://sorayuki.github.io/obs-multi-rtmp/
Source0:	https://github.com/sorayuki/obs-multi-rtmp/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake ninja
BuildRequires:  pkgconfig(libobs)
BuildRequires:  pkgconfig(simde)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  vulkan-headers
BuildRequires:  glslc
BuildRequires:  glslang
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(opengl)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

Requires: obs-studio

%description
OBS multi-site streaming plugin
%prep
%autosetup -n %{name}-%{version} -p1
%cmake  \
    -DENABLE_QT=ON \
    -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_libdir}/obs-plugins/obs-multi-rtmp.so
%{_datadir}/obs/obs-plugins/obs-multi-rtmp/
