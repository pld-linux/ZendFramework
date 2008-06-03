# TODO
# - Components to subpackages
%include	/usr/lib/rpm/macros.php
Summary:	Zend Framework
Summary(pl.UTF-8):	Szkielet Zend
Name:		ZendFramework
Version:	1.5.2
Release:	1.11
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

%package Zend_Acl
Summary:	Zend_Acl
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/en/zend.acl.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Acl
Zend_Acl provides lightweight and flexible access control list (ACL)
functionality and privileges management. In general, an application
may utilize such functionality to control access to certain protected
objects by other requesting objects.

%package Zend_Auth
Summary:	Zend_Auth
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/en/zend.auth.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Auth
Zend_Auth provides an API for authentication and includes concrete
authentication adapters for common use case scenarios.

%package Zend_Cache
Summary:	Zend_Cache
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/en/zend.cache.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Cache
Zend_Cache provides a generic way to cache any data.

%package Zend_Config
Summary:	Zend_Config
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/en/zend.config.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Config
Zend_Config is designed to simplify access to and use of configuration
data within applications.

%package Zend_Console_Getopt
Summary:	Zend_Console_Getopt
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/en/zend.console.getopt.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Console_Getopt
The Zend_Console_Getopt class helps command-line applications to parse
their options and arguments.

%package Zend_Controller
Summary:	Zend_Controller
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/en/zend.controller.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Controller
Zend_Controller is the heart of Zend Framework's MVC system. MVC
stands for Model-View-Controller and is a design pattern targeted at
separating application logic from display logic.

%package Zend_Currency
Summary:	Zend_Currency
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/en/zend.currency.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Currency
Zend_Currency is part of the I18N core of the Zend_Framework. It
handles all issues related to currency, money representation and
formating. And it also provides additional informational methods which
include localized informations on currencies, informations about which
currency is used in which region and more.

%package Zend_Date
Summary:	Zend_Date
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Date
Zend_Date

%package Zend_Db
Summary:	Zend_Db
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Db
Zend_Db

%package Zend_Debug
Summary:	Zend_Debug
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Debug
Zend_Debug

%package Zend_Exception
Summary:	Zend_Exception
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Exception
Zend_Exception

%package Zend_Feed
Summary:	Zend_Feed
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Feed
Zend_Feed

%package Zend_Filter
Summary:	Zend_Filter
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Filter
Zend_Filter

%package Zend_Filter_Input
Summary:	Zend_Filter_Input
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Filter_Input
Zend_Filter_Input

%package Zend_Form
Summary:	Zend_Form
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Form
Zend_Form

%package Zend_Gdata
Summary:	Zend_Gdata
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Gdata
Zend_Gdata

%package Zend_Http
Summary:	Zend_Http
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Http
Zend_Http

%package Zend_InfoCard
Summary:	Zend_InfoCard
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_InfoCard
Zend_InfoCard

%package Zend_Json
Summary:	Zend_Json
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Json
Zend_Json

%package Zend_Layout
Summary:	Zend_Layout
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Layout
Zend_Layout

%package Zend_Ldap
Summary:	Zend_Ldap
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Ldap
Zend_Ldap

%package Zend_Loader
Summary:	Zend_Loader
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Loader
Zend_Loader

%package Zend_Locale
Summary:	Zend_Locale
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Locale
Zend_Locale

%package Zend_Log
Summary:	Zend_Log
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Log
Zend_Log

%package Zend_Mail
Summary:	Zend_Mail
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Mail
Zend_Mail

%package Zend_Measure
Summary:	Zend_Measure
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Measure
Zend_Measure

%package Zend_Memory
Summary:	Zend_Memory
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Memory
Zend_Memory

%package Zend_Mime
Summary:	Zend_Mime
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Mime
Zend_Mime

%package Zend_OpenId
Summary:	Zend_OpenId
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_OpenId
Zend_OpenId

%package Zend_Pdf
Summary:	Zend_Pdf
Group:		Development/Languages/PHP

%description Zend_Pdf
Zend_Pdf

