Summary:	ASN.1 tools for Python
Name:		python-pyasn1
Version:	0.6.1
Release:	1
License:	BSD
Group:		Development/Python
Url:		https://pyasn1.sourceforge.net/
Source0:	https://files.pythonhosted.org/packages/source/p/pyasn1/pyasn1-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
%rename pyasn1

%description
This project is dedicated to implementation of ASN.1 types (concrete syntax)
and codecs (transfer syntaxes) for Python programming environment. ASN.1
compiler is planned for implementation in the future.

%files
%doc CHANGES.rst LICENSE.rst README.md TODO.rst
%{python_sitelib}/pyasn1
%{python_sitelib}/pyasn1-%{version}.dist-info
