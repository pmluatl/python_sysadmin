#!/usr/bin/env bash

UNAME="uname -a"
printf "Gathering system info with $UNAME command\n\n"
$UNAME

DISKSPACE="df -h"
printf "Gathering system info with $DISKSPACE command\n\n"
$DISKSPACE


