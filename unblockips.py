#!/usr/bin/python
#unblockblockips.py
#This script takes a list of ips and adds cisco commands to them
#so we can UNblock the heathens.
outfile=open('network_objects.txt', 'w')
with open("asaips.txt") as f:
    ips = f.read().splitlines()
for ip in ips:
    if " " in ip:
        outfile.write('no network-object ' +(ip))
        outfile.write('\n')
    else:
        outfile.write('no network-object host '+(ip))
        outfile.write('\n')
outfile.close()
