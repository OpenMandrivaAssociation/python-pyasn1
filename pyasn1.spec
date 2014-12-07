Summary:	ASN.1 tools for Python
Name:		pyasn1
Version:	0.1.6
Release:	8
License:	BSD
Group:		Development/Python
Url:		http://pyasn1.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pyasn1/pyasn1-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)

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
%doc CHANGES LICENSE README TODO
%{python_sitelib}/pyasn1
%{python_sitelib}/*.egg-info

