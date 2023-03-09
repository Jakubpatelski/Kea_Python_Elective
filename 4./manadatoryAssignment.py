print('1.')
# Model an organisation of employees, management and board of directors in 3 sets.
directores =  {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}

management = {'Tine', 'Trunte', 'Rane'}

employees =  {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

# who in the board of directors is not an employee?
directores_not_employee = directores.difference(employees)
print(directores_not_employee)
# who in the board of directors is also an employee?
directores_employee = directores.intersection(employees)
print(directores_employee)
# how many of the management is also member of the board?
management_directories_length = len(management.intersection(directores))
print(management_directories_length)
# All members of the managent also an employee
management_employee = management.intersection(employees)
print(management_employee)
# All members of the management also in the board?
management_directories = management.intersection(directores)
print(management_directories)
# Who is an employee, member of the management, and a member of the board?
employees_management_directores = employees.intersection(management).intersection(directores)
print(employees_management_directores)
# Who of the employee is neither a memeber or the board or management?
employees_not_management_not_directores = employees.difference(directores).difference(management)
print(employees_not_management_not_directores)


print('---------------------')
print('2.')


# 2.Using a list comprehension create a list of tuples from the folowing datastructure
data_structure = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}
tuples_list = [(key, value) for key, value in data_structure.items()]
print(tuples_list)



print('---------------------')
print('3.')

# 3. From these 2 sets:
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}

set2 =  {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

 
# Of the 2 sets create a:
# Union
union_sets = set1.union(set2)
print(union_sets)

# Symmetric Difference
symetric_difference = set2.difference(set1)
print(symetric_difference)

# difference
difference_set = set1.difference(set2)
print(difference_set) #returns set() ->  means that there are no elements in set1 that are not present in set2.

#disjoint
disjoint = set1.intersection(set2)
print(disjoint)



print('---------------------')
print('4.')

month_dict = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAY': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SEP': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12
}

def decode_date(date_string):
    # split the date string into day, month, and year using "-"
    day, month_name, year = date_string.split("-")
       
    # translate the month name to a number using the month_dict
    month = month_dict[month_name.upper()]
    # fix year which is not ideal 
    year = '20' + year if int(year) <= 22 else '19' + year
    
    return (year, month, day)




print(decode_date('8-mar-21'))




