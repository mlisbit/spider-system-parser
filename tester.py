#!/usr/bin/python

import monitoring

print ("PING: " + monitoring.get_ping("google.com"))
print ("LINK QUALITY: " + monitoring.get_link_quality("wlan0"))
print ("SIGNAL LEVEL: " + monitoring.get_signal_level("wlan0"))