Name: redborder-netflow2kafka
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Package for redborder-netflow2kafka systemd unit running x2kafka.

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-netflow2kafka
Source0: %{name}-%{version}.tar.gz

Requires: x2kafka

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
install -D -m 0644 resources/systemd/redborder-netflow2kafka.service %{buildroot}/usr/lib/systemd/system/redborder-netflow2kafka.service

%pre
# the unit was called netflow2kafka in previous versions: stop it so it frees UDP 2055
if [ "$1" -gt 1 ]; then
  systemctl disable --now netflow2kafka.service >/dev/null 2>&1 || :
fi

%post
systemctl daemon-reload

%files
%defattr(0644,root,root)
/usr/lib/systemd/system/redborder-netflow2kafka.service
%doc

%changelog
* Wed Nov 18 2026 manegron <manegron@redborder.com>
- Rename the systemd unit from netflow2kafka to redborder-netflow2kafka

* Mon Nov 09 2026 Juan Soto <jsoto@redborder.com> - 1.0.0-1
- first spec version, netflow2kafka service runs x2kafka and replaces f2k
