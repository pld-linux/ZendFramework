# NOTE
# - dependencies are filled according to official doc:
#   http://framework.zend.com/manual/1.12/en/requirements.introduction.html
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

# TODO
# - check Zend/Pdf/FileParser/Image/Jpeg.php and Zend/Pdf/FileParser/Image/Tiff.php
#   presence in Zend/Pdf/Image.php after update [not implemented in 1.10.2)
%define		php_min_version 5.2.11
%include	/usr/lib/rpm/macros.php
Summary:	Zend Framework
Summary(pl.UTF-8):	Szkielet Zend
Name:		ZendFramework
# 1.12 series EOL: https://framework.zend.com/blog/2016-06-28-zf1-eol.html
Version:	1.12.20
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
# Source0Download: https://framework.zend.com/downloads/archives#ZF1
Source0:	https://packages.zendframework.com/releases/%{name}-%{version}/ZendFramework-%{version}.tar.gz
# Source0-md5:	2f242859c42ae5d919aaf2669c9c7c94
Source1:	https://packages.zendframework.com/releases/ZendFramework-%{version}/%{name}-%{version}-manual-en.tar.gz
# Source1-md5:	b3691da3fc83d16629d23e76c9887c2e
Source2:	%{name}-find-lang.sh
Patch0:		%{name}-additional-locales.patch
Patch1:		%{name}-deps.patch
URL:		http://framework.zend.com/manual/1.12/en/manual.html
BuildRequires:	/usr/bin/php
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	sed >= 4.0
Requires:	php(core) >= %{php_min_version}
Requires:	php-pear
Requires:	rpm-whiteout >= 1.32
Obsoletes:	ZendFramework-doc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# disable PEAR dependency solving in requirements, while we still do Provide them
%define		_noautoreq_pear Zend/.*

# exclude optional php dependencies
%define		_noautophp	php-oci8 php-bitset

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp}

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
Summary:	Zend_Acl - ACL functionality and privileges management
Summary(pl.UTF-8):	Zend_Acl - listy kontroli dostępu i zarządzanie uprawnieniami
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.acl.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}

%description Zend_Acl
Zend_Acl provides lightweight and flexible access control list (ACL)
functionality and privileges management. In general, an application
may utilize such functionality to control access to certain protected
objects by other requesting objects.

%description Zend_Acl -l pl.UTF-8
Zend_Acl udostępnia lekkie i elastyczne listy kontroli dostępu (ACL)
oraz zarządzanie uprawnieniami. W ogólności aplikacje mogą
wykorzystywać te funkcje do kontroli dostępu do określonych
chronionych obiektów przez inne obiekty.

%package Zend_Amf
Summary:	Zend_Amf - Action Message Format support
Summary(pl.UTF-8):	Zend_Amf - obsługa formatu AMF (Action Message Format)
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.amf.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Acl = %{version}-%{release}
Requires:	%{name}-Zend_Auth = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Reflection = %{version}-%{release}
Requires:	%{name}-Zend_Server = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(dom)
Suggests:	php(simplexml)

%description Zend_Amf
Zend_Amf provides support for Adobe's Action Message Format (AMF), to
allow communication between Adobe's Flash Player and PHP.
Specifically, it provides a gateway server implementation for handling
requests sent from the Flash Player to the server and mapping these
requests to object and class methods and arbitrary callbacks.

%description Zend_Amf -l pl.UTF-8
Zend_Amf dodaje obsługę formatu Adobe Action Message Format (AMF),
pozwalającego na komunikację między Adobe Flash Playerem a PHP. W
szczególności udostępnia implementację serwera bramki do obsługi żądań
wysyłanych z Flash Playera do serwera i odwzorowywania tych żądań na
obiekty i metody klas oraz wywołania zwrotne.

%package Zend_Application
Summary:	Zend_Application - bootstrap facility
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.amf.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}
Suggests:	php(date)

%description Zend_Application
Zend_Application provides a bootstrapping facility for applications
which provides reusable resources, common- and module-based bootstrap
classes and dependency checking. It also takes care of setting up the
PHP environment and introduces autoloading by default.

%package Zend_Auth
Summary:	Zend_Auth - authentication API
Summary(pl.UTF-8):	Zend_Auth - API do uwierzytelniania
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.auth.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Db = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	php(ctype)
Suggests:	php(hash)
# Zend_Auth_Adapter_Http requires hash

%description Zend_Auth
Zend_Auth provides an API for authentication and includes concrete
authentication adapters for common use case scenarios.

%description Zend_Auth -l pl.UTF-8
Zend_Auth udostępnia API do uwierzytelniania i zawiera właściwe
adaptery do uwierzytelniania w popularnych przypadkach użycia.

%package Zend_Barcode
Summary:	Zend_Barcode - barcode generator
Summary(pl.UTF-8):	Zend_Barcode - generator kodów kreskowych
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.barcode.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Validate = %{version}-%{release}

%description Zend_Barcode
Zend_Barcode provides a generic way to generate barcodes. The
Zend_Barcode component is divided into two subcomponents: barcode
objects and renderers. Objects allow you to create barcodes
independently of the renderer. Renderer allow you to draw barcodes
based on the support required.

%description Zend_Barcode -l pl.UTF-8
Zend_Barcode udostępnia funkcjonalność generowania kodów kreskowych.
Komponent Zend_Barcode podzielony jest na dwa podkomponenty: obiekty i
renderery. Obiekty pozwalają na tworzenie kodów niezależnie od
renderera, renderer na rysowanie kodów na podstawie obiektu.

%package Zend_Cache
Summary:	Zend_Cache - data caching
Summary(pl.UTF-8):	Zend_Cache - pamięć podręczna dla danych
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.cache.html
Requires:	%{name} = %{version}-%{release}
Suggests:	php(apc)
Suggests:	php(memcache)
Suggests:	php(memcached)
Suggests:	php(sqlite)
# Zend_Cache_Backend_Apc requires apc
# Zend_Cache_Backend_Memcached requires memcache
# Zend_Cache_Backend_Libmemcached requires memcached
# Zend_Cache_Backend_Sqlite requires sqlite

%description Zend_Cache
Zend_Cache provides a flexible approach toward caching data, including
support for tagging, manipulating, iterating, and removing subsets.

%description Zend_Cache -l pl.UTF-8
Zend_Cache zapewnia elastyczną pamięć podręczną dla danych z obsługą
oznaczania, modyfikowania, iterowania i usuwania podzbiorów.

%package Zend_Captcha
Summary:	Zend_Captcha - CAPTCHA functionality
Summary(pl.UTF-8):	Zend_Captcha - funkcjonalność CAPTCHA
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.captcha.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Service_ReCaptcha = %{version}-%{release}
Requires:	%{name}-Zend_Text = %{version}-%{release}
Requires:	%{name}-Zend_Validate = %{version}-%{release}
Requires:	php(gd)

%description Zend_Captcha
CAPTCHA stands for "Completely Automated Turing test to tell Computers
and Humans Apart" it is used as a challenge-response to ensure that
the individual submitting information is a human and not an automated
process. Typically, a captcha is used with form submissions where
authenticated users are not necessary, but you desire to prevent spam
submissions. Captchas can take variety of forms, including asking
logic questions, presenting skewed fonts, and presenting images and
asking how they relate. Zend_Captcha aims to provide a variety of
backends that may be utilized either standalone or in conjunction with
Zend_Form.

%description Zend_Captcha -l pl.UTF-8
CAPTCHA (Completely Automated Turing test to tell Computers and Humans
Apart) to oparta na pytaniu i odpowiedzi metoda upewnienia się, że
wysyłający informację jest człowiekiem, a nie zautomatyzowanym
procesem. Zwykle captcha używa się tam, gdzie formularze są wywyłane
bez uwierzytelniania, ale chcemy zapobiec wysyłaniu spamu. Mają różne
postaci, np. zadawanie pytań logicznych, pokazywanie wykrzywionych
fontów lub obrazków z pytaniem o ich powiązania. Klasa Zend_Captcha
udostępnia różne backendy. Może być używana zarówno samodzielnie, jak
i w połączeniu z Zend_Form.

