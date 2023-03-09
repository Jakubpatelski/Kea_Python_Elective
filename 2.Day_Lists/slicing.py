# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
# ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
# ('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
# 'Hello World Huston we are here' -> 'World Huston we'

list1 = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
list1Edit  = list1[1:-1]
print(list1Edit)
list2Edit = list1[:2]
print(list2Edit)
list3Edit = list1[4:-1]
print(list3Edit)
list4Edit = list1[::2]
print(list4Edit)
list5Edit = list1[::-1]
print(list5Edit)
list6Edit = list1[1:-1]
print(list6Edit)
string = 'Hello World Huston we are here'
stringEdit = string[6:21]
print(stringEdit)

print('------------------------')


names = ['George', 'Bejamin', 'Thomas', 'John']

print(len(names))
print(list(names))
# print(map(lambda x: x + 'a', names))
print(str(names))
print(all(names))

print('------------------------')

# Create a function that takes a string as a parameter and returns a list.
# The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.

def remove_vovels(s):
    # isaplha() Check if all the characters in the text are letters:

    vowels = set("aeiouAEIOU")
    # vowels = ['a','e','i','o','u']
    # List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

    consonants = sorted(v for v in s if v not in vowels and v.isalpha())

    return consonants 


print(remove_vovels("hejwhatsupbro222"))
print('--------------------')
# 3.
# Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
# Sort this list by using the sorted() build in function.
# Sort the list in reversed order.
# Sort the list on the lenght of the name.
# Sort the list based on the last letter in the name.
# Sort the list with the names where the letter ‘a’ is in the name first.

l = ['Claus', 'Ib', 'Per']
l_sorted = sorted(l)
print(l_sorted)
l_sorted_reverse = sorted(l, reverse=True)
print(l_sorted_reverse)
l_sorted_name = sorted(l, key=len)
print(l_sorted_name)
l_sorted_last_letter = sorted(l, key=lambda x: x[-1])
print(l_sorted_last_letter)
l_sorted_name_a = sorted(l, key=lambda x: 'a' not in x)
print(l_sorted_name_a)

print('------------------------')

# Ex 4: Text editor plugin simulation
s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'
# Count the number of characters including blank spaces.
s_count = len(s)
print(f'String s has {s_count} characters including blank spaces ')

# Count the number of characters excluding blank spaces.
s_replace = s.replace(" ", "")
s_without_space = len(s_replace)
print(f'String s has {s_without_space} characters excluding blank spaces ')

# Count the number of words.
split = s.split() #split string into list of strings 
count_words = len(split)
print(f'String s has {count_words} words ')

print('------------------------')

# Ex 4: Files
# Create a file and call it lyrics.txt (it does not need to have any content)

# f = open("lyrics.txt", "x")
# Create a new file and call it songs.docx and in this file write 3 lines of text to it.

# f = open("songs.txt", "x")
# f.write("I am a song lalal \n")
# f.write("i am song but 2nd line \n")
# f.write("i am 3rd line \n")
# f.close()
# open and read the content and write it to your terminal window.
# * you should use both the read(), readline(), 
# and readlines() methods for this. (so 3 times the same output).

read_file = open('songs.txt', 'r')
print(read_file.read()) #reads entire file
# print(read_file.readline()) #reads one line
# print(read_file.readlines()) #eads all of the lines and returns them as string elements in a list, one for each line.

# Ex 5: Sort a list of tuples
print('------------------------')


my_list = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5),(10,4),(10,1),(3,1)]
my_list_sorted = sorted(my_list, key=lambda x: (x[1], x[0]))
print(my_list_sorted)