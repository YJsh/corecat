#!/bin/bash
PID=`ps aux|grep "./manage.py runserver 0.0.0.0:9000"|grep -v grep|awk '{print $2}'`
echo syj | sudo -S kill ${PID}

sleep 2

echo syj | sudo -S ./manage.py runserver 0.0.0.0:9000 >> run.log 2>&1 &

