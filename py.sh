#!/bin/bash

if [ -f $1.py -o -f $1 ]
then
	if [[ $1 != *".py"* ]]
	then
		vim $1.py
	#elif [[ $1 == *".py"* ]]
	else
	#then 
		vim $1
	fi
#elif [[ $1  == *"py" ]]
#then
#	vim $1.py
elif [ ! -f $1.py -o ! -f $1 ]
then
	#echo -e '#!/usr/bin/python\n' > $1.py
	echo -e '/usr/local/bin/python2.7\n' > $1.py
	chmod +x $1.py
	vim $1.py
fi

