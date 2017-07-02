#!/bin/sh
# ------------------------------------------------------------------
# loginfo.sh
# written by Duncan Murray
# quickly log info on RaspberryPI device 
# ------------------------------------------------------------------

VERSION=0.1.0

echo " --- Stats collected on " && date

echo " --- Hostname --- "
hostname  

echo " --- Users ---"
users  

echo " --- Network Config ---"
ifconfig

echo " --- List of Available Wifi Networks ---"
iwlist wlan0 scan | grep ESSID

echo " --- Internet Access Check ---"
echo "Google:"
ping -c2 google.com | grep rtt
echo "Acute Software:"
ping -c2 acutesoftware.com.au | grep rtt

echo " --- Network Links ---"
ss -r

ip maddr show

echo " --- Network Neighbours ---"
ip -s n


echo " --- CPU Info and Temperature ---"
cat /proc/cpuinfo
vcgencmd measure_temp

echo " --- Memory Free --- "
free  
df

echo " --- USB Disk details --- "
lsusb


echo " --- Uptime ---"
uptime  

