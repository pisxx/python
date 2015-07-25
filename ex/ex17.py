#!/usr/local/bin/python2.7
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s " % (from_file, to_file)

#zrobic to w jednej lini

#in_file = open(from_file)
#indata = in_file.read()
#jedna linai

#indata = open(from_file).read().close(from_file)
#otwiera i zamkya odrazu
with open(from_file, 'r') as indata:
	indata = indata.read()	

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists ? %r " % exists(to_file)
print "Ready, hit RETURN to continue, ctrl-c to abort"
raw_input()

#dwie linie
#out_file = open(to_file, 'w')
#out_file.write(indata)

#jedna linia
#outdata = open(to_file, 'w').write(indata).close(to_file)
#otwiera i zamyka w jednej lini
with open(to_file, 'w') as outdata:
     outdata.write(indata)


print "Alright, all done"

#indata.close()
#to_file.close()

#out_file.close()
#in_file.close()

