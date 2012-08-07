# revision 26577
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-epstopdf
Version:	20120807
Release:	1
Summary:	TeXLive epstopdf package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epstopdf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epstopdf.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-epstopdf.bin = %{EVRD}

%description
TeXLive epstopdf package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/epstopdf
%{_bindir}/repstopdf
%{_texmfdistdir}/scripts/epstopdf/epstopdf.pl
%doc %{_texmfdistdir}/doc/support/epstopdf/README
%doc %{_mandir}/man1/epstopdf.1*
%doc %{_texmfdir}/doc/man/man1/epstopdf.man1.pdf
%doc %{_mandir}/man1/repstopdf.1*
%doc %{_texmfdir}/doc/man/man1/repstopdf.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/epstopdf/epstopdf.pl epstopdf
    ln -sf epstopdf repstopdf
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
