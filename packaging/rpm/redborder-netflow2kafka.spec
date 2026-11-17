Name: redborder-netflow2kafka
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Package for redborder netflow2kafka systemd unit running x2kafka.

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-netflow2kafka
Source0: %{name}-%{version}.tar.gz

Requires: x2kafka
Obsoletes: f2k
Obsoletes: redborder-f2k

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
install -D -m 0644 resources/systemd/netflow2kafka.service %{buildroot}/usr/lib/systemd/system/netflow2kafka.service

%pre

%post
systemctl daemon-reload

%files
%defattr(0644,root,root)
/usr/lib/systemd/system/netflow2kafka.service
%doc

%changelog
* Mon Nov 09 2026 Juan Soto <jsoto@redborder.com> - 1.0.0-1
- first spec version, netflow2kafka service runs x2kafka and replaces f2k
