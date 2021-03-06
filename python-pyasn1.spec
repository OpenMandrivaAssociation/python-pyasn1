Summary:	ASN.1 tools for Python
Name:		python-pyasn1
Version:	0.4.8
Release:	1
License:	BSD
Group:		Development/Python
Url:		http://pyasn1.sourceforge.net/
Source0:	https://files.pythonhosted.org/packages/a4/db/fffec68299e6d7bad3d504147f9094830b704527a7fc098b721d38cc7fa7/pyasn1-0.4.8.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
%rename pyasn1

%description
This project is dedicated to implementation of ASN.1 types (concrete syntax)
and codecs (transfer syntaxes) for Python programming environment. ASN.1
compiler is planned for implementation in the future.

%package -n python2-pyasn1
Summary:	ASN.1 tools for Python 2.x
Group:		Development/Python
BuildRequires:	python2-setuptools
BuildRequires:	pkgconfig(python2)

%description -n python2-pyasn1
This project is dedicated to implementation of ASN.1 types (concrete syntax)
and codecs (transfer syntaxes) for Python programming environment. ASN.1
compiler is planned for implementation in the future.

%prep
%setup -qn pyasn1-%{version}
mkdir py2
cp -a `ls |grep -v py2` py2/

%build
cd py2
python2 setup.py build

cd ..
python ./setup.py build

%install
cd py2
python2 setup.py install --root=%{buildroot}

cd ..
python ./setup.py install --root=%{buildroot}

%files
%doc CHANGES.rst LICENSE.rst README.md TODO.rst
%{python_sitelib}/pyasn1
%{python_sitelib}/*.egg-info

%files -n python2-pyasn1
%{python2_sitelib}/pyasn1
%{python2_sitelib}/*.egg-info
