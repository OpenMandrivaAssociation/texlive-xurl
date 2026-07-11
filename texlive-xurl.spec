%global tl_name xurl
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.10
Release:	%{tl_revision}.1
Summary:	Allow URL breaks at any alphanumerical character
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xurl
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xurl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xurl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package loads url by default and defines possible URL breaks for
all alphanumerical characters, as well as = / . : * - ~ ' " All
arguments which are valid for url can be used and will be passed on to
this package. For more information read the documentation of url itself.

