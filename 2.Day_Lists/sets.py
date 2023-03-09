#  Lists are used to store multiple items in a single variable.
# A set is an unordered collection with no duplicate elements but are very fast

footabllers= {'ronaldo', 'messi', 'ronalidnho', 'kane'}
footabllers_english= {'rashford', 'dice', 'pickford', 'kane'}
print(footabllers)
# will print those that are in both -  intersection() 
print(footabllers.intersection(footabllers_english))
# will print those that are NOT in both - difference()
print(footabllers.difference(footabllers_english))
# put them together - union()
print(footabllers.union(footabllers_english))
print('orange' in footabllers)
print('ronaldo' in footabllers)

comprehension = {footballer for footballer in footabllers if footballer != 'ronaldo'}
print(f'comprehen {comprehension}')

#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
# . Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary,
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
a - b                              # letters in a but not in b
{'r', 'd', 'b'}
a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # letters in both a and b
{'a', 'c'}
a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}

#Sets - Exercise


friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
print('--------------')
#1. Check if ‘Eric’ and ‘John’ exist in friends
print('Eric' and 'John ' in friends)
#2. combine or add the two sets 
print(friends.union(my_friends))
#3. Find names that are in both sets
print(friends.intersection(my_friends))
#4. find names that are only in friends
print(friends.difference(my_friends))
#5. Show only the names who only appear in one of the lists
print(friends ^ my_friends)
print(friends.symmetric_difference(my_friends))
#6. Create a new cars-list without duplicates
cars_without_duplicate = set(cars)
print(cars_without_duplicate)

