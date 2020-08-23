#!/bin/bash
if ping -c 1 -W 1 192.168.1.2 &>/dev/null; then
	echo -e "at home"
	python3 control_triode.py
else
	echo -e "not at home"
fi