#!/bin/bash
PID=`ps aux|grep "./manage.py runserver 0.0.0.0:9000"|grep -v grep|awk '{print $2}'`
echo syj | sudo -S kill ${PID}