%package Zend_Cloud
Summary:	Zend_Cloud - SimpleCloud API
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.cloud.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}

%description Zend_Cloud
SimpleCloud API

%package Zend_CodeGenerator
Summary:	Zend_CodeGenerator - generate arbitrary code using OO interface
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.codegenerator.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}

%description Zend_CodeGenerator
Zend_CodeGenerator provides facilities to generate arbitrary code
using an object oriented interface, both to create new code as well as
to update existing code. While the current implementation is limited
to generating PHP code, you can easily extend the base class in order
to provide code generation for other tasks: JavaScript, configuration
files, apache vhosts, etc.

%package Zend_Config
Summary:	Zend_Config - access to configuration data
Summary(pl.UTF-8):	Zend_Config - dostęp do danych konfiguracyjnych
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.config.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Suggests:	php(simplexml)
# Zend_Config_Xml requires simplexml

%description Zend_Config
Zend_Config is designed to simplify access to and use of configuration
data within applications.

%description Zend_Config -l pl.UTF-8
Zend_Config ma na celu ułatwienie dostępu i używania danych
konfiguracyjnych w aplikacjach.

%package Zend_Console_Getopt
Summary:	Zend_Console_Getopt - parsing command-line options and arguments
Summary(pl.UTF-8):	Zend_Console_Getopt - analiza opcji i argumentów linii poleceń
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.console.getopt.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}

%description Zend_Console_Getopt
The Zend_Console_Getopt class helps command-line applications to parse
their options and arguments.

%description Zend_Console_Getopt -l pl.UTF-8
Klasa Zend_Console_Getopt pomaga aplikacjom linii poleceń w analizie
opcji i argumentów.

%package Zend_Controller
Summary:	Zend_Controller - heart of Model-View-Controller system
Summary(pl.UTF-8):	Zend_Controller - podstawa systemu Model-View-Controller
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.controller.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Config = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}
Requires:	%{name}-Zend_Registry = %{version}-%{release}
Requires:	%{name}-Zend_Uri = %{version}-%{release}
Requires:	%{name}-Zend_View = %{version}-%{release}
Requires:	php(reflection)
Requires:	php(session)

%description Zend_Controller
Zend_Controller is the heart of Zend Framework's MVC system. MVC
stands for Model-View-Controller and is a design pattern targeted at
separating application logic from display logic.

%description Zend_Controller -l pl.UTF-8
Zend_Controller to podstawa systemu MVC szkieletu Zend. MVC oznacza
Model-View-Controller (model-widok-kontroler) i jest wzorcem
projektowym służącym do oddzielenia logiki aplikacji od logiki
wyświetlania.

%package Zend_Crypt
Summary:	Zend_Crypt
Group:		Development/Languages/PHP
#URL:		http://framework.zend.com/manual/1.12/en/zend.crypt.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}

%description Zend_Crypt
Zend_Crypt

%package Zend_Currency
Summary:	Zend_Currency - currency representation handling
Summary(pl.UTF-8):	Zend_Currency - obsługa reprezentacji walut
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.currency.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Locale = %{version}-%{release}
Requires:	php(iconv)

%description Zend_Currency
Zend_Currency is part of the I18N core of the Zend_Framework. It
handles all issues related to currency, money representation and
formating. And it also provides additional informational methods which
include localized informations on currencies, informations about which
currency is used in which region and more.

%description Zend_Currency -l pl.UTF-8
Zend_Currency to część rdzenia I18N szkieletu Zend. Obsługuje
wszystkie zawiłości związane z walutami, reprezentacją i formatowaniem
jednostek monetarnych. Zawiera także dodatkowe metody informacyjne
zawierające zlokalizowane informacje o walutach, regionach, w których
są używane itp.

%package Zend_Date
Summary:	Zend_Date - manipulating dates and times
Summary(pl.UTF-8):	Zend_Date - operacje na dacie i czasie
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.date.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Locale = %{version}-%{release}

%description Zend_Date
Zend_Date component offers a detailed, but simple API for manipulating
dates and times. Its methods accept a wide variety of types of
information, including date parts, in numerous combinations yielding
many features and possibilities above and beyond the existing PHP date
related functions.

%description Zend_Date -l pl.UTF-8
Komponent Zend_Date oferuje szczegółowe, ale proste API do operacji na
dacie i czasie. Metody przyjmują szeroki zakres typów informacji, w
tym części daty w różnych kombinacjach wykraczających poza funkcje
obróbki daty istniejące w PHP.

%package Zend_Db
Summary:	Zend_Db
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.db.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}
Suggests:	php(mysqli)
Suggests:	php(pdo-mysql)
Suggests:	php(pdo-pgsql)
Suggests:	php(pdo-sqlite)
# Zend_Db_Adapter_Db2 requires ibm_db2
# Zend_Db_Adapter_Firebird requires interbase
# Zend_Db_Adapter_Mysqli requires mysqli
# Zend_Db_Adapter_Oracle requires oci8
# Zend_Db_Adapter_Pdo_Mysql requires pdo_mysql
# Zend_Db_Adapter_Pdo_Pgsql requires pdo_pgsql
# Zend_Db_Adapter_Pdo_Sqlite requires pdo_sqlite

%description Zend_Db
Zend_Db and its related classes provide a simple SQL database
interface for Zend Framework. The Zend_Db_Adapter is the basic class
you use to connect your PHP application to an RDBMS. There is a
different Adapter class for each brand of RDBMS. The Zend_Db Adapters
create a bridge from the vendor-specific PHP extensions to a common
interface, to help you write PHP applications once and deploy with
multiple brands of RDBMS with very little effort. The interface of the
Adapter class is similar to the interface of the PHP Data Objects
extension.

Zend_Db provides Adapter classes to PDO drivers for the following
RDBMS brands:
- IBM DB2 and Informix Dynamic Server (IDS), using the pdo_ibm PHP
  extension
- MySQL, using the pdo_mysql PHP extension
- Microsoft SQL Server, using the pdo_mssql PHP extension
- Oracle, using the pdo_oci PHP extension
- PostgreSQL, using the pdo_pgsql PHP extension
- SQLite, using the pdo_sqlite PHP extension

In addition, Zend_Db provides Adapter classes that utilize PHP
database extensions for the following RDBMS brands:
- MySQL, using the mysqli PHP extension
- Oracle, using the oci8 PHP extension
- IBM DB2, using the ibm_db2 PHP extension
- Firebird/Interbase, using the php_interbase PHP extension

%package Zend_Debug
Summary:	Zend_Debug
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.debug.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Debug
Zend_Debug is a simple debugging component. The static method
Zend_Debug::dump() prints or returns information about an expression.
This simple technique of debugging is easy to use in an ad hoc
fashion, and requires no initialization, special tools, or debugging
environment.

%package Zend_Dojo
Summary:	Zend_Dojo
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.dojo.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Form = %{version}-%{release}
Requires:	%{name}-Zend_Json = %{version}-%{release}
Requires:	%{name}-Zend_Registry = %{version}-%{release}
Requires:	%{name}-Zend_View = %{version}-%{release}

%description Zend_Dojo
Zend_Dojo component provides integration with Dojo Toolkit.

Integration points with Dojo include:
- JSON-RPC support
- dojo.data compatibility
- View helper to help setup the Dojo environment
- Dijit-specific Zend_View helpres
- Dijit-specific Zend_Form elements and decorators

%package Zend_Dom
Summary:	Zend_Dom
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.dom.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(dom)

