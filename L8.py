v=4
w=5
x=8
y=2
z=0
z=(v+w)*x/y
print(z)

name="Alex"
age=0
if name=="Alex" or name =="jhon" and age >=2:
    print("welcome")
else:
    print("sorry")
#Activity02
print("Enter the Numerator:")
num=int(input())
print("Enter the Denominator:")
den=int(input())
if num%den==0:
    print("The number is divisible")
else:
    print("The number is not divisible")
#Activity03
mean1=38
wrong_number=36
correct_number=56
total_number=40
sum=mean1*total_number
print("the Sum of 40 numbers is",sum)
num2=sum-(wrong_number-correct_number)
print("The correct number is",num2)

mean2=num2/total_number
print("The mean of 40 numbers is",mean2)
#Activity04 
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
avg=(a+b+c)/3
print("The average of the three numbers is",avg)

if avg>a and avg>b and avg>c:
    print("%d is the greater than %d and %d and %d" %(avg,a,b,c))
elif avg>a and avg>b:
    print("%d is the greater than %d and %d" %(avg,a,b))
elif avg>a and avg>c:
    print("%d is the greater than %d and %d" %(avg,a,c))
elif avg>b and avg>c:
    print("%d is the greater than %d and %d" %(avg,b,c))
elif avg>a:
    print("%d is the greater than %d" %(avg,a))
elif avg>b:
    print("%d is the greater than %d" %(avg,b))
elif avg>c:
    print("%d is the greater than %d" %(avg,c))
else:
    print("All are equal")
