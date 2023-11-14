#!bin/bash
users=$(bash sondeUser.sh)
espace=$(bash sondeDisk.sh)
ram=$(python3 sondeRAM.py)
cpu=$(python3 sondeCPU.py)
for ut in $users; do
	echo "utilisateur : "
	util=$(who |awk '{print $1}')
	echo $util
	echo "espace utilisé :"
	echo $espace
	echo "ram % : "
	echo $ram
	echo "cpu % : "
	echo $cpu
done

