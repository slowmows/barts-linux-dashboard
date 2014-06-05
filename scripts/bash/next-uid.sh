#!/bin/bash
LASTUID=$(getent passwd |gawk -F: '{ print $3 }' |tail -n1)
NEXTUID=$[LASTUID + 1]
echo $NEXTUID
