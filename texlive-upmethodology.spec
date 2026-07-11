%global tl_name upmethodology
%global tl_revision 78632

Name:		texlive-%{tl_name}
Epoch:		1
Version:	20260406
Release:	%{tl_revision}.1
Summary:	Writing specifications such as for UP-based methodologies
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/upmethodology
License:	lgpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/upmethodology.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/upmethodology.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle allows the user to create Unified Process methodology (UP or
RUP) based documents. The style provides document versioning, document
history, document authors, document validators, specification
description, task management, and several helping macros.

