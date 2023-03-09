#  sorted() - Return a new list containing all items from the iterable in ascending order, meaning smallest to largest..
numbers = [6, 9, 3, 1]
sorted_numbers = sorted(numbers)# [1, 3, 6, 9]
print(sorted(numbers))
print(sorted_numbers)
# set
numbers_set = {5, 5, 10, 1, 0}
print(sorted(numbers_set)) #[0, 1, 5, 10] it will return list, because sorted() returns a new list by definition. same with tuples

# Sorting Strings
string_value = 'I like to sort'
print(sorted(string_value)) #[' ', ' ', ' ', 'I', 'e', 'i', 'k', 'l', 'o', 'o', 'r', 's', 't', 't']
# sorted() will treat a str like a list and iterate through each element.
#  In a str, each element means each character in the str. sorted() will not treat a sentence differently, and it will sort each character, including spaces.
# .split() can change this behavior and clean up the output, and .join() can put it all back together.
# split() is a built-in function in Python that is used to split a string into a list
# The join() method takes all items in an iterable and joins them into one string.
# join() is a string method that allows you to concatenate a list of strings using a specific delimiter.
string_value = 'I like to sort'
sorted_string = sorted(string_value.split()) #['I', 'like', 'sort', 'to']
sorted_string_join = ' '.join(sorted_string) #I like sort to
print(sorted_string)
print(sorted_string_join)

# Lists With Non-Comparable Data Types Can’t Be sorted()
# non valid
mixed_numbers = [5, "1", 100, "34"]


# this is valid
similar_values = [False, 0, 1, 'A' == 'B', 1 <= 0]
print(sorted(similar_values)) #[False, 0, False, False, 1]
# Even though the elements in the list look different, 
# they can all be converted to Booleans (True or False) and compared to each other using sorted():

# When You’re Sorting Strings, Case Matters
# sorted() can be used on a list of strings to sort the values in ascending order, which appears to be alphabetically by default:

names = ['Harry', 'Suzy', 'Al', 'Mark']
print(sorted(names))#['Al', 'Harry', 'Mark', 'Suzy']

#However, Python is using the Unicode Code Point(numerical value that maps to a specific character) of the first letter in each string to determine ascending sort order.
#This means that sorted() will not treat the names Al and al the same.
# This example uses ord() to return the Unicode Code Point of the first letter in each string:
#ord() - Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.
# For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().
names_with_case = ['harry', 'Suzy', 'al', 'Mark']
print(sorted(names_with_case))#['Mark', 'Suzy', 'al', 'harry']

# List comprehension for Unicode Code Point of first letter in each word
print([(ord(name[0]), name[0]) for name in sorted(names_with_case)]) #[(77, 'M'), (83, 'S'), (97, 'a'), (104, 'h')]
print(chr(65))

# If the first letter is the same, then sorted() will use the second character to determine order,
#  and the third character if that is the same, and so on, all the way to the end of the string:
very_similar_strs = ['hhhhhd', 'hhhhha', 'hhhhhc','hhhhhb']
print(sorted(very_similar_strs))#['hhhhha', 'hhhhhb', 'hhhhhc', 'hhhhhd']

# Strings that contain identical values will end up sorted shortest to longest due to the shorter strings not having elements to compare to with the longer strings:
different_lengths = ['hhhh', 'hh', 'hhhhh','h']
print(sorted(different_lengths))#['h', 'hh', 'hhhh', 'hhhhh']

# Using sorted() With a reverse Argument
# If reverse is assigned True, then the sorting will be in descending order
numbers = [6, 9, 3, 1]
num_sorted_reverse = sorted(numbers, reverse=True)#[9, 6, 3, 1]
print(num_sorted_reverse)
names = ['Harry', 'Suzy', 'Al', 'Mark']
print(sorted(names, reverse=True))

# sorted() With a key Argument
# This argument expects a function to be passed to it, then it will bve sorted based on the argument provided
# "limitations": First, the number of required arguments in the function passed to key must be one.
# The second limitation is that the function used with key must be able to handle all the values in the iterable.

words = ['banana', 'pie', 'Washington', 'book']
print(sorted(words, key=len))#['pie', 'book', 'banana', 'Washington']

values_to_cast = ['1', '2', '10', '3']
print(sorted(values_to_cast, key=int))


#  order an iterable by the last letter, The word[::-1] slice syntax is used to reverse a string. 
# Each element will have reverse_word() applied to it, and the sorting order will be based on the characters in the backwards word.
words = ['banana', 'pie', 'Washington', 'book']
def word_reverse(word):
    return word[::-1]

print(sorted(words, key=word_reverse))


def word_reverse(word):
    return [s[::-1] for s in words]

print(word_reverse(words))



# lambda
# A lambda is an anonymous function that: Must be defined inline, Doesn’t have a name,
# Can’t contain statements, Will execute just like a function
words = ['banana', 'pie', 'Washington', 'book']
# the argument taken by the lambda is x, and x[::-1] is the operation that will be performed on the argument, x[::-1] is called on each element 
print(sorted(words, key=lambda word: word[::-1]))
print(sorted(words, key=lambda word: word[::-1], reverse=True))

# .sort()
# .sort() is a method in the list object.
# Avoid using this, instead use sorted()
# Reason:
# * sorted() can be used on all ‘iterable objects’, .sort() only works on lists.
# * sorted() does not change the original list, .sort() does.
