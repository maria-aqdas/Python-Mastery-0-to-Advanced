# #Today is my 6 day in python i try practice thing that learn in my last 5 days
# def add(a, b):
#     return a + b

# result = add(10,20)
# print(f"Resut is : {result}")

# #this is my first 'function' program.
# #check even odd numbers.
# def check_even_odd(number):
#     if number%2==0:
#         return "Number is even."
#     else:
#         return "Number is odd. "

# for i in range(3):
#     num=int(input("Enter number: "))
#     result=check_even_odd(num)
#     print(result) 

#Now we function to calculte net salary
# def check_net_salary(basic_salary, bonus=1000):
#     if basic_salary>50000:
#         tax=(basic_salary*10 )/100
#     else:
#         tax=(basic_salary*5 )/100    
#     net_salary=basic_salary+bonus-tax
#     return net_salary
# print("With parameters: " , check_net_salary(60000))
# print("Default parameters: ", check_net_salary(40000))     


# ### SOME BUILT IN FUNCTIONS ###
# # MIN AND MAX
# biggest=max(10,20,30,40,50)
# smallest=min(1,2,3,4,5,6)
# print(biggest)
# print(smallest)
    
# #'abs' it gives the absolute value of the number. no negative or zero
# distance=abs(-23.3)
# print(abs(-3.1314))
# print(abs(-3.86))
# print(abs(-3.99))
# print(distance)

# #'round' is a built in function that rounds off in a specfic number
# cgpa=round(3.86,2)
# print(round(3.1314))
# print(round(3.99))
# print(f"Now CGPA is : {cgpa} .")

# #'sum' is SUM all values
# total_marks=sum([71,77,81,83,86,85,85,93])
# print(total_marks)

# #'type' find the type of value
# a="Allah"
# b=1
# c=2.34
# d=True
# e=None
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

#'sorted' is used to sorte data 
a=[93,85,85,83,71,81,77,86]
Sort_Data=sorted(a)
print(Sort_Data)