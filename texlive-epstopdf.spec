# revision 19287
# category Package
# catalog-ctan /support/epstopdf
# catalog-date 2010-05-18 23:08:22 +0200
# catalog-license other-free
# catalog-version 2.16
Name:		texlive-epstopdf
Version:	2.16
Release:	2
Summary:	Convert EPS to 'encapsulated' PDF using GhostScript
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/epstopdf
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epstopdf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epstopdf.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-epstopdf.bin = %{EVRD}

Patch0:		texlive-epstopdf.patch

%description
Epstopdf is a Perl script that converts an EPS file to an
'encapsulated' PDF file (a single page file whose media box is
the same as the original EPS's bounding box). The resulting
file suitable for inclusion by PDFTeX as an image. The script
is adapted to run both on Windows and on Unix-alike systems.
The script makes use of Ghostscript for the actual conversion
to PDF. It assumes Ghostscript version 6.51 or later, and (by
default) suppresses its automatic rotation of pages where most
of the text is not horizontal. LaTeX users may make use of the
epstopdf package, which will run the epstopdf script "on the
fly", thus giving the illusion that PDFLaTeX is accepting EPS
graphic files.

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
%doc %{_texmfdistdir}/doc/latex/epstopdf/README
%doc %{_mandir}/man1/epstopdf.1*
%doc %{_texmfdir}/doc/man/man1/epstopdf.man1.pdf
%doc %{_mandir}/man1/repstopdf.1*
%doc %{_texmfdir}/doc/man/man1/repstopdf.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%patch0 -p1

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
