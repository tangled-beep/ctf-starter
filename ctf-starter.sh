#!/bin/bash

# ask for box name
echo Enter name of box of challenge
read boxname
#ask for IP
echo Enter IP
read rIP

echo made a new directory! $boxname
mkdir ~/HTB/$boxname
cd ~/HTB/$boxname

echo running wordlist gatherer
python3 ~/ctf-starter/main.py $rIP


echo running an NMAP scan
nmap -sV -sC -v $rIP -oN nmapscan.txt

echo all done! complete scan of $rIP for $boxname