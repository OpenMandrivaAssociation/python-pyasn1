Summary:	ASN.1 tools for Python
Name:		python-pyasn1
Version:	0.4.8
Release:	2
License:	BSD
Group:		Development/Python
Url:		http://pyasn1.sourceforge.net/
Source0:	https://files.pythonhosted.org/packages/a4/db/fffec68299e6d7bad3d504147f9094830b704527a7fc098b721d38cc7fa7/pyasn1-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
%rename pyasn1

%description
This project is dedicated to implementation of ASN.1 types (concrete syntax)
and codecs (transfer syntaxes) for Python programming environment. ASN.1
compiler is planned for implementation in the future.

%prep
%autosetup -n pyasn1-%{version}

%build
%py_build

%install
%py_install

%files
%doc CHANGES.rst LICENSE.rst README.md TODO.rst
%{python_sitelib}/pyasn1
%{python_sitelib}/*.egg-info
