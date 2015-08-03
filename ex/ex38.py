#!/usr/local/bin/python2.7
ten_things = "Apples Orages Crows Telephone Light Sugar"

print "Wait ther's not 10 tihs in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisebee", "Cron", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d itmes now" % len(stuff)

print "There we go : ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()

print ' '.join(stuff)
print '#'.join(stuff[3:5]) 

