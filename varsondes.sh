#!/bin/bash 
util=$(who | awk '{print $1}' | sort | uniq)
espace=$(bash sondeDisk.sh)
ram=$(python3 sondeRAM.py)
cpu=$(python3 sondeCPU.py)
dateactuel=$(bash datesonde.sh)
