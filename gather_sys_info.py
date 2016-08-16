#!/usr/bin/env python

# only work for linux system
import subprocess

def os_func(func_name, func_arg):
    print "gather system info by %s..." %func_name
    subprocess.call([func_name, func_arg])

#command 1
uname = "uname"
uname_arg = "-a"
os_func(uname, uname_arg)

#command 2
diskspace = "df"
diskspace_arg = "-h"
os_func(diskspace, diskspace_arg)

input("Press enter to confirm..")
