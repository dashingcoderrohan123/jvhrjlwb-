#Write a program to understand how the value error exception works?


try:
    r=int(input("enter the value"))
    print("the number entered is ",r)
except ValueError as ex:
    print("exception", ex)
    
        