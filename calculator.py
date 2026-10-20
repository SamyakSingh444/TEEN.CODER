a=input("Enter the operation you want on the numbers:")
if (a=="+" or a=="plus" or a=="addition"):
     n=int(input("Enter number 1 you want sum of:"))
     n2=int(input("Enter number 2 you want sum of:"))
     print(f"{n}+{n2}={n+n2}")
elif (a=="-" or a=="minus" or a=="subtraction"):
     n3=int(input("Enter number 1 you want differnce of:"))
     n4=int(input("Enter number 2 you want differnce of:"))
     print(f"{n3}-{n4}={n3-n4}")
elif (a=="*" or a=="product" or a=="multiply"):
     n5=int(input("Enter number 1 you want product of:"))
     n6=int(input("Enter number 2 you want product of:"))
     print(f"{n5}*{n6}={n5*n6}")
elif (a=="/" or a=="divide"):
     n7=int(input("Enter number 1 (dividend):"))
     n8=int(input("Enter number 2 (divisor):"))
     print(f"{n7}/{n8}={n7/n8}")
else:
     print("Something went wrong!")
 
