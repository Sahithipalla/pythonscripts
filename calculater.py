def add(a,b):
    return(a+b)
def substract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def division(a,b):
    return(a/b)
print("select operation:")
print("1:add")
print("2:substarct")
print("3:multiply")
print("4:division")
choice=input("enter choice 1/2/3/4:")
num_1=int(input("enter first number:"))
num_2=int(input("enter second number:"))
if choice=="1":
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice=="2":
      print(num_1,"-",num_2,"=",substract(num_1,num_2))
elif choice=="3":
      print(num_1,"*",num_2,"=",multiply(num_1,num_2))
elif choice=="4":
      print(num_1,"/",num_2,"=",division(num_1,num_2))
else:
    print("Invalid input")