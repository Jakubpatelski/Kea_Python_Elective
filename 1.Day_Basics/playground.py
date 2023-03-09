# strings in python are unmutable to you cannot change them you can assign them to another instance
msg = "welcome to the tets message"
print(msg, msg)

print(msg.upper())
print(msg.lower())
# first letter is cpatialize
print(msg.capitalize())
print(msg.title())
# length of the string
print(len(msg))
# counting how many o are in a given string
print(msg.count('o'))

# slicing
fullName = "Mike Jordan"
print(fullName[1])

# this will take 2 and  evething after index 2
slice = fullName[2:]
print(slice)
# will take from 2 to 5(6 is not inclusive)
sliceEnd = fullName[2: 6]
print(sliceEnd)

# will take from 0 to 5
sliceBegin = fullName[:6]
print(sliceBegin)

# [start:end:step], The [::-1] slice returns the reverse of the sequence
#  by starting at the end of the sequence and counting backwards by step of -1,
#  effectively reversing the order of elements in the sequence.
sliceEnd = fullName[::-1]
print(sliceEnd)

# multi line string with """
msg="""Dear Terry,,
You must cut down the mightiest 
tree in the forest with…
a herring! <3"""
print(msg)

msg = "hello i am learning Python"
print(msg.find('hello')) #it will print index from where it starts

print(msg.replace('learning', 'know'))

print('Python' in msg)

name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color + '!'
print(msg)

msg = '[' + name.lower() + '] loves the color ' + color + '!'
print(msg)


