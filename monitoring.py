#!/usr/bin/python

import os 

def get_ping(server):
	get_output = os.popen("ping -c 1 -W 1 "+server) #terminal command executed 
	s = get_output.readlines()								#gets the output
	get_output.close()										#stops capturing the input
	device_info = ''.join(s);								#join the strings from the input for easier parsing

	if (device_info.find("100% packet loss") != -1):		#checks if this string is found
		return ("ERROR: timeout on response from server")	#return this if above string is found
	elif (device_info.find("ping: unknown host") != -1): 
		return ("ERROR: unknown host")
	else:
		start = int(device_info.index("time=")+5)
		new_string = ""
		while (device_info[start] != 'm'):
			new_string += str(device_info[start])
			start=start+1
		return (new_string)

def get_link_quality(interface):
	start_capture = os.popen("iwconfig "+interface) 					#terminal command executed 
	s = start_capture.readlines()								#gets the output
	start_capture.close()										#stops capturing the input
	device_info = ''.join(s);									#join the strings from the input for easier parsing

	if (device_info.find("Link Quality=") != -1):		#checks if this string is found
		start = int(device_info.index("Link Quality=")+13)
		new_string = ""
		while (device_info[start] != ' '):
			new_string += str(device_info[start])
			start=start+1
		return (new_string)

def get_signal_level(interface):
	start_capture = os.popen("iwconfig "+interface) 					#terminal command executed 
	s = start_capture.readlines()								#gets the output
	start_capture.close()										#stops capturing the input
	device_info = ''.join(s);									#join the strings from the input for easier parsing

	if (device_info.find("Signal level=") != -1):		#checks if this string is found
		start = int(device_info.index("Signal level=")+13)
		new_string = ""
		while (device_info[start] != 'm'):
			new_string += str(device_info[start])
			start=start+1
		new_string += str(device_info[start+1])
		return (new_string)