#!/usr/local/bin/python2.7
print "Let's practice everything"
print 'You\'d need to know \'bout escapes with \\ that do \n newlins and \t tabs'

poem = """
\t The lovely world
with logic so firmly platend
cannot discren \n 
the needs of love
nor compregend passion from intuition
and requires and explanation
\n\t\t where there is none.
"""


print "--------------------"
print poem
print "--------------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 1000
beans, jars, crates = secret_formula(start_point)

print "With a starging point of: %d " % start_point
print "We'd have %d beans, %d jars, and %d crates " % (beans, jars, crates)

start_point = start_point / 10 

print "We can also do that this way: "
print "We'd have %d beans, %d jars, and %d crates" % secret_formula(start_point)
