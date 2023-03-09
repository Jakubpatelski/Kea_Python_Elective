# User input
name = input("what is your name?")
age = input("what is your age?")
print('Hello '+ name + '! You are '+ age + ' years old.')

num1=input('Enter a digit: ')
num2=input('Enter a second number:')
# we will be ijecting string so we need to convert it
answer=float(num1)+float(num2)
print(answer)

name2 =  input("what is your name?")
distance =  input("what is your distance in km?")
convert = round(float(distance)/1.609)
answer2 = f"helllo {name2}, your distance in km is {distance} and in miles {convert}."
print(answer2)