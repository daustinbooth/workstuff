#!/usr/bin/python

list = []
"""
blockips.py
This takes a list of ips and adds cisco commands to them
so we can unblock the heathens. After you paste hit return if there is not a newline,
then Control+D to send.
"""

outfile=open('network_objects.txt', 'w')

print('Paste the IPs here followed by Ctrl D to add Cisco commands:')

try:
    while True:
        list.append(raw_input())
except EOFError:
    pass

for ip in list:
    if " " in ip:
        outfile.write('no network-object ' +(ip))
        outfile.write('\n')
    else:
        outfile.write('no network-object host '+ (ip))
        outfile.write('\n')
outfile.close()

output=open('network_objects.txt')
print output.read()
output.close()