#!/bin/bash
#sleep 180
podstat=`kubectl get pod -A`
stat=`kubectl get pod -A |grep -v NAME|grep -v Running|wc -l`
echo $stat
if [ $stat -gt 0 ]
then
	echo "Check pod status,there is some potential error"
	kubectl get pod -A |grep -v NAME|grep -v Running
	exit 1
else
	echo "Pod is up and running \n $podstat"

fi

