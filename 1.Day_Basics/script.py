
import sys

def message(x):
    if x[1] == 'Jakub':
        print('Hello '  + x[1])
    else:
        print('No No No')
    

message(sys.argv)

