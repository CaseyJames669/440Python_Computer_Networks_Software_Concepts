#-------------------------------------------------------------------------------
# Name:        Asmt1
# Purpose:     Quick tutorial run through.
#              It has been a few semesters since Python...
#              Pydocs - docs.python.org/3.3/tutorial
#
# Author:      Casey Bladow
#
# Created:     26/08/2014
# Copyright:   (c) Casey Bladow 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def scope_test():
    def do_local():
        variable = "local variable"
    def do_nonlocal():
        nonlocal variable
        variable = "nonlocal variable"
    def do_global():
        global variable
        variable = "global variable"
    variable = "test variable"
    do_local()
    print("After local assignment:", variable)
    do_nonlocal()
    print("After nonlocal assignment:", variable)
    do_global()
    print("After global assignment:", variable)

scope_test()
print("In global scope:", variable)

class Complex:
     def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart

x = Complex(5.0, -6.7)
x.r, x.i
print(x.r)
print(x.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
    print(x.counter)
print(x.counter)
del x.counter

string = 'Yay to another year...'
print(string)
print(1/7)
a = 10
b = 67
print(a+b)

def fibSeries(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
fibSeries(100)

z = [2,5,6,7,3,3]
print(z)
z.sort()
print(z)
z.reverse()
print(z)

stack = [6,7,8]
stack.append(9)
stack.append(10)
print(stack)
print(stack.pop())
print(stack)

x = int(input("Please enter an integer:"))
if x < 0:
    x=0
    print('Negative number set to 0')
elif x==0:
    print('Zero')
elif x==1:
    print('One')
else:
    print('Greater than 1')

wordBank = ['cat', 'hat', 'doctor', 'suess']
for w in wordBank:
    print(w, len(w))

for i in range(len(wordBank)):
    print(i, wordBank[i])

