# for loops 
# Repetitive execution of the same block of code over and over is referred to as iteration.
# There are two types of iteration:
# Definite iteration, in which the number of repetitions is specified explicitly in advance
# Indefinite iteration, in which the code block executes until some condition is met

for num in range(10):
    print(num)

for num in range(1,10,2):
    print(num)

    
for name in ['John','Terry','Eric','Michael','George']:
    print(name)


print('---------------')
names = ['John','Terry','Eric','Michael','George']

for index, name,  in enumerate(names):
    print(name)

# will set the index num to 1
# The enumerate() function adds a counter to an iterable and returns it (the enumerate object).
for index, name in enumerate(names,1):
    print(f'{index}: {name}')


languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

# convert enumerate object to list
print(list(enumerate_prime))

# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]


# Tuples
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable and allow duplicate value
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# and we can access the elements inside a tuple with an index.

thistuple = ("apple", "banana", "cherry", "cherry")
print(thistuple)

# Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# dictionary is a set of key: value pairs, with the requirement that the keys are unique 
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict['brand'])
# get return none insted of error
print(thisdict.get('lala'))
#after get we can add a message that will apear if the key is not found
print(thisdict.get('x', 'non found'))
print(len(thisdict))
thisdict['price'] = 2500
del thisdict['brand']
print(thisdict)
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
for key, value in movie.items():
    print(key, value)


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)