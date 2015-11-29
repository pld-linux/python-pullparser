%define 	module	pullparser

Summary:	Python package providing a module for parsing HTML
Summary(pl.UTF-8):	Pakiet zawierający moduł analizatora HTML
Name:		python-%{module}
Version:	0.0.5b
Release:	4
License:	Artistic
Group:		Development/Languages/Python
Source0:	http://wwwsearch.sourceforge.net/%{module}/src/%{module}-%{version}.tar.gz
# Source0-md5:	e4e238ead1d1e421cc5866c8e3f9153f
URL:		http://wwwsearch.sourceforge.net/pullparser/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python-modules >= 2.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple "pull API" for HTML parsing, after Perl's HTML::TokeParser.
Many simple HTML parsing tasks are simpler this way than with the
HTMLParser module. pullparser.PullParser is a subclass of
HTMLParser.HTMLParser.

%description -l pl.UTF-8
Prosty analizator HTML, inspirowany perlowym HTML::TokeParser. Wiele
prostych zadań związanych z przetwarzaniem HTML można nim zrobić
łatwiej niż za pomocą modułu HTMLParser. pullparser.PullParser jest
podklasą HTMLParser.HTMLParser.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

rm $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog GeneralFAQ.html README.html
%{py_sitescriptdir}/*.py[co]
