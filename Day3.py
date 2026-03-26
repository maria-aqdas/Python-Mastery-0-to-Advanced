a=float(input("Enter first number: "))
b=float(input("Enter second number: "))

print("\n 1 .Addition.")
print("\n 2 .Substraction.")
print("\n 3 .Multiplication. ")
print("\n 4 .Devision. ")
print("\n 5 .Modlus. ")
print("\n 6 .Power. ")

choice=input("\nPlease enter your choice(1/2/3/4/5):\n")

if(choice=="1"):
    SUM=a+b
    print(f"{a}+{b}={SUM}")
elif(choice=="2"):
    Substraction=a-b
    print(f"{a}-{b}={Substraction}")    
elif(choice=="3"):
    Multiplication=a*b
    print(f"{a}*{b}={Multiplication}")    
elif(choice=="4"):
    if(b==0):
        print("Devision is not possible. error")
    else:    
        Devision=a/b
        print(f"{a}/{b}={Devision}") 
elif(choice=="5"):
    Modulus=a%b
    print(f"{a}%{b}={Modulus}")      
elif(choice=="6"):
    Power=a**b
    print(f"{a}**{b}={Power}")
else:
    print("Invalid. Please enter(1, 2, 3, 4, 5, 6)")    




