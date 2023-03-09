msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(msg.split()) #will split by word into list
print(csv.split(','))
print('-'.join(friends_list)) #will split by index
print('-'.join(msg) + ' test')#will split by word
print('-'.join(friends_list + friends_list)) #will split by index


print(''.join(msg.split())) # WelcometoPython101:SplitandJoin
# will to the same
print(msg.replace(' ', ''))
print(msg.replace(' ', '-'))

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# print(','.join(csv.split(';')))
# print(','.join(csv.split(';')).split(':'))
# print(','.join(','.join(csv.split(';')).split(':')))
print((','.join(','.join(csv.split(';')).split(':'))).split(','))
print('replace', csv.replace(';',',').replace(':',',').split(','))


#Tuples - faster Lists you can't change(they are immutable)
friends_tuple = ('John','Michael','Terry','Eric','Graham')

