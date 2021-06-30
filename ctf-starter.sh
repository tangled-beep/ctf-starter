#!/bin/bash

# ask for box name
echo Enter name of box of challenge
read boxname
#ask for IP
echo Enter IP
read rIP



mkdir
nmap -sV -sC -oN $rIP nmapscan.txt