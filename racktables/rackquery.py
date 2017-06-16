#!/usr/bin/python
'''This script will take a single argument, either a hostname or IP address,
    and query our Racktables database for information.'''
from __future__ import print_function
from mysqlrackconnect import connection
import argparse
import sys

def parse(query):
    parser = argparse.ArgumentParser()
    parser.add_argument('query', nargs ='*', help='Input a partial or full hostname or IP address')
    args = parser.parse_args()
    try:
        query = args.query[0]
        return query
    except:
        print('\nPlease run the program followed by an Hostname or IP address\n')
        sys.exit()
        
def make_dict(rackdata):
    #Return a dictionary of name:ipaddr pairs.
    d={}
    for name, ipaddr in rackdata:
        d.setdefault(name, ipaddr)
    return d

def main(argv):
    #Send argv to argparse.
    query = parse(argv)
    
    #Open connection to racktables db and ask it for a full dump of hostname:ip associations 
    c, conn = connection()
    c.execute("select name, INET_NTOA(ip) FROM IPv4Address")
    
    #Send the list of tuples recieved to be converted into a dictionary.
    rackdict = make_dict(rackdata = c.fetchall())
    
    for n, i in rackdict.items():
        n, i, query = n.lower(), i.lower(), query.lower()
        if query in n:
             print('{:<50s} ' ' {}'.format(n, i))
        if query in i:
             print('{:<50s} ' ' {}'.format(i, n))
             
    c.close()
    conn.close()

if __name__ == '__main__':
    main(sys.argv)
