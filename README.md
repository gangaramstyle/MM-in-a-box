MM-in-a-box
===========

Setting up LAN
------------
Update apt-get and install the necessary packages

1. sudo apt-get update
2. sudo apt-get install apache2
3. sudo apt-get install hostapd
4. sudo apt-get install isc-dhcp-server

Edit the necessary config files

1. Edit the hostapd file with: sudo nano /etc/hostapd/hostapd.conf and replace with the hostapd.conf file from the repository
2. Edit the network interfaces file with: sudo nano /etc/network/interfaces and replace with the interfaces file from the repository
3. Edit the dhcp config file with: sudo nano /etc/dhcp/dhcp.conf and replace with the dhcpd.conf file from the repository
4. Edit the rc.local file with sudo nano /etc/rc.local and replace with the rc.local file in the repository

This should be
