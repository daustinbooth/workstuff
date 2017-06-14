def make_dict(rackdata):
    #Return a dictionary of name:ipaddr pairs.
    
    d={}
    for name, ipaddr in rackdata:
        d.setdefault(name, ipaddr)
    return d

def main(query):

    #Open connection to racktables db and ask it for a full dump of hostname:ip associations 
    c, conn = connection()
    c.execute("select name, INET_NTOA(ip) FROM IPv4Address")
    
    #Send the list of tuples recieved to be converted into a dictionary.
    rackdict = make_dict(rackdata = c.fetchall())
    
    #Loop through dictionary to find match.
    for n, i in rackdict.items(): 
        if query in n:
            print ('The host "{}" has an IP of {} in Racktables.').format (n, i)
        if query in i:
            print ('The IP {} is associated with "{}" in Racktables.').format(i, n) 

    c.close()
    conn.close()

if __name__ == '__main__':
    main(query=sys.argv[1])
