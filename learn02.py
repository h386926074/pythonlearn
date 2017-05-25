# -*- coding: UTF-8 -*-
print('hello world')
age = 1
name= 'haungfeng'
print("my name is {}, my age is {}".format(name,age))

#hello world

myname = '''这是一个多行字符串，这是它的第一行
        THIS IS THE SECOND LINE.
        '''
print(myname +' is ' + name)

print('{0:.3f}'.format(1.0/3))  #保留小数后几位
print('{0:_^11}'.format('hello'))
print('{name} wrote {book}'.format(name='huangfeng',book='a byte of python'))

#print('a',end= '')
#print('b',end= '')

print(r'what\'s \t my')

number = 23
guess = int(input('enter an integer: '))
if guess==number:
    print('congratulations,you guessed it')
elif guess < number:
    print('No,it is a litter higher than that.')
else:
    print('No.it is a litter lower than that')


    
