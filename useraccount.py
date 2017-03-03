import subprocess
import shutil
import os
from fabric.api import *
from os.path import isfile, join
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

ltpop_list=['10.1.250.1','10.1.250.2','10.1.250.3','10.1.250.8','10.1.250.5','10.1.250.7','10.1.250.10','10.1.250.11','10.1.251.1','10.1.251.2','10.1.251.3','10.1.251.4','10.1.251.5','10.1.251.6','10.1.251.7','10.1.251.8','10.1.251.9','10.1.251.11','10.1.251.12','10.1.251.13','10.1.251.14','10.1.251.15','10.1.251.16','10.1.251.17','10.1.251.18','10.1.251.19','10.1.250.111','10.1.250.112','10.1.250.113','10.1.250.114','10.1.250.115','10.1.250.116','10.1.250.117','10.1.250.118','10.1.250.119','10.1.250.121','10.1.250.122','10.1.250.131','10.1.250.132']
#ltpop_list=['10.1.250.132']
winpopuser = "$USER"
nowdate=datetime.now()


for ip in ltpop_list:
    nowtime = datetime.now()
    nowtime = nowtime.strftime('%H%M%S')
    mountdir = "/mnt/" + ip + "-" + nowtime
    mount_cmd="mount -t cifs //%s/f$ -o,ro,user=%s,pass=$PASS %s" % (ip, winpopuser, mountdir)
    mkdir_cmd="mkdir %s" % mountdir
    rmdir_cmd="rmdir %s" % mountdir

    with hide('everything'):
        print "\nMounting: %s" % mountdir
        local(mkdir_cmd)
        local(mount_cmd)
        print ''
        print ip
        usercmd = 'ls -1 ' + mountdir + '/Inetpub/mailroot/Mailbox/*/'
        domainlist = subprocess.Popen(usercmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = domainlist.communicate()
        for user in out.splitlines():
            if '@' in user:
                print user

        local("umount %s" % mountdir)
        local(rmdir_cmd)
        print "Umounted: %s" % mountdir
