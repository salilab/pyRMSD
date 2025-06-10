Name:           python3-pyrmsd
Version:        4.3.2
Release:        3%{?dist}
Summary:        Way of performing RMSD calculations of large sets of structures
Group:          Development/Languages
License:        MIT 
URL:            https://github.com/salilab/pyRMSD
Source0:        pyRMSD-%{version}.zip
Patch1:         pyrmsd-setuptools.patch
Patch2:         pyrmsd-numpy2.patch
Patch3:         pyrmsd-test-tolerance.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  python3-devel, python3-setuptools, python3-numpy, gcc-c++

%description
pyRMSD goal is the fast (and easy!) calculation of rmsd collective
operations, specially matrices of large ensembles of protein
conformations. It also offers a symmetric distance matrix implementation
with improved access speed and memory efficiency.

If you like it and you are using it for your scientific projects, please
cite `the pyRMSD
paper <http://bioinformatics.oxfordjournals.org/content/29/18/2363>`_.

%prep
%setup -q -n pyRMSD-%{version}
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --record=INSTALLED_FILES
 
%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
cd pyRMSD/test
%{__python3} testRMSDCalculators.py -v

%files -f INSTALLED_FILES
%defattr(-,root,root,-)

%changelog
* Tue Aug 01 2023 Ben Webb <ben@salilab.org>  4.3.2-2
- Set correct name

* Tue Aug 01 2023 Ben Webb <ben@salilab.org>  4.3.2-1
- Update to latest version, drop Python 2

* Tue Dec 09 2014 Ben Webb <ben@salilab.org>  4.0.0-1
- Initial package.
