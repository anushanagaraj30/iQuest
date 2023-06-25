#program
'''x=1 
y=9
print("sum=",x+y)
print(type(x))
print(type(y))
x=y=20
print("sum=",x+y)
x,y=10,20
print("sum=",x+y)
a=5
print(id(a))
b=5
print(id(b))'''


'''Operators:symbols which are used to operate on variables
Types of operators:
1.Arithmetic: +,-,*,/,%,**
2.Logical: AND,OR,NOT
3.Bitwise:NOR,NAND,XOR
3.Relational:==,<,>,<=,>=
4.Increment/Decremental:++,--
5.Assignment: =,+=,-=
6.Membership Operators:'''

#program
'''a=1       
b=2
c=15.5
d=10
output=a+b*(d/b)**b-a #arithmetic 
print(output)

output=b%d
print(output)    #division

output=c/b       #floor division
print(output)

output=c//b
print(output)

print(0 and 0)   #logical
print(0 and 1)
print(1 and 0)
print(1 and 1)'''


'''
BODMAS RULE:
op:1+2*(10/2)**2-1
op:1+2*5**2-1
op:1+2*25-1
op:1+50-1
op:51-1
op:50'''

'''Control Statements:
1.if'''

#program
'''a=1
b=2
if b>4:
    if a<2:
        a=a+1
        print(a)
elif a!=0:
    print("end")'''
    
'''Taking Input from the user'''

#program
'''a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print(a+b)
print(type(a))
print(type(b))'''



'''Largest of 3 numbers'''

a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))
if a>=b and a>=c:
    largest=a
elif b>=a and b>=c:
    largest=b
else:
    largest=c
print("The largest number is",largest)
    




    
    
        





