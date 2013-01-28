Name: pyasn1
Summary: ASN.1 tools for Python
Version: 0.1.6
Release: 1
License: BSD
Group: Development/Python
Source0: http://downloads.sourceforge.net/pyasn1/pyasn1-%{version}.tar.gz
URL: http://pyasn1.sourceforge.net/
BuildRequires: python-devel
BuildArch: noarch

%description
This project is dedicated to implementation of ASN.1 types (concrete syntax)
and codecs (transfer syntaxes) for Python programming environment. ASN.1
compiler is planned for implementation in the future.


%prep
%setup -q

%build
python ./setup.py build

%install
python ./setup.py install --root=%{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES LICENSE README TODO
%{python_sitelib}/pyasn1
%{python_sitelib}/*.egg-info


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.11a-2mdv2011.0
+ Revision: 667903
- mass rebuild

* Sun Oct 31 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.0.11a-1mdv2011.0
+ Revision: 590921
- update to 0.0.11a
- drop the obsolete %%py_requires macro

* Sun Jan 03 2010 Frederik Himpe <fhimpe@mandriva.org> 0.0.10a-1mdv2010.1
+ Revision: 485754
- update to new version 0.0.10a

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.0.6a-6mdv2010.0
+ Revision: 441980
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.0.6a-5mdv2009.1
+ Revision: 325867
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.0.6a-4mdv2009.0
+ Revision: 259394
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.0.6a-3mdv2009.0
+ Revision: 247254
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.0.6a-1mdv2008.1
+ Revision: 136445
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 28 2007 Andreas Hasenack <andreas@mandriva.com> 0.0.6a-1mdv2008.0
+ Revision: 31989
- fixed (build)requires
- Import pyasn1

