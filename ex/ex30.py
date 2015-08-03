#!/usr/local/bin/python2.7

people = 30
cars = 40
buses = 15

if cars > people:
	print "We shoud take the cars"
elif cars < people:
	print "We shoud not take the cras"
else:
	print "We cant'decide"


if buses > cars:
	print "That's too many buses"
elif buses < cars:
	print "Maybe we coudl take the buses"
else:
	print "We still can't decide"

if people > buses:
	print "Alright, let's just take the buses"
else:
	print "Fine, let's stay home then"




