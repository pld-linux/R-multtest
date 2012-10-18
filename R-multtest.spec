%define		packname	multtest

Summary:	Multiple hypothesis testing library from Bioconductor
Name:		R-%{packname}
Version:	2.14.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	2cbfe12636fc0865e8fc3fe56272fa5f
URL:		http://www.bioconductor.org/packages/release/bioc/html/multtest.html
BuildRequires:	R-Biobase
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R-Biobase
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Non-parametric bootstrap and permutation resampling-based multiple
testing procedures for controlling the family-wise error rate (FWER),
generalized family-wise error rate (gFWER), tail probability of the
proportion of false positives (TPPFP), and false discovery rate (FDR).
Single-step and step-wise methods are implemented. Tests based on a
variety of t- and F-statistics (including t-statistics based on
regression parameters from linear and survival models) are included.
Results are reported in terms of adjusted p-values, confindence
regions and test statistic cutoffs. The procedures are directly
applicable to identifying differentially expressed genes in DNA
microarray experiments.

This Library is a part of the Bioconductor (bioconductor.org) proejct.

%prep
%setup -c -q -n %{packname}

%{__sed} -i -e 's/\r$//'  %{packname}/inst/doc/multtest.bib
%{__sed} -i -e 's/\r$//'  %{packname}/inst/doc/MTP.tex
#%{__sed} -i -e 's/\r$//'  %{packname}/inst/doc/Rplots.ps

%build
R CMD build %{packname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/otherDocs
