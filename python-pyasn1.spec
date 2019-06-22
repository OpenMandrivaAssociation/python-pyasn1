Summary:	ASN.1 tools for Python
Name:		python-pyasn1
Version:	0.4.5
Release:	2
License:	BSD
Group:		Development/Python
Url:		http://pyasn1.sourceforge.net/
Source0:	https://files.pythonhosted.org/packages/46/60/b7e32f6ff481b8a1f6c8f02b0fd9b693d1c92ddd2efb038ec050d99a7245/pyasn1-0.4.5.tar.gz
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
