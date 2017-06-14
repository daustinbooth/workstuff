#!/usr/bin/python
'''
ping.py
resolves ips to hostnames
'''

import subprocess
import re
with open('lists/hostnames.txt') as h:
    with open ('lists/fullhostnames.txt','w') as outfile:	
      hostnames = h.readlines()
        for host in hostnames:
 	        i = host.strip()
                outfile.write((i) +'.net')
                outfile.write('\n')



with open('lists/fullhostnames.txt') as hostnames:
	with open('lists/ips.txt', 'a') as ips:
		host = hostnames.readlines()
		for line in host:
			line = line.strip()
			response = subprocess.check_output(['dig', "+short", line])
			response = ((line)+ ' ' + str(response))
			output = re.findall( r'[0-9]+(?:\.[0-9]+){3}', response )
			output = str(output)
			if len(output) > 3:
				print response,
