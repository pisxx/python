#!/usr/bin/python
import os
import sys
import pdb

#file_name = 'plik'
file_name = sys.argv[1]
file_size = os.path.getsize(file_name)

pattern = sys.argv[2]
print "File size is  -> %s " % file_size

file_pos = open('pos', 'r')
#pdb.set_trace()
last_pos = int(file_pos.readline().strip("'").rstrip('\n'))

print "Previous last line in file was -> %s " % last_pos
if file_size < last_pos:
    last_pos = 0
if last_pos == file_size:
    print "Nothing new in file"
    sys.exit(1)

with open(file_name, 'rb') as plik:
    try:
        plik.seek(last_pos)
        for line in iter(plik.readline, ''):
            if pattern in line:
                print "------------"
            print "This is line -> %s " % line.strip('\n')
            pos = plik.tell()
            print "This is position in file -> %s " % pos
        print "This is last line in file -> %s " %pos
        with open('pos', 'w') as pos_file:
            pos_file.write(str(pos))
    except Exception, e:
        print e