%description Zend_Dom
Zend_Dom provides tools for working with DOM documents and structures.
Currently, it offer Zend_Dom_Query, which provides a unified interface
for querying DOM documents utilizing both XPath and CSS selectors.

%package Zend_Exception
Summary:	Zend_Exception
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.exception.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Exception
Zend_Exception is a base exception class. All exceptions thrown by
Zend Framework classes should throw an exception that derives from the
base class Zend_Exception.

%package Zend_EventManager
Summary:	Zend_EventManager
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.event-manager.html
Requires:	%{name} = %{version}-%{release}

%description Zend_EventManager
Zend_EventManager is a component designed for the following use cases:
- Implementing simple subject/observer patterns.
- Implementing Aspect-Oriented designs.
- Implementing event-driven architectures.

%package Zend_Feed
Summary:	Zend_Feed
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.feed.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}
Requires:	%{name}-Zend_Uri = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(dom)
Requires:	php(mbstring)
Requires:	php(simplexml)

%description Zend_Feed
Zend_Feed provides functionality for consuming RSS and Atom feeds. It
provides a natural syntax for accessing elements of feeds, feed
attributes, and entry attributes. Zend_Feed also has extensive support
for modifying feed and entry structure with the same natural syntax,
and turning the result back into XML. In the future, this modification
support could provide support for the Atom Publishing Protocol.

%package Zend_File
Summary:	Zend_File
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.file.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Suggests:	php(apc)

%description Zend_File
Zend_File enables developers to take control over file uploads and
also over file downloads. It allows you to use built in validators for
file purposes and gives you the ability even to change files with
filters. Zend_File_Transfer works with adapters which allow to use the
same API for different transport protocols like HTTP, FTP, WEBDAV and
more.

%package Zend_Filter
Summary:	Zend_Filter
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.filter.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}
Requires:	%{name}-Zend_Validate = %{version}-%{release}
Requires:	php(reflection)
Suggests:	php(zlib)
# Zend_Filter_Compress requires zlib

%description Zend_Filter
Zend_Filter component provides a set of commonly needed data filters.
It also provides a simple filter chaining mechanism by which multiple
filters may be applied to a single datum in a user-defined order.

%package Zend_Filter_Input
Summary:	Zend_Filter_Input
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.filter.input.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Filter_Input
Zend_Filter_Input provides a declarative interface to associate
multiple filters and validators, apply them to collections of data,
and to retrieve input values after they have been processed by the
filters and validators. Values are returned in escaped format by
default for safe HTML output.

%package Zend_Form
Summary:	Zend_Form
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.form.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Filter = %{version}-%{release}
Requires:	%{name}-Zend_Validate = %{version}-%{release}

%description Zend_Form
Zend_Form simplifies form creation and handling in your web
application. It accomplishes the following goals:
- Element input filtering and validation
- Element ordering
- Element and Form rendering, including escaping
- Element and form grouping
- Element and form-level configuration

%package Zend_Gdata
Summary:	Zend_Gdata
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.gdata.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Http = %{version}-%{release}
Requires:	%{name}-Zend_Mime = %{version}-%{release}
Requires:	%{name}-Zend_Version = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(ctype)
Requires:	php(dom)

%description Zend_Gdata
Zend_Gdata component is a interface for accessing Google Data from
PHP. Google Data APIs provide programmatic interface to some of
Google's online services. The Google data Protocol is based upon the
Atom Publishing Protocol and allows client applications to retrieve
data matching queries, post data, update data and delete data using
standard HTTP and the Atom syndication formation. Zend_Gdata component
also supports accessing other services implementing the Atom
Publishing Protocol.

%package Zend_Http
Summary:	Zend_Http
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.http.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}
Requires:	%{name}-Zend_Uri = %{version}-%{release}
Requires:	php(ctype)
Suggests:	php(curl)
Suggests:	php(fileinfo)
# Zend_Http_Client_Adapter_Curl requires curl
# Zend_Http_Client has soft dependency on mime_magic (fileinfo)

%description Zend_Http
Zend_Http component provides a client for the HTTP protocol. It
supports:
- URL validation
- cookies
- proxy servers.

%package Zend_Json
Summary:	Zend_Json
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.json.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}
Requires:	%{name}-Zend_Server = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(reflection)
Suggests:	php(json)

%description Zend_Json
Zend_Json provides convenience methods for serializing native PHP to
JSON and decoding JSON to native PHP.

JSON, JavaScript Object Notation, can be used for data interchange
between JavaScript and other languages. Since JSON can be directly
evaluated by JavaScript, it is a more efficient and lightweight format
than XML for exchanging data with JavaScript clients.

In addition, Zend_Json provides a useful way to convert any arbitrary
XML formatted string into a JSON formatted string. This built-in
feature will enable PHP developers to transform the enterprise data
encoded in XML format into JSON format before sending it to
browser-based Ajax client applications. It provides an easy way to do
dynamic data conversion on the server-side code thereby avoiding
unnecessary XML parsing in the browser-side applications. It offers a
nice utility function that results in easier application-specific data
processing techniques.

%package Zend_Layout
Summary:	Zend_Layout
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.layout.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}

%description Zend_Layout
Zend_Layout implements a classic Two Step View pattern, allowing
developers to wrap application content within another view, usually
representing the site template. Such templates are often termed
layouts by other projects, and Zend Framework has adopted this term
for consistency.

The main goals of Zend_Layout are as follows:
- Automate selection and rendering of layouts when used with the Zend
  Framework MVC components.
- Provide separate scope for layout related variables and content.
- Allow configuration, including layout name, layout script resolution
  (inflection), and layout script path.
- Allow disabling layouts, changing layout scripts, and other states;
  allow these actions from within action controllers and view scripts.
- Follow same script resolution rules (inflection) as the
  ViewRenderer, but allow them to also use different rules.
- Allow usage without Zend Framework MVC components.

%package Zend_Ldap
Summary:	Zend_Ldap
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.ldap.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	php(ldap)

%description Zend_Ldap
Zend_Ldap is a class for performing LDAP operations including but not
limited to binding, searching and modifying entries in an LDAP
directory.

%package Zend_Loader
Summary:	Zend_Loader
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.loader.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}

%description Zend_Loader
The Zend_Loader class includes methods to help you load files
dynamically.

%package Zend_Locale
Summary:	Zend_Locale
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.locale.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(iconv)

%description Zend_Locale
Zend_Locale is the Framework's answer to the question, "How can the
same application be used around the whole world?". This component is
the foundation of Zend_Date, Zend_Translate, and others. It provides:
- access to CLDR, an international data repository for I18N issues,
  for all framework classes
- localizing of numbers
- normalizing of dates, times and numbers.

%package Zend_Log
Summary:	Zend_Log
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.log.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	php(reflection)
Suggests:	php(dom)
# Zend_Log_Formatter_Xml requires dom

%description Zend_Log
Zend_Log is a component for general purpose logging. It supports
multiple log backends, formatting messages sent to the log, and
filtering messages from being logged. These functions are divided into
the following objects:
- A Log (instance of Zend_Log) is the object that your application
  uses the most. You can have as many Log objects as you like; they do
  not interact. A Log object must contain at least one Writer, and can
  optionally contain one or more Filters.
- A Writer (inherits from Zend_Log_Writer_Abstract) is responsible for
  saving data to storage.
- A Filter (implements Zend_Log_Filter_Interface) blocks log data from
  being saved. A filter may be applied to an individual Writer, or to a
  Log where it is applied before all Writers. In either case, filters
  may be chained.
- A Formatter (implements Zend_Log_Formatter_Interface) can format the
  log data before it is written by a Writer. Each Writer has exactly one
  Formatter.

%package Zend_Mail
Summary:	Zend_Mail
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.mail.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}
Requires:	%{name}-Zend_Mime = %{version}-%{release}
Requires:	%{name}-Zend_Validate = %{version}-%{release}
Suggests:	php(posix)

