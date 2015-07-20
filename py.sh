#!/bin/bash

if [ -f $1.py -o -f $1 ]
then
vim $1
elif [ ! -f $1.py -o ! -f $1 ]
then
touch $1.py
echo -e '#!/usr/bin/python\n' >> $1.py
chmod +x $1.py
vim $1.py
fi