%package Zend_Registry
Summary:	Zend_Registry
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Registry
Zend_Registry

%package Zend_Rest
Summary:	Zend_Rest
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Rest
Zend_Rest

%package Zend_Search_Lucene
Summary:	Zend_Search_Lucene
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Search_Lucene
Zend_Search_Lucene

%package Zend_Server_Reflection
Summary:	Zend_Server_Reflection
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Server_Reflection
Zend_Server_Reflection

%package Zend_Service_Akismet
Summary:	Zend_Service_Akismet
Group:		Development/Languages/PHP

%description Zend_Service_Akismet
Zend_Service_Akismet

%package Zend_Service_Amazon
Summary:	Zend_Service_Amazon
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Service_Amazon
Zend_Service_Amazon

%package Zend_Service_Audioscrobbler
Summary:	Zend_Service_Audioscrobbler
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Service_Audioscrobbler
Zend_Service_Audioscrobbler

%package Zend_Service_Delicious
Summary:	Zend_Service_Delicious
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Service_Delicious
Zend_Service_Delicious

%package Zend_Service_Flickr
Summary:	Zend_Service_Flickr
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Service_Flickr
Zend_Service_Flickr

%package Zend_Service_Nirvanix
Summary:	Zend_Service_Nirvanix
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Service_Nirvanix
Zend_Service_Nirvanix

%package Zend_Service_Simpy
Summary:	Zend_Service_Simpy
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Service_Simpy
Zend_Service_Simpy

%package Zend_Service_SlideShare
Summary:	Zend_Service_SlideShare
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Service_SlideShare
Zend_Service_SlideShare

%package Zend_Service_StrikeIron
Summary:	Zend_Service_StrikeIron
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Service_StrikeIron
Zend_Service_StrikeIron

%package Zend_Service_Technorati
Summary:	Zend_Service_Technorati
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Service_Technorati
Zend_Service_Technorati

%package Zend_Service_Yahoo
Summary:	Zend_Service_Yahoo
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Service_Yahoo
Zend_Service_Yahoo

%package Zend_Session
Summary:	Zend_Session
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Session
Zend_Session

%package Zend_Translate
Summary:	Zend_Translate
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Translate
Zend_Translate

%package Zend_Uri
Summary:	Zend_Uri
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Uri
Zend_Uri

%package Zend_Validate
Summary:	Zend_Validate
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Validate
Zend_Validate

%package Zend_Version
Summary:	Zend_Version
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_Version
Zend_Version

%package Zend_View
Summary:	Zend_View
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_View
Zend_View

%package Zend_XmlRpc
Summary:	Zend_XmlRpc
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description Zend_XmlRpc
Zend_XmlRpc

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
%dir %{php_pear_dir}/Zend
%dir %{php_pear_dir}/Zend/Console
%dir %{php_pear_dir}/Zend/Search

%dir %{php_pear_dir}/Zend/Server
%{php_pear_dir}/Zend/Server/Abstract.php
%{php_pear_dir}/Zend/Server/Exception.php
%{php_pear_dir}/Zend/Server/Interface.php

%dir %{php_pear_dir}/Zend/Service
%{php_pear_dir}/Zend/Service/Abstract.php
%{php_pear_dir}/Zend/Service/Exception.php

%{php_pear_dir}/Zend/Request/Interface.php

%{php_pear_dir}/Zend/TimeSync
%{php_pear_dir}/Zend/TimeSync.php

%files Zend_Acl
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Acl
%{php_pear_dir}/Zend/Acl.php

%files Zend_Auth
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Auth
%{php_pear_dir}/Zend/Auth.php

%files Zend_Cache
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Cache
%{php_pear_dir}/Zend/Cache.php

%files Zend_Config
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Config
%{php_pear_dir}/Zend/Config.php

%files Zend_Console_Getopt
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Console/Getopt
%{php_pear_dir}/Zend/Console/Getopt.php

%files Zend_Controller
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Controller

%files Zend_Currency
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Currency
%{php_pear_dir}/Zend/Currency.php

