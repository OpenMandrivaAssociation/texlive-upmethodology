# revision 33091
# category Package
# catalog-ctan /macros/latex/contrib/upmethodology
# catalog-date 2014-03-03 17:31:22 +0100
# catalog-license lgpl
# catalog-version undef
Name:		texlive-upmethodology
Version:	20140303
Release:	5
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
%{_texmfdistdir}/tex/latex/upmethodology/UPMVERSION.def
%{_texmfdistdir}/tex/latex/upmethodology/upmethodology-backpage.sty
%{_texmfdistdir}/tex/latex/upmethodology/upmethodology-code.sty
%{_texmfdistdir}/tex/latex/upmethodology/upmethodology-document.cls
%{_texmfdistdir}/tex/latex/upmethodology/upmethodology-document.sty
%{_texmfdistdir}/tex/latex/upmethodology/upmethodology-extension.sty
%{_texmfdistdir}/tex/latex/upmethodology/upmethodology-fmt.sty
%{_texmfdistdir}/tex/latex/upmethodology/upmethodology-frontpage.sty
%{_texmfdistdir}/tex/latex/upmethodology/upmethodology-p-common.sty
%{_texmfdistdir}/tex/latex/upmethodology/upmethodology-spec.sty
%{_texmfdistdir}/tex/latex/upmethodology/upmethodology-task.sty
%{_texmfdistdir}/tex/latex/upmethodology/upmethodology-version.sty
%doc %{_texmfdistdir}/doc/latex/upmethodology/AUTHORS
%doc %{_texmfdistdir}/doc/latex/upmethodology/COPYING
%doc %{_texmfdistdir}/doc/latex/upmethodology/Changelog
%doc %{_texmfdistdir}/doc/latex/upmethodology/README
%doc %{_texmfdistdir}/doc/latex/upmethodology/README.textile
%doc %{_texmfdistdir}/doc/latex/upmethodology/VERSION
%doc %{_texmfdistdir}/doc/latex/upmethodology/arakhne_org_logo.jpg
%doc %{_texmfdistdir}/doc/latex/upmethodology/caution.png
%doc %{_texmfdistdir}/doc/latex/upmethodology/figure_and_tex.pdf
%doc %{_texmfdistdir}/doc/latex/upmethodology/figure_and_tex.pdftex_t
%doc %{_texmfdistdir}/doc/latex/upmethodology/frontclassic.jpg
%doc %{_texmfdistdir}/doc/latex/upmethodology/frontmodern.jpg
%doc %{_texmfdistdir}/doc/latex/upmethodology/illustration.jpg
%doc %{_texmfdistdir}/doc/latex/upmethodology/info.png
%doc %{_texmfdistdir}/doc/latex/upmethodology/question.png
%doc %{_texmfdistdir}/doc/latex/upmethodology/upmethodology-doc.pdf
%doc %{_texmfdistdir}/doc/latex/upmethodology/upmethodology-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
