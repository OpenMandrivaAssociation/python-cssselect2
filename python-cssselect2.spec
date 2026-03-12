%define module cssselect2

Name:	 	python-cssselect2
Version:	0.9.0
Release:	1
Summary:	CSS selectors for Python ElementTree
License:	BSD-3-Clause
Group:	 	Development/Python
URL:	 	https://pypi.org/project/cssselect2/
Source0:	https://github.com/Kozea/cssselect2/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch: noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
cssselect2 is a straightforward implementation of CSS4 Selectors for markup
documents (HTML, XML, etc.) that can be read by ElementTree-like parsers
(including cElementTree, lxml, html5lib, etc.)

Unlike cssselect, it doesn't translate selectors to XPath and thus does 
not have all the corner cases that are hard or impossible to fix in cssselect.

%files
%doc README.rst
%license LICENSE
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info
