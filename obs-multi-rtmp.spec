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
BuildRequires:  vulkan-headers
BuildRequires:  glslc
BuildRequires:  glslang
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(opengl)

Requires: obs-studio

%description
OBS multi-site streaming plugin
%prep
%autosetup -n %{name}-%{version} -p1
%cmake  \
    -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
