Name:           python3-pyrmsd
Version:        4.3.3
Release:        1%{?dist}
Summary:        Way of performing RMSD calculations of large sets of structures
Group:          Development/Languages
License:        MIT 
URL:            https://github.com/salilab/pyRMSD
Source0:        pyRMSD-%{version}.zip
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
* Mon Mar 02 2026 Ben Webb <benmwebb@gmail.com>  4.3.3-1
- Update to latest version

* Tue Aug 01 2023 Ben Webb <benmwebb@gmail.com>  4.3.2-1
- Update to latest version, drop Python 2

* Tue Dec 09 2014 Ben Webb <benmwebb@gmail.com>  4.0.0-1
- Initial package.
