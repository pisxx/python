#!/usr/local/bin/python2.7

i = 0
numbers = []

def test(a, b):
	numbers.append(a)
	print "At the top is %r " % numbers[0] 
	print numbers
	a += b
	#return numbers
	numbers.append(a)
	print numbers
	print "At the bottom is %r " % numbers[-1] 
	print numbers
	return numbers
#while i < 6:
#	print "At the top i is %d" % i
#	numbers.append(i)
#
#	i = i + 1
#	print "Numbers now: ", numbers
#
#	print "At the bottom i is %d " % i
#
#
#print "The numbers: "
#
#for num in numbers:
#	print num

test(1, 1)
test(1, 2)
test(3, 3)
