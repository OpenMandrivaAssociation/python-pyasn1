Name: pyasn1
Summary: ASN.1 tools for Python
Version: 0.0.11a
Release: %mkrel 1
License: BSD
Group: Development/Python
Source0: http://downloads.sourceforge.net/pyasn1/pyasn1-%{version}.tar.gz
URL: http://pyasn1.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(id -u -n)
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
rm -rf %{buildroot}
python ./setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES LICENSE README TODO
%{python_sitelib}/pyasn1
%{python_sitelib}/*.egg-info
