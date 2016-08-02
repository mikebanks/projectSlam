#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title:              ipBlocker.py
#author:          Michael Banks
#date:              01 Aug 2016
#version:         1.0
#usage:            sudo python ipBlocker.py
#notes:             must be root
#python_version  :2.7
#=======================================================================
import sys, re, os, platform

OS = platform.system()

if not os.geteuid() == 0:
    sys.exit('Script must be run as root!')

try:
    if sys.argv[1:]:
        print "File: %s" % (sys.argv[1])
        logfile = sys.argv[1]
    else:
        logfile = raw_input(
            "Please enter a file to parse, e.g /var/log/secure: ")
    try:
        file = open(logfile, "r")
        ips = []
        for text in file.readlines():
            text = text.rstrip()
            found = re.findall(
                r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',
                ext)
            if found:
                ips.extend(found)
        ips = list(set(ips))
        for ip in ips:
            IP = "".join(ip)
            if IP is not '':
                if OS == "Windows":
                    #WIN
                    cmd = "netsh advfirewall firewall add rule name=" + '"IP Block"' + " dir=in interface=any action=block remoteip=" + IP + " + /32"
                    print cmd
                    #os.system(cmd)
                    print "IP: %s (Blocked)" % (IP)
                elif OS == "Linux":
                    #Linux
                    cmd = "iptables -I INPUT -s " + IP + " -j DROP"
                    print cmd
                    #os.system(cmd)
                    print "IP: %s (Blocked)" % (IP)
                elif OS == "Darwin":
                    print "MAC Commad Comming Soon"
                    break
                    #MAC
                    #cmd = "MAC Commad"
                    #print cmd
                    #os.system(cmd)
                    #print "IP: %s (Blocked)" % (IP)
                else:
                    print "Don't Recognize Operating System... Exiting..."
                    break
    finally:
        file.close()
except IOError, (errno, strerror):
    print "I/O Error(%s) : %s" % (errno, strerror)
