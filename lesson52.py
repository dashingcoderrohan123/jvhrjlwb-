#Write a program to check how the exceptions and finally statement works
try:
    num1=int(input("Enter two numbers seperating by comma"))
    num2=int(input("Enter two numbers seperating by comma"))
    r=num1/num2
    print("the result is ",r)
except ZeroDivisionError:
    print("division by zero is not possible")

except SyntaxError:
    print("you have not seperate the values by commas")
except :
    print("wrong input" )

else:
    print("no exception")
    
finally:
    print("this will execut no matter what")
 