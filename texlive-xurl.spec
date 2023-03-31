Name:		texlive-xurl
Version:	61553
Release:	2
Summary:	Allow URL breaks at any alphanumerical character
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xurl
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xurl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xurl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package loads url by default and defines possible URL
breaks for all alphanumerical characters, as well as = / . : *
- ~ ' " All arguments which are valid for url can be used and
will be passed on to this package. For more information read
the documentation of url itself.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/xurl
%doc %{_texmfdistdir}/doc/latex/xurl

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
