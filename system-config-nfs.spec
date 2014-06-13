Summary: NFS server configuration tool
Name: system-config-nfs
Version: 1.3.51
Release: 7
URL: http://fedorahosted.org/%{name}
License: GPLv2+
Group: System/Configuration/Networking
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Source0: http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2
Patch0: service_name.patch
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: python
Obsoletes: system-config-nfs < 1.3.42
Requires: system-config-nfs-docs
Requires: pygtk2.0
Requires: pygtk2.0-libglade
Requires: python >= 2.0
Requires: nfs-utils
Requires: usermode
Requires: hicolor-icon-theme

%description
system-config-nfs is a graphical user interface for creating, 
modifying, and deleting nfs shares.

%prep
%setup -q
%patch0 -p1

%build
make %{?with_console_util:CONSOLE_USE_CONFIG_UTIL=1} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

desktop-file-install --vendor system --delete-original       \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
  --add-category X-Red-Hat-Base        \
  --add-category X-Red-Hat-ServerConfig        \
  $RPM_BUILD_ROOT%{_datadir}/applications/system-config-nfs.desktop

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/system-config-nfs
%{_datadir}/system-config-nfs
%{_datadir}/applications/system-config-nfs.desktop
%{_datadir}/icons/hicolor/48x48/apps/system-config-nfs.png
%config(noreplace) %{_sysconfdir}/security/console.apps/system-config-nfs
%config(noreplace) %{_sysconfdir}/pam.d/system-config-nfs


%changelog
* Sat May 28 2011 Александр Казанцев <kazancas@mandriva.org> 1.3.51-1mdv2011.0
+ Revision: 681298
- initial adopt from Fedora
- imported package system-config-nfs

