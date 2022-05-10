#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-fontmath
Version  : 0.9.2
Release  : 5
URL      : https://files.pythonhosted.org/packages/b4/71/a6165862dcd6c30259b3ba9fc834a59a0e11b2c34f44f9e1d1eb6cc674d5/fontMath-0.9.2.zip
Source0  : https://files.pythonhosted.org/packages/b4/71/a6165862dcd6c30259b3ba9fc834a59a0e11b2c34f44f9e1d1eb6cc674d5/fontMath-0.9.2.zip
Summary  : A set of objects for performing math operations on font data.
Group    : Development/Tools
License  : MIT
Requires: pypi-fontmath-license = %{version}-%{release}
Requires: pypi-fontmath-python = %{version}-%{release}
Requires: pypi-fontmath-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(fonttools)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
[![Build Status](https://github.com/robotools/fontMath/workflows/Tests/badge.svg)](https://github.com/robotools/fontMath/actions?query=workflow%3ATests)
[![codecov](https://codecov.io/gh/robotools/fontMath/branch/master/graph/badge.svg)](https://codecov.io/gh/robotools/fontMath)
[![PyPI version fury.io](https://badge.fury.io/py/fontMath.svg)](https://pypi.org/project/fontMath/)
![Python versions](https://img.shields.io/badge/python-3.7%2C%203.8%2C%203.9%2C%203.10-blue.svg)

%package license
Summary: license components for the pypi-fontmath package.
Group: Default

%description license
license components for the pypi-fontmath package.


%package python
Summary: python components for the pypi-fontmath package.
Group: Default
Requires: pypi-fontmath-python3 = %{version}-%{release}

%description python
python components for the pypi-fontmath package.


%package python3
Summary: python3 components for the pypi-fontmath package.
Group: Default
Requires: python3-core
Provides: pypi(fontmath)
Requires: pypi(fonttools)

%description python3
python3 components for the pypi-fontmath package.


%prep
%setup -q -n fontMath-0.9.2
cd %{_builddir}/fontMath-0.9.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652193230
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-fontmath
cp %{_builddir}/fontMath-0.9.2/License.txt %{buildroot}/usr/share/package-licenses/pypi-fontmath/eacd7483dbe0f90140ab577e977c1c14d218e57a
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-fontmath/eacd7483dbe0f90140ab577e977c1c14d218e57a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
