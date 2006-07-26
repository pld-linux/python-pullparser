%define 	module	pullparser

Summary:	Python package providing a module for parsing HTML
Summary(pl):	Pakiet zawieraj±cy modu³ analizatora HTML
Name:		python-%{module}
Version:	0.0.5b
Release:	1
License:	Artistic
Group:		Development/Languages/Python
Source0:	http://wwwsearch.sourceforge.net/%{module}/src/%{module}-%{version}.tar.gz
# Source0-md5:	e4e238ead1d1e421cc5866c8e3f9153f
URL:		http://wwwsearch.sourceforge.net/pullparser/
Requires:	python-modules >= 2.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple "pull API" for HTML parsing, after Perl's HTML::TokeParser.
Many simple HTML parsing tasks are simpler this way than with the
HTMLParser module. pullparser.PullParser is a subclass of
HTMLParser.HTMLParser.

%description -l pl
Prosty analizator HTML, inspirowany perlowym HTML::TokeParser. Wiele
prostych zadañ zwi±zanych z przetwarzaniem HTML mo¿na nim zrobiæ
³atwiej ni¿ za pomoc± modu³u HTMLParser. pullparser.PullParser jest
podklas± HTMLParser.HTMLParser.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

rm $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog GeneralFAQ.html README.html
%{py_sitescriptdir}/*.py[co]
