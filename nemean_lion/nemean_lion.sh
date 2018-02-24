#!/bin/bash

apt-get -y update && apt-get install -y openssh-server
sed -i s'/#Port 22/Port 655535/' /etc/ssh/sshd_config
service ssh restart
