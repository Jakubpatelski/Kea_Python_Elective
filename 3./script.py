import string
alphabet = list(string.ascii_uppercase)
alphabet2 = [i for i in string.ascii_uppercase]
print(f'alphabet2 {alphabet2}')
print(alphabet)


# The chr() method converts an integer to its unicode character and returns it.
# The ord() function returns an integer representing the Unicode character.

capital_letters = [chr(i) for i in range(ord("A"), ord("Z") +1)]
excluded_code_points = [70, 75, 80, 85]

print(capital_letters)
exclude = [i for i in capital_letters if ord(i) not in excluded_code_points]
print(f'exclude {exclude}')

# print(exclude)
capital_letters2 = [chr(i) for i in range(ord('A'), ord('Z')+1) if ord(chr(i)) not in excluded_code_points]
print(capital_letters2)
capital_letters4 = [i for i in range(ord("A"), ord("Z") +1)]

remove = [chr(i) for i in range (65, 91) if i not in [70,75,80,85]]
print(f'remove {remove}')

# range last parameter gives the step
ex3 = [chr(i) for i in range (65, 91) if i not in range(70, 80, 2)]
print(ex3)

# nested list comprehensions
l = []
for i in range(3):
    for j in range(2):
        l.append((i,j))

print(l)

li_nested = [(i,j) for i in range(3) for j in range(2)]
print(f'nested {li_nested}')

l1 = [i if i%2==0 else 'Hello' for i in range(10)]
print(l1)

# Ex 2: Clothes List Comprehension
# [(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

clothes = [(color, size) for color in colors for size in sizes]
print(clothes)

soled_out = [('Black', 'm'), ('White', 's')]
stock = [(color, size) for color in colors for size in sizes if (color, size) not in soled_out]
print(stock)

stock_2 = [(c,s) for c in colors for s in sizes if (c,s) not in [('Black', 'm'), ('White', 's')]]
print(stock_2)

