%define name        NNlinuxconfbak
%define buildroot   %{_topdir}/%{name}-%{version}-%{release}-buildroot
%define LINKDIR     /usr/local/bin
%define release     1
%define version     1.0
BuildRoot:      %{buildroot}

Name:           NNlinuxconfbak
Release:        %{release}
Version:        %{version}
Summary:        Linux config file backup

Group:          Development/Tools
License:        GPL
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  bash
Requires:       bash
Packager:      Dipanjan Mukherjee

%description
Linux config file backup

%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
echo "created $RPM_BUILD_ROOT"
install -m 755 -d ${RPM_BUILD_ROOT}%{LINKDIR}
install -m 0755 -o rpmbuild -g rpmbuild -d ${RPM_BUILD_ROOT}/etc/init.d
cp -r %{name}-%{version} ${RPM_BUILD_ROOT}
install -m 755 -o rpmbuild -g rpmbuild ${RPM_BUILD_ROOT}/%{name}-%{version} ${RPM_BUILD_ROOT}/etc/init.d/%{name}


%clean
rm -rf $RPM_BUILD_ROOT

%post
# POST ACTION:
/sbin/chkconfig --add "%{name}"
/sbin/chkconfig "%{name}" on
/etc/init.d/%{name} start


%files
%defattr(-,root,root)
/NNlinuxconfbak*
/usr/*
%attr(750, root, root) /etc/init.d/%{name}

%changelog
* Fri Aug 10 2018 - DM
- New rpm for linuxconfbackup
