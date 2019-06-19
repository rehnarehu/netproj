#!/usr/bin/env bash

# author: github.com/jbdrvl
# date: November 2017

RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
ORANGE='\033[1;35m'
NC='\033[0m'
echo ""
### DISPLAY HELP INFO
help_function()
{
	local bold=$(tput bold)
	local normal=$(tput sgr0)
	echo "${bold}NAME"
    echo "		${normal}connect.sh - connects host to a remote machine using <netcat -u> (UDP)"
	echo "${bold}SYNOPSIS"
	echo "		${normal}connect.sh [OPTIONS] -a ip_address -p port"
	echo "${bold}DESCRIPTION"
	echo "		${normal}This script takes as argument an IP address and a port and connects to them using netcat and the UDP protocol."
	echo "		${bold}-h, --help"
	echo "			${normal}displays this help menu"
	echo "		${bold}-a, --address"
	echo "			${normal}IP address of the remote machine the user wants to connect to."
	echo "		${bold}-p, --port"
	echo "			${normal}port of the remote machine used for the UDP connection. The port needs to be open and listening for incoming UDP connections."
}

######### VARIABLES #########

# GET PARAMETERS and check their type
while [ "$1" != "" ]; do
	case $1 in
		-h | --help )	clear
				help_function
				exit
				;;
		-a | --address )shift
				IP_ADDRESS=$1
				;;
		-p | --port )	shift
				PORT=$1
				;;
		* ) 		echo -e "${RED}[ERROR]${NC} what is this: $1? This parameter was not expected."
				exit
				;;
	esac
	shift
done

if [[ "$IP_ADDRESS" == "" ]]; then
    echo -e "${GREEN}[INFO]${NC} no IP address so using localhost instead: 127.0.0.1"
    IP_ADDRESS="127.0.0.1"
fi
if [[ "$PORT" == "" ]]; then
    echo -e "${RED}[ERROR]${NC} missing a port"
    exit
fi

echo "About to connect to $IP_ADDRESS:$PORT"
nc -uvv $IP_ADDRESS $PORT
exit
