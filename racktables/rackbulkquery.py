#!/usr/bin/env python
from __future__ import print_function
import sys

def gather_names(filename):
    """Look through a file with one name per lines and return a list."""
    guestlist = []
    with open(filename) as f:
        for line in f:
            line = line.strip('\n')
            line = guestlist.append(line)
        return guestlist

def make_directory(racktables):
    """Return a directory of name:ipaddr pairs."""
    d = {}
    with open(racktables) as g:
        for l in g.readlines():
            # Evaluate the tuple strings in the txt file
            # into actual tuples in python
            tup = eval(l.strip())
            name, ipaddr = tup[0], tup[1]
            d[name] = ipaddr
    return d

def main():
    """find the IP addresses of hosts from a list of names."""
    directory = make_directory(racktables='lists/rackips.txt')
    names = gather_names(filename='lists/pspguests.txt')

    for n, i in directory.items(): 
        for line in names:
            if line in n:          
                print('Full match: "{}" is at: {}'.format(n, i))


if __name__ == '__main__':
    main()
