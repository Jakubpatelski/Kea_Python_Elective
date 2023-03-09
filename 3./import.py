import sys 

def greeting(x):
    print(x)
    if len(x) ==2 and x[1] == '-it':
        print('interaqctive terminal started')
    if len(x) == 3 and x[2] == '--rm':
        print("will be removed at exit ")
    if len(x) ==1:
        print('Usage: python script.py [-it]{--rm}')

greeting(sys.argv)