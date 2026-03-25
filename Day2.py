#Today I study all OPERATORS

#1.  Arithmetic operators    all 
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#2. Comparsion operators  --> its also called "Relational" operators
c=12
d=15
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)
print(a==b)

#3. Assignement Operators
e=20
e+=12
print(e)
e-=12
print(e)
e*=12
print(e)
e/=12
print(e)
e//=12
print(e)
e**=12
print(e)
e%=12
print(e)

#4. Logical operator
a=12
b=45
print(a<b and b>a)
print(a>b and b>a)
print(a<b and b<a)
print(a>b and b<a)

print(a<b or b>a)
print(a>b or b>a)
print(a<b or b<a)
print(a>b or b<a)

print(not(a==b))
print(not(a<b))
print(not(a>b))
print(not(a!=b))

#5. Bitwise operator    --> Its work on Bollean values
a=5
b=2
print(a & b)  #AND
print(a | b)   #OR
print(a ^ b)   #XOR
print(~a)     #NOT
print(~b)     #NOT

#6. Identity Operator
a="Allah"
b="Allah"
c="Muhammad"
print(a is b)
print(b is a)
print(a is c)
print(a is not c)

#7. Membership Operator
a=["Allah","Muhammad","Prophet","Muslims","Auma"]
print("Allah" in a)
print("Maria" in a)
print("Maria" not in a)

#today 2nd topic is input
name=input("Enter your Name: " )
age=input("Enter your Age: " )
love=input("Enter your First love: ")
print(f"Your name is {name}.")
print(f"Your age is just {age}.")
print(f"So next year you will be {int(age)+1} years old.")
print(f"Amazing your first love is {love}. ")