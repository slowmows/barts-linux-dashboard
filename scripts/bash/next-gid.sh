#!/bin/bash
LASTGID=$(getent group |gawk -F: '{ print $3 }' |tail -n1)
NEXTGID=$[LASTGID + 1]
echo $NEXTGID
