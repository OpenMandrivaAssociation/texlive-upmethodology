Name:		texlive-upmethodology
Version:	20171212
Release:	1
Summary:	Writing specifications such as for UP-based methodologies
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/upmethodology
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/upmethodology.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/upmethodology.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle allows the user to create Unified Process
methodology (UP or RUP) based documents. The style provides
document versioning, document history, document authors,
document validators, specification description, task
management, and several helping macros.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/upmethodology
%doc %{_texmfdistdir}/doc/latex/upmethodology

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
