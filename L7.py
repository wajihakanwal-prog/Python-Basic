x=5
if(type(x) is int):
    print("x is an integer")
else:
    print("x is not an integer")

x=5.5
if(type(x) is float):
    print("true")
else:
    print("false")

x=20
y=20
if(x is y):
    print("x and y are equal")
else:
    print("x and y are not equal")
y=30
if(x is not y):
    print("x and y are different")

#Activity02
a=10
b=10
print("a >> 1 = ",a>>1)
print("b >> 1 = ",b>>1)

a=5
b=-10
print("a << 1 =",a<<1)
print("b << 1 =",b<<1)

#Activity03
print("Enter the marks obtained in three subjects")
a=int(input())
b=int(input())
c=int(input())
total=a+b+c
print("Total marks obtained = ",total)
average=total/3
print("Average marks obtained = ",average)
validrange=range(0,101)
if average in validrange:
    print("Average is valid")
else:
    print("Average is not valid")
if average in range(90,101):
    print("Grade A")
elif average in range(80,90):
    print("Grade B")
elif average in range(70,80):
    print("Grade C")
elif average in range(60,70):
    print("Grade D")