%description Zend_Mail
Zend_Mail provides generalized functionality to compose and send both
text and MIME-compliant multipart e-mail messages. Mail can be sent
with Zend_Mail via the default Zend_Mail_Transport_Sendmail transport
or via Zend_Mail_Transport_Smtp.

%package Zend_Markup
Summary:	Zend_Markup
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.markup.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Markup
The Zend_Markup component provides an extensible way for parsing text
and rendering lightweight markup languages like BBcode and Textile. It
is available as of Zend Framework version 1.10.

Zend_Markup uses a factory method to instantiate an instance of a
renderer that extends Zend_Markup_Renderer_Abstract. The factory
method accepts three arguments. The first one is the parser used to
tokenize the text (e.g. BbCode). The second (optional) parameter is
the renderer to use, Html by default. Thirdly an array with options to
use for the renderer can be specified.

%package Zend_Measure
Summary:	Zend_Measure
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.measure.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Locale = %{version}-%{release}
Requires:	%{name}-Zend_Registry = %{version}-%{release}

%description Zend_Measure
Zend_Measure component provide a generic and easy way for working with
measurements. Using Zend_Measure_* classes, you can convert
measurements into different units of the same type. They can be added,
subtracted and compared against each other. From a given input made in
the user's native language, the unit of measurement can be
automatically extracted. Numerous units of measurement are supported.

%package Zend_Memory
Summary:	Zend_Memory
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.memory.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Cache = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}

%description Zend_Memory
The Zend_Memory component is intended to manage data in an environment
with limited memory. Memory objects (memory containers) are generated
by memory manager by request and transparently swapped/loaded when
it's necessary. For example, if creating or loading a managed object
would cause the total memory usage to exceed the limit you specify,
some managed objects are copied to cache storage outside of memory. In
this way, the total memory used by managed objects does not exceed the
limit you need to enforce.

%package Zend_Mime
Summary:	Zend_Mime
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.mime.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	php(iconv)

%description Zend_Mime
Zend_Mime is a support class for handling multipart MIME messages.

%package Zend_Mobile_Push
Summary:	Zend_Mobile_Push
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.mobile.push.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}

%description Zend_Mobile_Push
Zend_Mobile_Push provides the ability for sending push notifications
to the vendor specific notification servers. Currently this list
includes APNS (iTouch/iPad/iPhone), GCM (Google Android) and MPNS
(Windows Phone).

%package Zend_Navigation
Summary:	Zend_Navigation - manage trees of pointers to web page
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.navigation.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Navigation
Zend_Navigation is a component for managing trees of pointers to web
pages. Simply put: It can be used for creating menus, breadcrumbs,
links, and sitemaps, or serve as a model for other navigation related
purposes.

%package Zend_Oauth
Summary:	Zend_Oauth
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.oauth.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Oauth
OAuth allows you to approve access by any application to your private
data stored a website without being forced to disclose your username
or password. If you think about it, the practice of handing over your
username and password for sites like Yahoo Mail or Twitter has been
endemic for quite a while. This has raised some serious concerns
because there's nothing to prevent other applications from misusing
this data. Yes, some services may appear trustworthy but that is never
guaranteed. OAuth resolves this problem by eliminating the need for
any username and password sharing, replacing it with a user controlled
authorization process

%package Zend_OpenId
Summary:	Zend_OpenId
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.openid.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Controller = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Http = %{version}-%{release}
Requires:	%{name}-Zend_Session = %{version}-%{release}
# needed for dh keys: any of these tree can do for
Suggests:	php(bcmath)
Suggests:	php(gmp)
Suggests:	php(openssl)

%description Zend_OpenId
Zend_OpenId is a Zend Framework component that provides a simple API
for building OpenID-enabled sites and identity providers.

%package Zend_Paginator
Summary:	Zend_Paginator
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.paginator.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Json = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}

%description Zend_Paginator
Zend_Paginator is a flexible component for paginating collections of
data and presenting that data to users.

The primary design goals of Zend_Paginator are as follows:
- Paginate arbitrary data, not just relational databases
- Fetch only the results that need to be displayed
- Do not force users to adhere to only one way of displaying data or
  rendering pagination controls
- Loosely couple Zend_Paginator to other Zend Framework components so
  that users who wish to use it independently of Zend_View, Zend_Db,
  etc. can do so.

%package Zend_Pdf
Summary:	Zend_Pdf
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.pdf.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Log = %{version}-%{release}
Requires:	%{name}-Zend_Memory = %{version}-%{release}
Requires:	php(ctype)
Requires:	php(gd)
Requires:	php(iconv)
Requires:	php(zlib)

%description Zend_Pdf
Zend_Pdf module is a PDF (Portable Document Format) manipulation
engine. It can load existing documents, create new, modify and save
modified documents. Thus it can help application dynamically prepare
documents in a PDF by modifying existing template or generating
document from a scratch.

Zend_Pdf module supports the following features:
- Create new document or load existing one (PDF V1.4 (Acrobat 5)
  documents are supported for loading now).
- Retrieving specified revision of the document.
- Manipulate pages within document. Changing page order, adding new
  pages, removing pages from a document.
- Different drawing primitives (lines, rectangles, polygons, circles,
  ellipses and sectors).
- Text drawing using any of the 14 standard (built-in) fonts or your
  own custom TrueType fonts.
- Rotations.
- Image drawing (JPG, PNG [Up to 8bit per channel+Alpha] and TIFF
  images are supported).
- Incremental PDF file update.

%package Zend_ProgressBar
Summary:	Zend_ProgressBar
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.progressbar.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Config = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Json = %{version}-%{release}

%description Zend_ProgressBar
Zend_ProgressBar is a component to create and update progressbars in
different environments. It consists of a single backend, which outputs
the progress through one of the multiple adapters. On every update, it
takes an absolute value and optionally a status message, and then
calls the adapter with some precalculated values like percentage and
estimated time left.

%package Zend_Queue
Summary:	Zend_Queue
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.progressbar.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Queue
Zend_Queue is a standardized interface for dealing with a variety of
queuing systems. Proposed systems include: simple array access,
Zend_Cache, Zend Platform Job Queue, Amazon's Simple Queue Service
(SQS). It should support creating queues, determining the number of
messages in a queue, retrieving messages from a queue (all or specific
number), submitting messages to a queue, and removing queues.

%package Zend_Reflection
Summary:	Zend_Reflection
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.reflection.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Reflection
Zend_Reflection is a drop-in extension to PHP's own Reflection API,
providing several additional features:
 - Ability to retrieve return values types.
 - Ability to retrieve method and function parameter types.
 - Ability to retrieve class property types.
 - DocBlocks gain a Reflection class, allowing introspection of
   docblocks. This provides the ability to determine what annotation tags
   have been defined as well as to retrieve their values, and the ability
   to retrieve the short and long descriptions.
 - Files gain a Reflection class, allowing introspection of PHP files.
   This provides the ability to determine what functions and classes are
   defined in a given file, as well as to instrospect them.
 - Ability to override any Reflection class with your own variant, for
   the entire reflection tree you create.

In general, Zend_Reflection works just like the standard Reflection
API, but provides a few additional methods for retrieving artifacts
not defined in the Reflection API.

%package Zend_Registry
Summary:	Zend_Registry
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.registry.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}

%description Zend_Registry
The registry is a container for storing objects and values in the
application space. By storing the value in the registry, the same
object is always available throughout your application. This mechanism
is an alternative to using global storage.

%package Zend_Rest
Summary:	Zend_Rest
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.rest.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Server = %{version}-%{release}
Requires:	%{name}-Zend_Service = %{version}-%{release}
Requires:	%{name}-Zend_Uri = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(ctype)
Requires:	php(dom)
Requires:	php(reflection)
Requires:	php(simplexml)

