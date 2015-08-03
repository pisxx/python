#!/usr/local/bin/python2.7

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimmes', 3, 'quarters']

for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit

#mozna robic mixed lists, uzywamy wtedy %r bo nie wiadomo czy to bedzie digit czy string

for i in change:
	print "I got %r" % i

elements = []
elements.extend(range(0, 6))

#for i in range(0, 6):
#	print "Adding %d to the list " % i
#	elements.append(i)

for i in elements:
	print "Element was: %d " % i

