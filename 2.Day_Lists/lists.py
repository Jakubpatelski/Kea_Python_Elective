friends = ['John','Michael','Terry','Eric','Graham', 'Terry']

print(friends[1],friends[4])
print(len(friends))
print(friends.index('Eric'))
print(friends.count('Terry'))

ascending = sorted(friends)
print(ascending)
reverse = sorted(friends, reverse=True) #reverse order of list
print(reverse)
bank = [1,200,20,30]
sumNum = sum(bank)
print(sumNum)
max_value = max(bank)
print(max_value)
friends.append("Jakub") #list.append(value) will add value to the array
print(friends)
friends.insert(0,"mike")
print(friends)
friends[0] = 'Robero'
print(friends)
# extend list
# friends.extend(bank)
# print(friends)

friends.remove('Terry')
friends.pop() #remove the last index or friends.pop(1) that remove sgiven index
print(friends)
# friends.clear() will clear the list
# del friends #will delete the list
del friends[0]
print(friends)

new_friends = friends
print()
print(new_friends)


# exercise
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
day = input("Eneter a number of sold lemonades: ")
sales_w2.append(int(day))
print(sales_w2)
# sales.extend(sales_w1)
# sales.extend(sales_w2)
sales = sales_w1 + sales_w2
print(sales)
sales.sort()
print(f"sorted: {sales}")
lemonade_sum = sum(sales)
print(f'Sum of sold lemonades: {lemonade_sum}')
total_profit = lemonade_sum * 1.5
best_day = max(sales) * 1.5
worst_day = min(sales) * 1.5
print(f'Total profit: {total_profit} \nBest day {best_day}\nWorst day {worst_day}')

# list comprehension = a way to create a new list with less syntax, easire to read
# lis = [expression for item in iterable]