%description Zend_Rest
REST Web Services use service-specific XML formats. These ad-hoc
standards mean that the manner for accessing a REST web service is
different for each service. REST web services typically use URL
parameters (GET data) or path information for requesting data and POST
data for sending data. Zend_Rest component provides:
- capabilities to access REST web services
- capabilities to expose APIs as REST services

%package Zend_Search_Lucene
Summary:	Zend_Search_Lucene
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.search.lucene.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(ctype)
Requires:	php(dom)
Requires:	php(iconv)
Suggests:	php(bitset)

%description Zend_Search_Lucene
Zend_Search_Lucene is a general purpose text search engine. Since it
stores its index on the filesystem and does not require a database
server, it can add search capabilities to almost any PHP-driven
website.

Zend_Search_Lucene supports the following features:
- Ranked searching - best results returned first
- Many powerful query types: phrase queries, wildcard queries,
  proximity queries, range queries and more
- Search by specific field (e.g., title, author, contents)

%package Zend_Serializer
Summary:	Zend_Serializer
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.serializer.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Suggests:	php(igbinary)
Suggests:	php(json)
Suggests:	php(simplexml)
Suggests:	php(wddx)
# Zend_Serializer_Adapter_Igbinary requires igbinary
# Zend_Serializer_Adapter_Json soft depends on json
# Zend_Serializer_Adapter_Wddx requires SimpleXML, wddx

%description Zend_Serializer
Zend_Serializer provides an adapter based interface to simply generate
storable representation of php types by different facilities, and
recover.

%package Zend_Server
Summary:	Zend_Server
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.server.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	php(spl)

%description Zend_Server
The Zend_Server family of classes provides functionality for the
various server classes, including Zend_XmlRpc_Server,
Zend_Rest_Server, Zend_Json_Server and Zend_Soap_Wsdl.

%package Zend_Server_Reflection
Summary:	Zend_Server_Reflection
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.server.reflection.html
Requires:	%{name} = %{version}-%{release}
Requires:	php(reflection)

%description Zend_Server_Reflection
Zend_Server_Reflection provides a standard mechanism for performing
function and class introspection for use with server classes. It is
based on Reflection API, and extends it to provide methods for
retrieving parameter and return value types and descriptions, a full
list of function and method prototypes (i.e., all possible valid
calling combinations), and function/method descriptions.

%package Zend_Service
Summary:	Zend_Service
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Service
Zend_Service is an abstract class which serves as a foundation for web
service implementations, such as SOAP or REST.

%package Zend_Service_Akismet
Summary:	Zend_Service_Akismet
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.akismet.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Http = %{version}-%{release}
Requires:	%{name}-Zend_Uri = %{version}-%{release}
Requires:	%{name}-Zend_Version = %{version}-%{release}

%description Zend_Service_Akismet
Zend_Service_Akismet provides a client for the Akismet API. The
Akismet service is used to determine if incoming data is potentially
spam; it also exposes methods for submitting data as known spam or as
false positives (ham). Originally intended to help categorize and
identify spam for Wordpress, it can be used for any type of data.

Akismet requires an API key for usage. You may get one for signing up
for a WordPress.com account. You do not need to activate a blog;
simply acquiring the account will provide you with the API key.

Additionally, Akismet requires that all requests contain a URL to the
resource for which data is being filtered, and, because of Akismet's
origins in WordPress, this resource is called the blog url. This value
should be passed as the second argument to the constructor, but may be
reset at any time using the setBlogUrl() accessor, or overridden by
specifying a 'blog' key in the various method calls.

%package Zend_Service_Amazon
Summary:	Zend_Service_Amazon
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.amazon.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Http = %{version}-%{release}
Requires:	%{name}-Zend_Rest = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(dom)

%description Zend_Service_Amazon
Zend_Service_Amazon is a simple API for using Amazon web services.
Zend_Service_Amazon has two APIs: a more traditional one that follows
Amazon's own API, and a simpler "Query API" for constructing even
complex search queries easily.

Zend_Service_Amazon enables developers to retrieve information
appearing throughout Amazon.com web sites directly through the Amazon
Web Services API.

%package Zend_Service_Audioscrobbler
Summary:	Zend_Service_Audioscrobbler
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.audioscrobbler.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Http = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(iconv)
Requires:	php(simplexml)

%description Zend_Service_Audioscrobbler
Zend_Service_Audioscrobbler is a simple API for using the
Audioscrobbler REST Web Service. The Audioscrobbler Web Service
provides access to its database of Users, Artists, Albums, Tracks,
Tags, Groups, and Forums.

%package Zend_Service_Delicious
Summary:	Zend_Service_Delicious
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.delicious.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Date = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Http = %{version}-%{release}
Requires:	%{name}-Zend_Json = %{version}-%{release}
Requires:	%{name}-Zend_Rest = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(dom)

%description Zend_Service_Delicious
Zend_Service_Delicious is simple API for using del.icio.us XML and
JSON web services. This component gives you read-write access to posts
at del.icio.us if you provide credentials. It also allows read-only
access to public data of all users.

%package Zend_Service_DeveloperGarden
Summary:	Zend_Service_DeveloperGarden
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.developergarden.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Service_DeveloperGarden
DeveloperGarden is the name for the "Open Development services" of the
German Telekom. The "Open Development services" are a set of SOAP API
Services.

The family of Zend_Service_DeveloperGarden components provides a clean
and simple interface to the DeveloperGarden API and additionally
offers functionality to improve handling and performance

%package Zend_Service_Ebay
Summary:	Zend_Service_Ebay is a simple group of APIs for using eBay web services
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.ebay.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}

%description Zend_Service_Ebay
Zend_Service_Ebay is a simple group of APIs for using eBay web
services.

Zend_Service_Ebay implements the eBay APIs:
- Finding

%package Zend_Service_Flickr
Summary:	Zend_Service_Flickr
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.delicious.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Http = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(dom)
Requires:	php(iconv)

%description Zend_Service_Flickr
Zend_Service_Flickr is a simple API for using the Flickr REST Web
Service. In order to use the Flickr web services, you must have an API
key. To obtain a key, visit the Flickr API Documentation
<http://www.flickr.com/services/api/>.

%package Zend_Service_LiveDocx
Summary:	Zend_Service_LiveDocx
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.livedocx.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Service_LiveDocx
LiveDocx is a SOAP service that allows developers to generate word
processing documents by combining structured data from PHP with a
template, created in a word processor. The resulting document can be
saved as a PDF, DOCX, DOC, HTML or RTF file. LiveDocx implements
mail-merge in PHP.

The family of Zend_Service_LiveDocx components provides a clean and
simple interface to the LiveDocx API and additionally offers
functionality to improve network performance.

%package Zend_Service_Rackspace
Summary:	Zend_Service_Rackspace
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.rackspace.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Service_Rackspace
The Zend_Service_Rackspace is a class that provides a simple API to
manage the Rackspace services Cloud Files and Cloud Servers.

%package Zend_Service_ReCaptcha
Summary:	Zend_Service_ReCaptcha
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.recaptcha.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Http = %{version}-%{release}
Requires:	%{name}-Zend_Json = %{version}-%{release}
Suggests:	php(mcrypt)
# Zend_Service_ReCaptcha_MailHide requires mcrypt

%description Zend_Service_ReCaptcha
Zend_Service_ReCaptcha provides a client for the reCAPTCHA Web
Service. Per the reCAPTCHA site, "reCAPTCHA is a free CAPTCHA service
that helps to digitize books." Each reCAPTCHA requires the user to
input two words, the first of which is the actual captcha, and the
second of which is a word from some scanned text that Optical
Character Recognition (OCR) software has been unable to identifiy. The
assumption is that if a user correctly provides the first word, the
second is likely correctly entered as well, and can be used to improve
OCR software for digitizing books.

