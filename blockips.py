#!/usr/bin/python

"""
blockips.py
This takes a list of ips and adds cisco commands to them
so we can unblock the heathens. After you paste hit return if there is not a newline,
then Control+D to send.
"""

import sys


def main():
    with open('network_objects.txt', 'w') as outfile:
        print('Paste the IPs here followed by Ctrl D to add Cisco commands:')
        inputs = sys.stdin.read()
        candidate_list = inputs.split('\n')

        for ip in candidate_list:
            if " " in ip:
                outfile.write('no network-object {}\n'.format(ip))
            else:
                outfile.write('no network-object host {}\n'.format(ip))

    with open('network_objects.txt') as output:
        print(output.read())

if __name__ == '__main__':
    main()