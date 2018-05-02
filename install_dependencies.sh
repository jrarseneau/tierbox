#!/bin/sh

## Disable IPv6
sudo grep -q -F 'net.ipv6.conf.all.disable_ipv6 = 1' /etc/sysctl.d/99-sysctl.conf || sudo echo 'net.ipv6.conf.all.disable_ipv6 = 1' >> /etc/sysctl.d/99-sysctl.conf
sudo grep -q -F 'net.ipv6.conf.default.disable_ipv6 = 1' /etc/sysctl.d/99-sysctl.conf || sudo echo 'net.ipv6.conf.default.disable_ipv6 = 1' >> /etc/sysctl.d/99-sysctl.conf
sudo grep -q -F 'net.ipv6.conf.lo.disable_ipv6 = 1' /etc/sysctl.d/99-sysctl.conf || sudo echo 'net.ipv6.conf.lo.disable_ipv6 = 1' >> /etc/sysctl.d/99-sysctl.conf
sysctl -p

## Install Dependencies
sudo apt-get update
sudo apt-get install -y \
    git \
    build-essential \
    python3-dev \
    python3-pip \
    python-dev \
    python-pip
sudo python3 -m pip install --upgrade \
    pip \
    setuptools
sudo python -m pip install --upgrade \
    pip \
    setuptools
sudo python3 -m pip install \
    request \
    pyOpenSSL
sudo python -m pip install \
    ansible==2.5.0 \
    pyOpenSSL \
    requests
