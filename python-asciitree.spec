#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	ASCII Trees
Summary(pl.UTF-8):	Drzewka ASCII
Name:		python-asciitree
Version:	0.3.3
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/asciitree/
Source0:	https://files.pythonhosted.org/packages/source/a/asciitree/asciitree-%{version}.tar.gz
# Source0-md5:	2570b31e563b69da1aff54509db8ac6a
URL:		https://pypi.org/project/asciitree/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
asciitree module allows to draw trees in your terminal.

%description -l pl.UTF-8
Moduł asciitree pozwala rysować drzewka w terminalu.

%package -n python3-asciitree
Summary:	ASCII Trees
Summary(pl.UTF-8):	Drzewka ASCII
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-asciitree
asciitree module allows to draw trees in your terminal.

%description -n python3-asciitree -l pl.UTF-8
Moduł asciitree pozwala rysować drzewka w terminalu.

%prep
%setup -q -n asciitree-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/asciitree
%{py_sitescriptdir}/asciitree-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-asciitree
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/asciitree
%{py3_sitescriptdir}/asciitree-%{version}-py*.egg-info
%endif
