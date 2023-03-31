%define	module	cssselect2

Summary: Library for parsing CSS3 selectors and translating them to XPath 1.0
Name:	 python-%{module}
Version: 0.2.1
Release: 4
Source0: https://github.com/Kozea/cssselect2/%{module}-%{version}.tar.gz
License: BSD
Group:	 Development/Python
Url:	 https://pypi.org/project/cssselect2/
BuildArch: noarch
BuildRequires:	python-setuptools

%description
cssselect2 is a straightforward implementation of CSS3 Selectors for markup 
documents (HTML, XML, etc.) that can be read by ElementTree-like parsers 
such as cElementTree, lxml, html5lib, etc.
Unlike cssselect, it doesn't translate selectors to XPath and thus does 
not have all the corner cases that are hard or impossible to fix in cssselect.


%prep
%setup -q -n %{module}-%{version}


%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

#pushd %pydir
%__python setup.py install --root=%{buildroot}

%files
%doc CHANGES LICENSE README.rst
%{py_puresitedir}/%{module}*

