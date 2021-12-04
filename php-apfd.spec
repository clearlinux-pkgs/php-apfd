#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-apfd
Version  : 1.0.3
Release  : 17
URL      : https://pecl.php.net/get/apfd-1.0.3.tgz
Source0  : https://pecl.php.net/get/apfd-1.0.3.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: php-apfd-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
# ext-apfd
[![Build Status](https://github.com/m6w6/ext-apfd/workflows/ci/badge.svg?branch=master)](https://github.com/m6w6/ext-apfd/actions?query=branch%3Amaster+workflow%3Aci)
[![codecov](https://codecov.io/gh/m6w6/ext-apfd/branch/master/graph/badge.svg?token=Nku9tz8EMj)](https://codecov.io/gh/m6w6/ext-apfd)

%package lib
Summary: lib components for the php-apfd package.
Group: Libraries

%description lib
lib components for the php-apfd package.


%prep
%setup -q -n apfd-1.0.3
cd %{_builddir}/apfd-1.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/apfd.so
