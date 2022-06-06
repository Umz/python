import random, os

clear = lambda: os.system('cls')

list = [1, 2, 3]
one, two, three = list
print (list)

list[-1] = 'Coder'
print(list)

list += [10]
print (list)

list *= 2
print (list)

gs = 10;

def func():
    print('This is from a function')
    print('Standard stuff it seems')

func()

clear()

for i in range(5):
    print (random.randint(1, 100))

