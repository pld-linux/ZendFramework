Summary:	Zend Framework
Summary(pl):	Szkielet Zend
Name:		ZendFramework
Version:	0.1.3
Release:	0.1
License:	Zend Framework License, 1.0, (distributable, see LICENSE)
Group:		Development/Languages/PHP
Source0:	http://framework.zend.com/releases/%{name}-%{version}.tar.gz
# Source0-md5:	3adef29f62bb8f3c536b81e56d65fd86
URL:		http://framework.zend.com/
Requires:	php-common >= 4:5.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
Zend Framework is a high quality and open source framework for
developing Web Applications and Web Services.

Built in the true PHP spirit, the Zend Framework delivers ease-of-use
and powerful functionality. It provides solutions for building modern,
robust, and secure websites.

%description -l pl
Zend Framework to maj�cy otwarte �r�d�a, wysokiej jako�ci szkielet do
tworzenia aplikacji i us�ug WWW.

Stworzony w prawdziwym duchu PHP szkielet Zend dostarcza �atw� w
u�yciu i pot�n� funkcjonalno��. Udost�pnia rozwi�zania do tworzenia
nowoczesnych, bogatych i bezpiecznych serwis�w WWW.

%package doc
Summary:	Documentation for Zend Framework
Summary(pl):	Dokumentacja dla Szkieletu Zend
Group:		Documentation

%description doc
Documentation for Zend Framework.

%description doc -l pl
Dokumentacja dla Szkieletu Zend.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_appdir}}
cp -a demos/Zend/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# library should be in include_path if used
cp -a library $RPM_BUILD_ROOT%{_appdir}

# The /incubator directory contains recent contributions that may
# eventually be moved to the /library directory.  These are considered
# highly unstable.
cp -a incubator $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt NEWS.txt
%{_appdir}
%{_examplesdir}/%{name}-%{version}

%files doc
%defattr(644,root,root,755)
%doc documentation/*
