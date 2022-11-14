#!/bin/sh

HOST="10.2.6.10"

USER="alliman"

PASSWD="alliman"

FILE="file.txt"

ftp -n $HOST <<END_SCRIPT

quote USER $USER

quote PASS $PASSWD

put $FILE

quit

END_SCRIPT