%files Zend_Date
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Date
%{php_pear_dir}/Zend/Date.php

%files Zend_Db
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Db
%{php_pear_dir}/Zend/Db.php

%files Zend_Debug
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Debug.php

%files Zend_Exception
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Exception.php

%files Zend_Feed
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Feed
%{php_pear_dir}/Zend/Feed.php

%files Zend_Filter
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Filter
%{php_pear_dir}/Zend/Filter.php
%exclude %{php_pear_dir}/Zend/Filter/Input.php

%files Zend_Filter_Input
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Filter/Input.php

%files Zend_Form
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Form
%{php_pear_dir}/Zend/Form.php

%files Zend_Gdata
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Gdata
%{php_pear_dir}/Zend/Gdata.php

%files Zend_Http
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Http

%files Zend_InfoCard
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/InfoCard
%{php_pear_dir}/Zend/InfoCard.php

%files Zend_Json
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Json
%{php_pear_dir}/Zend/Json.php

%files Zend_Layout
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Layout
%{php_pear_dir}/Zend/Layout.php

%files Zend_Ldap
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Ldap
%{php_pear_dir}/Zend/Ldap.php

%files Zend_Loader
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Loader
%{php_pear_dir}/Zend/Loader.php

%files Zend_Locale
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Locale
%{php_pear_dir}/Zend/Locale.php

%files Zend_Log
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Log
%{php_pear_dir}/Zend/Log.php

%files Zend_Mail
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Mail
%{php_pear_dir}/Zend/Mail.php

%files Zend_Measure
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Measure

%files Zend_Memory
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Memory
%{php_pear_dir}/Zend/Memory.php

%files Zend_Mime
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Mime
%{php_pear_dir}/Zend/Mime.php

%files Zend_OpenId
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/OpenId
%{php_pear_dir}/Zend/OpenId.php

%files Zend_Pdf
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Pdf
%{php_pear_dir}/Zend/Pdf.php

%files Zend_Registry
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Registry.php

%files Zend_Rest
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Rest

%files Zend_Search_Lucene
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Search/Exception.php
%{php_pear_dir}/Zend/Search/Lucene
%{php_pear_dir}/Zend/Search/Lucene.php

%files Zend_Server_Reflection
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Server/Reflection
%{php_pear_dir}/Zend/Server/Reflection.php

%files Zend_Service_Akismet
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Akismet.php

%files Zend_Service_Amazon
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Amazon
%{php_pear_dir}/Zend/Service/Amazon.php

%files Zend_Service_Audioscrobbler
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Audioscrobbler.php

%files Zend_Service_Delicious
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Delicious
%{php_pear_dir}/Zend/Service/Delicious.php

%files Zend_Service_Flickr
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Flickr
%{php_pear_dir}/Zend/Service/Flickr.php

%files Zend_Service_Nirvanix
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Nirvanix
%{php_pear_dir}/Zend/Service/Nirvanix.php

%files Zend_Service_Simpy
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Simpy
%{php_pear_dir}/Zend/Service/Simpy.php

%files Zend_Service_SlideShare
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/SlideShare
%{php_pear_dir}/Zend/Service/SlideShare.php

%files Zend_Service_StrikeIron
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/StrikeIron
%{php_pear_dir}/Zend/Service/StrikeIron.php

%files Zend_Service_Technorati
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Technorati
%{php_pear_dir}/Zend/Service/Technorati.php

%files Zend_Service_Yahoo
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Yahoo
%{php_pear_dir}/Zend/Service/Yahoo.php

%files Zend_Session
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Session
%{php_pear_dir}/Zend/Session.php

%files Zend_Translate
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Translate
%{php_pear_dir}/Zend/Translate.php

%files Zend_Uri
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Uri
%{php_pear_dir}/Zend/Uri.php

%files Zend_Validate
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Validate
%{php_pear_dir}/Zend/Validate.php

%files Zend_Version
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Version.php

%files Zend_View
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/View
%{php_pear_dir}/Zend/View.php

%files Zend_XmlRpc
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/XmlRpc

%files demos
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
