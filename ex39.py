# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'Califorrnia': 'CA',
	'NewYork': 'NY',
	'Michigan': 'MI'
}
	
# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
} 

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY state has:", cities['NY']
print "OR state has:", cities['OR']

# print some states
print "-" * 10
print "Michigan's abreviation is:", states['Michigan']
print "Florida's abbreviation is:", states['Florida']

# do it y using the state then cities dict
print "-" * 10
print "Michigan has:", cities[states['Michigan']]
print "Florida has:", cities[states['Florida']]

# print every state abbreviation
print "-" * 10
for state, abbrev in states.items():
	print "%s is abbreviated as %s." %(state, abbrev)
	
# print every city in the state
print "-" * 10
for state, city in cities.items():
	print "%s has the city %s" %(state, city)
	
# now do both at the same time
print "-" * 10
for state, abbrev in states.items():
	print "The state %s is abbreviated as %s and has city %s" % (
		state, abbrev, cities[abbrev])
		
print "-" * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."
	
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city