In order to use the reCAPTCHA service, you will need to sign up for an
account (http://recaptcha.net/whyrecaptcha.html) and register one or
more domains with the service in order to generate public and private
keys.

%package Zend_Service_ShortUrl
Summary:	Zend_Service_ShortUrl
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.short-url.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Service_ShortUrl
URL shorteners have exploded in popularity in the last several years,
in large part due to the social nature of the web and the desire to
share links.

Zend_Service_ShortUrl provides an API for accessing a number of
different URL shortener services, with the ability to both create
short URLs as well as retrieve the original URL.

%package Zend_Service_SlideShare
Summary:	Zend_Service_SlideShare
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.slideshare.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Cache = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Http = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}

%description Zend_Service_SlideShare
The Zend_Service_SlideShare component is used to interact with the
slideshare.net web services for hosting slide shows online. With this
component, you can embed slide shows which are hosted on this web site
within a web site and even upload new slide shows to your account.

In order to use the Zend_Service_SlideShare component you must first
create an account on the slideshare.net servers in order to receive an
API key, username, password and shared secret value -- all of which
are needed in order to use the Zend_Service_SlideShare component.

%package Zend_Service_SqlAzure
Summary:	Zend_Service_
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}

%description Zend_Service_SqlAzure

%package Zend_Service_StrikeIron
Summary:	Zend_Service_StrikeIron
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.strikeiron.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Http = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}

%description Zend_Service_StrikeIron
Zend_Service_StrikeIron provides a client to StrikeIron web services.

The Zend_Service_StrikeIron component provides:
- A single point for configuring your StrikeIron authentication
  credentials that can be used across many StrikeIron services.
- A standard way of retrieving your StrikeIron subscription
  information such as license status and the number of hits remaining to
  a service.
- The ability to use any StrikeIron service from its WSDL without
  creating a PHP wrapper class, and the option of creating a wrapper for
  a more convenient interface.
- Wrappers for three popular StrikeIron services.

Before you can get started with Zend_Service_StrikeIron, you must
first register (http://strikeiron.com/Register.aspx) for a StrikeIron
developer account. After registering, you will receive a StrikeIron
username and password. These will be used when connecting to
StrikeIron using Zend_Service_StrikeIron. You will also need to sign
up (http://www.strikeiron.com/ProductDetail.aspx?p=257) for
StrikeIron's Super Data Pack Web Service. Both registration steps are
free and can be done relatively quickly through the StrikeIron
website.

%package Zend_Service_Technorati
Summary:	Zend_Service_Technorati
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.technorati.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Date = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Http = %{version}-%{release}
Requires:	%{name}-Zend_Locale = %{version}-%{release}
Requires:	%{name}-Zend_Uri = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}

%description Zend_Service_Technorati
Zend_Service_Technorati provides an easy, intuitive and
object-oriented interface for using the Technorati API. It provides
access to all available Technorati API queries and returns the
original XML response as a friendly PHP object.

Technorati requires a valid API key for usage. To get your own API Key
you first need to create a new Technorati account
(http://technorati.com/signup/), then visit the API Key section
(http://technorati.com/developers/apikey.html).

%package Zend_Service_Twitter
Summary:	Zend_Service_Twitter
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.twitter.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Feed = %{version}-%{release}
Requires:	%{name}-Zend_Http = %{version}-%{release}
Requires:	%{name}-Zend_Json = %{version}-%{release}
Requires:	%{name}-Zend_Rest = %{version}-%{release}
Requires:	%{name}-Zend_Uri = %{version}-%{release}

%description Zend_Service_Twitter
Zend_Service_Twitter provides a client for the Twitter REST API.
Zend_Service_Twitter will allow you to query the public timeline and
if you provide a username and password for Twitter it will allow you
to get and update your status, reply to friends, direct message
friends, mark tweets as favorite and much more.

%package Zend_Service_WindowsAzure
Summary:	Zend_Service_WindowsAzure
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.windowsazure.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}

%description Zend_Service_WindowsAzure
Windows Azure is the name for Microsoft's Software + Services
platform, an operating system in the cloud providing services for
hosting, management, scalable storage with support for simple blobs,
tables, and queues, as well as a management infrastructure for
provisioning and geo-distribution of cloud-based services, and a
development platform for the Azure Services layer.

%package Zend_Service_Yahoo
Summary:	Zend_Service_Yahoo
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.service.yahoo.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Http = %{version}-%{release}
Requires:	%{name}-Zend_Rest = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(dom)

%description Zend_Service_Yahoo
Zend_Service_Yahoo is a simple API for using many of the Yahoo! REST
APIs. Zend_Service_Yahoo allows you to search Yahoo! Web search,
Yahoo! News, Yahoo! Local, Yahoo! Images. In order to use the Yahoo!
REST API, you must have a Yahoo! Application ID. To obtain an
Application ID, please complete and submit the Application ID Request
Form (http://developer.yahoo.com/wsregapp/).

%package Zend_Session
Summary:	Zend_Session
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.session.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	php(session)

%description Zend_Session
Zend_Session helps manage and preserve session data across multiple
page requests by the same client. Zend_Session component:
- provides an object-oriented interface to access session data
- provides optional security features to help protect against session
  hijacking
- supports namespaced access to the PHP session for interoperability.

%package Zend_Soap
Summary:	Zend_Soap
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.soap.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Server = %{version}-%{release}
Requires:	%{name}-Zend_Uri = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(dom)
Requires:	php(simplexml)

%description Zend_Soap
Zend_Soap component is intended to simplify Web Services development
for PHP programmers.

%package Zend_Tag
Summary:	Zend_Tag -- work with taggable Items
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.tag.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Tag
Zend_Tag is a component suite which provides a facility to work with
taggable Items. As its base, it provides two classes to work with
Tags, Zend_Tag_Item and Zend_Tag_ItemList. Additionally, it comes with
the interface Zend_Tag_Taggable, which allows you to use any of your
models as a taggable item in conjunction with Zend_Tag.

%package Zend_Text
Summary:	Zend_Text
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.text.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}

%description Zend_Text
Zend_Text is a component which enables developers to create a so
called FIGlet text. A FIGlet text is a string, which is represented as
ASCII art. FIGlets use a special font format, called FLT (FigLet
Font).

%package Zend_Test
Summary:	Zend_Test
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.test.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Controller = %{version}-%{release}
Requires:	%{name}-Zend_Dom = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Layout = %{version}-%{release}
Requires:	%{name}-Zend_Registry = %{version}-%{release}
Requires:	%{name}-Zend_Session = %{version}-%{release}

%description Zend_Test
Zend_Test provides tools to facilitate unit testing of your Zend
Framework applications.

%package Zend_TimeSync
Summary:	Zend_TimeSync
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.timesync.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Date = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}

%description Zend_TimeSync
Zend_TimeSync is able to receive internet or network time from a time
server using the NTP or SNTP protocol. With Zend_TimeSync, Zend
Framework is able to act independently from the time settings of the
server where it is running.

%package Zend_Tool
Summary:	Zend_Tool
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/wiki/display/ZFDEV/Zend_Tool
Requires:	%{name} = %{version}-%{release}
Requires:	/usr/bin/php

%description Zend_Tool
Zend_Tool component is intended to simplify project development for
PHP programmers.

Please note that this component is part of Zend Framework incubator.

%package Zend_Translate
Summary:	Zend_Translate
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.translate.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}
Requires:	%{name}-Zend_Locale = %{version}-%{release}
Suggests:	php(xml)
# Zend_Translate_Adapter_Qt requires xml
# Zend_Translate_Adapter_Tmx requires xml
# Zend_Translate_Adapter_Xliff requires xml

%description Zend_Translate
Zend_Translate is the Zend Framework's solution for multilingual
applications.

The benefits of Zend_Translate are:
- Supports multiple source formats: Zend_Translate supports several
  source formats, including those supported by PHP, and other formats
  including TMX and CSV files.
- Thread-safe gettext: The gettext reader of Zend_Translate is
  thread-safe. There are no problems using it in multi-threaded
  environments.
