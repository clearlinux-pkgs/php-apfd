#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-apfd
Version  : 1.0.2
Release  : 11
URL      : https://pecl.php.net/get/apfd-1.0.2.tgz
Source0  : https://pecl.php.net/get/apfd-1.0.2.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: php-apfd-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
# ext-apfd
[![Build Status](https://travis-ci.org/m6w6/ext-apfd.svg?branch=master)](https://travis-ci.org/m6w6/ext-apfd)

%package lib
Summary: lib components for the php-apfd package.
Group: Libraries

%description lib
lib components for the php-apfd package.


%prep
%setup -q -n apfd-1.0.2
cd %{_builddir}/apfd-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
autoupdate
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20200930/apfd.so
