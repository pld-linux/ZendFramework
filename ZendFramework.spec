# TODO
# - Components to subpackages
%include	/usr/lib/rpm/macros.php
Summary:	Zend Framework
Summary(pl.UTF-8):	Szkielet Zend
Name:		ZendFramework
Version:	1.5.2
Release:	1.6
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://framework.zend.com/releases/%{name}-%{version}/ZendFramework-%{version}.tar.gz
# Source0-md5:	f2c3d4e6aea6136645d20979cc94bf5b
URL:		http://framework.zend.com/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 4:5.1.4
Requires:	php-ctype
Requires:	php-hash
Requires:	php-iconv
Requires:	php-pcre
Requires:	php-pdo
Requires:	php-pdo-mysql
Obsoletes:	ZendFramework-doc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package demos
Summary:	Demos for Zend Framework
Summary(pl.UTF-8):	Programy demonstracyjne dla szkieletu Zend Framework
Group:		Documentation

%description demos
Demos for Zend Framework.

%description demos -l pl.UTF-8
Programy demonstracyjne dla szkieletu Zend Framework.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{php_pear_dir}}
cp -a demos/Zend/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# library should be in include_path if used, so we use already defined %{php_pear_dir}
cp -a library/* $RPM_BUILD_ROOT%{php_pear_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt
%{php_pear_dir}

%files demos
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
