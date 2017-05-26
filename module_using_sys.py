import sys
import os

print('the command line argiuments are: ')
for i in sys.argv:
    print(i)

print(sys.argv[1])

print('\n\nThe PYTHONPATH is',sys.path,'\n')

print(os.getcwd())
