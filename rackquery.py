#!/usr/bin/env python
from __future__ import print_function
from mysqlrackconnect import connection
import sys


def main(query):
    
    output = c.fetchall()
    
    c, conn = connection()
    c.execute("select name, INET_NTOA(ip) FROM IPv4Address")
    

    for n, i in output.items(): 
            if query in n:          
                print('Full match: "{}" is at: {}'.format(n, i))

    c.close()
    conn.close()

if __name__ == '__main__':
    main(query=sys.argv[1])
