#!/usr/local/bin/python2.7

print "You enter a dark room with two droors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do ?"
	print "1. Take the cake."
	print "2. Scream at te bear"

	bear = raw_input("> ")

	if bear == "1":
		print "The eats your face off."
	elif bear == "2":
		print "Yhe bear eats your legs off"
	else:
		print "Well, doing %s is probably better. Bear rusn away" % bear

elif door == "2":
	print "you stare into the endless abyss at Cthulu's retina"
	print "1. Blueberries"
	print "2. Yellow jacket clothspins"
	print "3. Understanding revolvers yelling melodies"

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job"
	else:
		print "The insanity rots your eyes into a pool of muck"

else:
	print "You stumble around and fall on a knife and die"
