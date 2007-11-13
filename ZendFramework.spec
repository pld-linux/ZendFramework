Summary:	Zend Framework
Summary(pl.UTF-8):	Szkielet Zend
Name:		ZendFramework
Version:	1.0.2
Release:	1
License:	Zend Framework License, 1.0, (distributable, see LICENSE)
Group:		Development/Languages/PHP
Source0:	http://framework.zend.com/releases/ZendFramework-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	15066ea33600df509c1ba6a5924688a7
URL:		http://framework.zend.com/
Requires:	php-common >= 4:5.1.4
Obsoletes:	ZendFramework-doc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
Zend Framework is a high quality and open source framework for
developing Web Applications and Web Services.

Built in the true PHP spirit, the Zend Framework delivers ease-of-use
and powerful functionality. It provides solutions for building modern,
robust, and secure websites.

%description -l pl.UTF-8
Zend Framework to mający otwarte źródła, wysokiej jakości szkielet do
tworzenia aplikacji i usług WWW.

Stworzony w prawdziwym duchu PHP szkielet Zend dostarcza łatwą w
użyciu i potężną funkcjonalność. Udostępnia rozwiązania do tworzenia
nowoczesnych, bogatych i bezpiecznych serwisów WWW.

%package doc
Summary:	Documentation for Zend Framework
Summary(pl.UTF-8):	Dokumentacja dla Szkieletu Zend
Group:		Documentation

%description doc
Documentation for Zend Framework.

%description doc -l pl.UTF-8
Dokumentacja dla Szkieletu Zend.

%package demos
Summary:	Demos for Zend Framework
Group:		Documentation

%description demos
Demos for Zend Framework.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_appdir}}
cp -a demos/Zend/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# library should be in include_path if used
cp -a library $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt NEWS.txt
%{_appdir}

%files demos
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