- Easy and generic API: The API of Zend_Translate is very simple and
  requires only a handful of functions. So it's easy to learn and easy
  to maintain. All source formats are handled the same way, so if the
  format of your source files change from Gettext to TMX, you only need
  to change one line of code to specify the storage adapter.
- Detection of the user's standard language: The preferred language of
  the user accessing the site can be detected and used by
  Zend_Translate.
- Automatic source detection: Zend_Translate is capable of detecting
  and integrating multiple source files and additionally detect the
  locale to be used depending on directory or filenames.

%package Zend_Uri
Summary:	Zend_Uri
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.uri.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}
Requires:	%{name}-Zend_Locale = %{version}-%{release}
Requires:	%{name}-Zend_Validate = %{version}-%{release}
Requires:	php(ctype)

%description Zend_Uri
Zend_Uri is a component that aids in manipulating and validating
Uniform Resource Identifiers (URIs). Zend_Uri exists primarily to
service other components such as Zend_Http_Client but is also useful
as a standalone utility.

%package Zend_Validate
Summary:	Zend_Validate
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.validate.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}
Requires:	%{name}-Zend_Locale = %{version}-%{release}
Requires:	php(ctype)
Requires:	php(reflection)

%description Zend_Validate
The Zend_Validate component provides a set of commonly needed
validators. It also provides a simple validator chaining mechanism by
which multiple validators may be applied to a single datum in a
user-defined order.

%package Zend_Version
Summary:	Zend_Version
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.version.html
Requires:	%{name} = %{version}-%{release}

%description Zend_Version
Zend_Version component delivers current version number of Zend
Framework.

%package Zend_View
Summary:	Zend_View
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.view.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Controller = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}
Requires:	%{name}-Zend_Locale = %{version}-%{release}
Requires:	%{name}-Zend_Registry = %{version}-%{release}
Requires:	php(reflection)

%description Zend_View
Zend_View is a class for working with the "view" portion of the
model-view-controller pattern. That is, it exists to help keep the
view script separate from the model and controller scripts. It
provides a system of helpers, output filters, and variable escaping.
Zend_View is template system agnostic; you may use PHP as your
template language, or create instances of other template systems and
manipulate them within your view script. Essentially, using Zend_View
happens in two major steps: 1. Your controller script creates an
instance of Zend_View and assigns variables to that instance. 2. The
controller tells the Zend_View to render a particular view, thereby
handing control over the view script, which generates the view output.

%package Zend_Wildfire
Summary:	Zend_Wildfire
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.wildfire.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Controller = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Json = %{version}-%{release}
Requires:	%{name}-Zend_Loader = %{version}-%{release}

