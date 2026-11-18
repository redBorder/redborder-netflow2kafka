# redborder-netflow2kafka

Systemd unit that runs [x2kafka](https://github.com/redBorder/x2kafka) as the `redborder-netflow2kafka` service (netflow/IPFIX collector, UDP 2055).

The configuration (`/etc/redborder-netflow2kafka/config.json`) is rendered by Chef. This package replaces the legacy `f2k` and `redborder-f2k` packages.
