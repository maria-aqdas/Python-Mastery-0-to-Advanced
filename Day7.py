# #Today is my revision day and I revise previous topic
#Write a Python program that asks the user to enter their name and age. Then print a message like:
#"Hello [Name], you are [Age] years old."
name=input("Enter you name: ")
age=int(input("Enter your age :  "))
print(f"My name is {name} and I am {age} years old.")


#Q2. Write a program that takes two numbers as input from the user and prints their:Sum,Difference,Product,Division (float),Modulus
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"Sum is: {a+b}")
print(f"Difference is: {a-b}")
print(f"Product is: {a*b}")
print(f"Devision is: {a/b}")
print(f"Modulus is: {a%b}")

#Q3. Write a Simple Calculator program that does the following:,Takes two numbers as input,Asks the user which operation they want to perform (+, -, *, /, %),Prints the result according to the chosen operation
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
operation=input("Enter any operation you want to perform(+,-,/,*,%):")
if operation=="+":
    print(f"Sum is : {a+b}")
elif operation=="-":
    print(f"Differance is : {a-b}")
elif operation=="*":
    print(f"Product is : {a*b}")
elif operation=="/":
    print(f"Devsion is : {a/b}")
elif operation=="%":
    print(f"Modulus is : {a%b}")
else:
    print("Invalid input. Please Enter any operator!!!!")    

#Q4. Write a program that takes marks of 3 subjects (Math, Science, English) as input and calculates the average. Then use if-elif-else to print the grade:
#Average >= 90 → "A+ Grade",Average >= 80 → "A Grade",Average >= 70 → "B Grade",Average >= 60 → "C Grade",Otherwise → "Fail"


math=int(input("Enter number of maths: "))
science=int(input("Enter number of science: "))
english=int(input("Enter number of English: "))
average=((math+science+english)/3)
if average>=90 :    
    print("A+")
elif average>=80 and average<=90:    
    print("A")
elif average>=70 and average<=80:    
    print("B")
elif average>=60 and average<=70:    
    print("C")            
else:
    print("FAIL.....")

#Q5. Write a program using nested if that asks the user for their age and checks:
#If age < 18 → "You are a minor.",If age >= 18 and age < 60 → "You are an adult.",If age >= 60 → "You are a senior citizen."
age=int(input("Please Enter your age : "))
if age<18:
    print("Yo are miner.")
elif age>19 and age<60:
    print("You are adult.")
elif age>60:
    print("you are senior.")
else:
    print("INVALID")


#Q6. Write a program using a for loop to print all even numbers from 1 to 50 (inclusive).
for i in range(0,50):
    if i%2==0:
        print(f"Even number: {i} ")    
#Q7. Write a program using a for loop to calculate and print the sum of first 20 natural numbers (1 + 2 + 3 + ... + 20).
total=0
for i in range (0,20):
    total=total+i
print(f"SUM IS : {total}")        

#Q8. Write a program using a while loop to print the multiplication table of any number given by the user (like you did for 5).
n=0
while n<=9:
    n=n+1
    table=n*5
    print(f"5 * {n} = {table}")    


#Write a program that asks the user to enter a number and uses a while loop to print its digits in reverse order.
num=12345
reverse_num=0

while num>0:
    digit=num%10
    reverse_num=reverse_num*10 + digit
    num=num//10
print(f"Reverse number is : {reverse_num}")    
    