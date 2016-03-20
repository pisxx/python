#!/usr/bin/python
import os
import sys
import pdb

#file_name = 'plik'
file_name = sys.argv[1]
file_size = os.path.getsize(file_name)

pattern = sys.argv[2]
print "Wielkosc pliku to -> %s " % file_size

file_pos = open('pos', 'r')
#pdb.set_trace()
last_pos = int(file_pos.readline().strip("'").rstrip('\n'))

print "Poprzednia ostatnia linia  w pliku to -> %s " % last_pos
if file_size < last_pos:
    last_pos = 0
if last_pos == file_size:
    print "Nie ma nic nowego"
    sys.exit(1)

with open(file_name, 'rb') as plik:
    try:
        plik.seek(last_pos)
        for line in iter(plik.readline, ''):
            if pattern in line:
                print "------------"
            print "to jest linia -> %s " % line.strip('\n')
            pos = plik.tell()
            print "to jest polozenie w pliku -> %s " % pos
        print "To jest ostatnia linia w pliku -> %s " %pos
        with open('pos', 'w') as pos_file:
            pos_file.write(str(pos))
    except Exception, e:
        print e
