%define module pyasn1

Name:		python-pyasn1
Summary:	ASN.1 tools for Python
Version:	0.6.3
Release:	1
License:	BSD-2-Clause
Group:		Development/Python
URL:		https://github.com/pyasn1/pyasn1
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%rename pyasn1

%description
This project is dedicated to implementation of ASN.1 types (concrete syntax)
and codecs (transfer syntaxes) for Python programming environment. ASN.1
compiler is planned for implementation in the future.

%files
%doc CHANGES.rst LICENSE.rst README.md TODO.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
