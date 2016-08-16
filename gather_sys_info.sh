#!/usr/bin/env bash


function os_func()
{
   printf "Gathering system info with $1 command\n\n"
   $1 $2 
}

UNAME="uname -a"
os_func $UNAME
DISKSPACE="df -h"
os_func $DISKSPACE

