#!/bin/sh
if [ -f english.chow ]
then
	rm -rf *.chow
	echo "chow files deleted"
fi 

if [ "$1" == "0" ]
then
	echo "exiting"
	exit
else
	echo "updating dictionary"
	py load_dictionary.py
	echo "dictionary updated"
fi

while true; do py checker.py; done
