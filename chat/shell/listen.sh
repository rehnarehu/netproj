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
    echo "		${normal}listen.sh - listens to a UDP connection from a remote machine"
	echo "${bold}SYNOPSIS"
	echo "		${normal}listen.sh [OPTIONS] -p port"
	echo "${bold}DESCRIPTION"
	echo "		${normal}This script takes as argument a port and listens for any UDP connection on that port."
	echo "		${bold}-h, --help"
	echo "			${normal}displays this help menu"
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
		-p | --port )	shift
				PORT=$1
				;;
		* ) 		echo -e "${RED}[ERROR]${NC} what is this: $1? This parameter was not expected."
				exit
				;;
	esac
	shift
done

if [[ "$PORT" == "" ]]; then
    echo -e "${RED}[ERROR]${NC} missing a port"
    exit
fi

nc -luvv -p $PORT
echo "Listening for UDP incoming on $PORT"
exit
