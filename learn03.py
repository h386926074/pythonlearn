for i in range(1,5):
    print(i)
else:
    print('the for loop is over')

x= 50

def func():
    global x
    print('x is',x)
    x = 2
    print('changed golbal x to',x)

func()
print('value of x is',x)

def total(a=5,*numbers,**phonebook):
    'my name haha'
    print('a',a)
    for single_item in numbers:
        print('single_item',single_item)

    for first_part,second_part in phonebook.items():
        print(first_part,second_part)

print(total(110,1,2,3,jack=1123))
print(total.__doc__)


#DocStrings
