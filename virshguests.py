#!/usr/bin/python
'''
virshguest.py goes out and gets virsh info from some kvms
'''

import subprocess

with open('lists/psphv.txt') as hvs:
    with open('lists/pspvirshguests.txt', 'a') as outfile:
        ppsp_kvms = hvs.readlines()[0:6]
        
        for server in ppsp_kvms:
            name = server.split()[1]
            ip = server.split()[0]    
            user= '$user'
            cmd = ('ssh ' + user + '@' + ip + " 'sudo virsh list --all'")
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            if (p.returncode == 0):
               outfile.write(name + ' ' + ip)
               outfile.write('\n')
               outfile.write(out) 
            else:
                print 'fail'   

with open('lists/psphv.txt') as hvs:
    with open('lists/pspvirshguests.txt', 'a') as outfile:
        rpsp_kvms = hvs.readlines()[6:10]

        for server in rpsp_kvms:
            name = server.split()[1]
            ip = server.split()[0] 
            user = '$user'
            cmd = ('ssh ' + user + '@' + ip + " 'virsh list --all'")
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            if (p.returncode == 0):
                outfile.write(name + ' ' + ip)
                outfile.write('\n')
                outfile.write(out)
            else:
                print 'fail'