%description Zend_Wildfire
Zend_Wildfire is a component that facilitates communication between
PHP code and Wildfire client components. The purpose of the Wildfire
Project is to develop standardized communication channels between a
large variety of components and a dynamic and scriptable plugin
architecture. At this time the primary focus is to provide a system to
allow server-side PHP code to inject logging messages into the Firebug
Console (http://getfirebug.com/).

%package Zend_Xml
Summary:	Zend_Xml
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
Requires:	php(dom)
Requires:	php(simplexml)
Requires:	php(xml)

%description Zend_Xml
Zend_Xml.

%package Zend_XmlRpc
Summary:	Zend_XmlRpc
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/1.12/en/zend.xmlrpc.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Zend_Exception = %{version}-%{release}
Requires:	%{name}-Zend_Http = %{version}-%{release}
Requires:	%{name}-Zend_Server = %{version}-%{release}
Requires:	%{name}-Zend_Xml = %{version}-%{release}
Requires:	php(dom)
Requires:	php(iconv)
Requires:	php(reflection)
Requires:	php(simplexml)

%description Zend_XmlRpc
From its home page <http://www.xmlrpc.com/>, XML-RPC is described as a
"...remote procedure calling using HTTP as the transport and XML as
the encoding. XML-RPC is designed to be as simple as possible, while
allowing complex data structures to be transmitted, processed and
returned". The Zend Framework provides support for both consuming
remote XML-RPC services and building new XML-RPC servers.

%package demos
Summary:	Demos for Zend Framework
Summary(pl.UTF-8):	Programy demonstracyjne dla szkieletu Zend Framework
Group:		Documentation

%description demos
Demos for Zend Framework.

%description demos -l pl.UTF-8
Programy demonstracyjne dla szkieletu Zend Framework.

%package manual-en
Summary:	Zend Framework manual in English language
Summary(pl.UTF-8):	Podręcznik do Zend Framework w języku angielskim
Group:		Documentation

%description manual-en
Zend Framework manual in English language.

%description manual-en -l pl.UTF-8
Podręcznik do Zend Framework w języku angielskim.

%prep
%setup -q -a1
mv %{name}-%{version}/documentation .
find '(' -name '*.php' -o -name '*.xml' ')' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'
%patch0 -p1
%patch1 -p1

install -p %{SOURCE2} find-lang.sh

sed -i -e 's,Zend/Serializer/Excception.php,Zend/Serializer/Exception.php,' library/Zend/Serializer/Adapter/PythonPickle.php

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
%if %{with tests}
lint_php() {
	for a in $(find library -name '*.php'); do
		php -n -l $a
	done
}
lint_php
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_bindir},%{php_pear_dir}/bin}
cp -a demos/Zend/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# library should be in include_path if used, so we use already defined %{php_pear_dir}
# NOTE: we could use %{php_data_dir} as of php-common-4:5.2.8-3, but then
# pear(...) deps won't be satisifed that these libs use extensively.
cp -a library/* $RPM_BUILD_ROOT%{php_pear_dir}

# create script in bindir
install -p bin/zf.php $RPM_BUILD_ROOT%{php_pear_dir}/bin
cat >> $RPM_BUILD_ROOT%{_bindir}/zf <<-'EOF'
#!/bin/sh
cd %{php_pear_dir}/bin
exec %{_bindir}/php -d safe_mode=off zf.php ${1:+"$@"}
EOF

./find-lang.sh %{name}.lang

# manual
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-en
cp -a documentation/manual/core/en/* $RPM_BUILD_ROOT%{_docdir}/%{name}-en

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%dir %{php_pear_dir}/Zend

%files Zend_Acl
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Acl
%{php_pear_dir}/Zend/Acl.php

%files Zend_Amf
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Amf

%files Zend_Application
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Application
%{php_pear_dir}/Zend/Application.php

%files Zend_ProgressBar
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/ProgressBar.php
%{php_pear_dir}/Zend/ProgressBar

%files Zend_Auth
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Auth
%{php_pear_dir}/Zend/Auth.php

%files Zend_Barcode
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Barcode
%{php_pear_dir}/Zend/Barcode.php

%files Zend_Cache
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Cache
%{php_pear_dir}/Zend/Cache.php
# Zend_Server_Cache subpackage?
# but not listed as separate component on doc
%{php_pear_dir}/Zend/Server/Cache.php

%files Zend_Captcha
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Captcha

%files Zend_Cloud
%defattr(644,root,root,755)
%dir %{php_pear_dir}/Zend/Cloud
%{php_pear_dir}/Zend/Cloud/AbstractFactory.php
%{php_pear_dir}/Zend/Cloud/Exception.php
%{php_pear_dir}/Zend/Cloud/OperationNotAvailableException.php

# subpackages?
%{php_pear_dir}/Zend/Cloud/DocumentService
%{php_pear_dir}/Zend/Cloud/Infrastructure
%{php_pear_dir}/Zend/Cloud/QueueService
%{php_pear_dir}/Zend/Cloud/StorageService

%files Zend_CodeGenerator
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/CodeGenerator

%files Zend_Config
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Config
%{php_pear_dir}/Zend/Config.php

%files Zend_Console_Getopt
%defattr(644,root,root,755)
%dir %{php_pear_dir}/Zend/Console
%{php_pear_dir}/Zend/Console/Getopt
%{php_pear_dir}/Zend/Console/Getopt.php

%files Zend_Controller
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Controller

%files Zend_Crypt
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Crypt
%{php_pear_dir}/Zend/Crypt.php

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

%files Zend_Dojo
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Dojo
%{php_pear_dir}/Zend/Dojo.php

%files Zend_Dom
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Dom

%files Zend_Exception
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Exception.php

%files Zend_EventManager
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/EventManager

# package here, as for now only EventManager uses Stdlib classes
%{php_pear_dir}/Zend/Stdlib

%files Zend_Feed
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Feed
%{php_pear_dir}/Zend/Feed.php

%files Zend_File
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/File

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

%files Zend_Locale -f %{name}.lang
%defattr(644,root,root,755)
%dir %{php_pear_dir}/Zend/Locale
%{php_pear_dir}/Zend/Locale.php
%{php_pear_dir}/Zend/Locale/Exception.php
%{php_pear_dir}/Zend/Locale/Format.php
%{php_pear_dir}/Zend/Locale/Math.php
%{php_pear_dir}/Zend/Locale/Math

%{php_pear_dir}/Zend/Locale/Data.php
%dir %{php_pear_dir}/Zend/Locale/Data
%{php_pear_dir}/Zend/Locale/Data/Translation.php
%{php_pear_dir}/Zend/Locale/Data/characters.xml
%{php_pear_dir}/Zend/Locale/Data/coverageLevels.xml
%{php_pear_dir}/Zend/Locale/Data/dayPeriods.xml
%{php_pear_dir}/Zend/Locale/Data/genderList.xml
%{php_pear_dir}/Zend/Locale/Data/languageInfo.xml
%{php_pear_dir}/Zend/Locale/Data/likelySubtags.xml
%{php_pear_dir}/Zend/Locale/Data/metaZones.xml
%{php_pear_dir}/Zend/Locale/Data/numberingSystems.xml
%{php_pear_dir}/Zend/Locale/Data/ordinals.xml
%{php_pear_dir}/Zend/Locale/Data/plurals.xml
%{php_pear_dir}/Zend/Locale/Data/postalCodeData.xml
%{php_pear_dir}/Zend/Locale/Data/root.xml
%{php_pear_dir}/Zend/Locale/Data/supplementalData.xml
%{php_pear_dir}/Zend/Locale/Data/supplementalMetadata.xml
%{php_pear_dir}/Zend/Locale/Data/telephoneCodeData.xml
%{php_pear_dir}/Zend/Locale/Data/windowsZones.xml

%files Zend_Log
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Log
%{php_pear_dir}/Zend/Log.php

%files Zend_Mail
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Mail
%{php_pear_dir}/Zend/Mail.php

%files Zend_Markup
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Markup
%{php_pear_dir}/Zend/Markup.php

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

%files Zend_Mobile_Push
%defattr(644,root,root,755)
%dir %{php_pear_dir}/Zend/Mobile
%{php_pear_dir}/Zend/Mobile/Exception.php
%{php_pear_dir}/Zend/Mobile/Push

%files Zend_Navigation
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Navigation
%{php_pear_dir}/Zend/Navigation.php

%files Zend_Oauth
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Oauth
%{php_pear_dir}/Zend/Oauth.php

%files Zend_OpenId
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/OpenId
%{php_pear_dir}/Zend/OpenId.php

%files Zend_Paginator
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Paginator
%{php_pear_dir}/Zend/Paginator.php

%files Zend_Pdf
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Pdf
%{php_pear_dir}/Zend/Pdf.php

%files Zend_Queue
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Queue
%{php_pear_dir}/Zend/Queue.php

%files Zend_Reflection
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Reflection

%files Zend_Registry
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Registry.php

%files Zend_Rest
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Rest

%files Zend_Search_Lucene
%defattr(644,root,root,755)
%dir %{php_pear_dir}/Zend/Search
%{php_pear_dir}/Zend/Search/Exception.php
%{php_pear_dir}/Zend/Search/Lucene
%{php_pear_dir}/Zend/Search/Lucene.php

%files Zend_Serializer
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Serializer
%{php_pear_dir}/Zend/Serializer.php

%files Zend_Server
%defattr(644,root,root,755)
%dir %{php_pear_dir}/Zend/Server
%{php_pear_dir}/Zend/Server/Abstract.php
%{php_pear_dir}/Zend/Server/Exception.php
%{php_pear_dir}/Zend/Server/Interface.php
%{php_pear_dir}/Zend/Server/Definition.php
%dir %{php_pear_dir}/Zend/Server/Method
%{php_pear_dir}/Zend/Server/Method/Callback.php
%{php_pear_dir}/Zend/Server/Method/Definition.php
%{php_pear_dir}/Zend/Server/Method/Parameter.php
%{php_pear_dir}/Zend/Server/Method/Prototype.php

%files Zend_Server_Reflection
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Server/Reflection
%{php_pear_dir}/Zend/Server/Reflection.php

%files Zend_Service
%defattr(644,root,root,755)
%dir %{php_pear_dir}/Zend/Service
%{php_pear_dir}/Zend/Service/Abstract.php
%{php_pear_dir}/Zend/Service/Exception.php

# subpackage?
%{php_pear_dir}/Zend/Service/Console

%files Zend_Service_Akismet
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Akismet.php

%files Zend_Service_Amazon
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Amazon
%{php_pear_dir}/Zend/Service/Amazon.php

%files Zend_Service_Audioscrobbler
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Audioscrobbler
%{php_pear_dir}/Zend/Service/Audioscrobbler.php

%files Zend_Service_Delicious
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Delicious
%{php_pear_dir}/Zend/Service/Delicious.php

%if 0
%files Zend_Service_DeveloperGarden
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/DeveloperGarden
%endif

%files Zend_Service_Ebay
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Ebay

%files Zend_Service_Flickr
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Flickr
%{php_pear_dir}/Zend/Service/Flickr.php

%files Zend_Service_LiveDocx
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/LiveDocx
%{php_pear_dir}/Zend/Service/LiveDocx.php

%files Zend_Service_Rackspace
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Rackspace

%files Zend_Service_ReCaptcha
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/ReCaptcha
%{php_pear_dir}/Zend/Service/ReCaptcha.php

%files Zend_Service_ShortUrl
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/ShortUrl

%files Zend_Service_SlideShare
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/SlideShare
%{php_pear_dir}/Zend/Service/SlideShare.php

%files Zend_Service_SqlAzure
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/SqlAzure

%files Zend_Service_StrikeIron
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/StrikeIron
%{php_pear_dir}/Zend/Service/StrikeIron.php

%if 0
%files Zend_Service_Technorati
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Technorati
%{php_pear_dir}/Zend/Service/Technorati.php
%endif

%files Zend_Service_Twitter
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Twitter
%{php_pear_dir}/Zend/Service/Twitter.php

%files Zend_Service_WindowsAzure
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/WindowsAzure

%files Zend_Service_Yahoo
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Service/Yahoo
%{php_pear_dir}/Zend/Service/Yahoo.php

%files Zend_Session
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Session
%{php_pear_dir}/Zend/Session.php

%files Zend_Soap
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Soap

%files Zend_Tag
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Tag

%files Zend_Text
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Text

%files Zend_Test
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Test

%files Zend_TimeSync
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/TimeSync
%{php_pear_dir}/Zend/TimeSync.php

%files Zend_Tool
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zf
%{php_pear_dir}/bin/zf.php
%{php_pear_dir}/Zend/Tool

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

%files Zend_Wildfire
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Wildfire

%files Zend_Xml
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/Xml

%files Zend_XmlRpc
%defattr(644,root,root,755)
%{php_pear_dir}/Zend/XmlRpc

%files demos
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files manual-en
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-en
