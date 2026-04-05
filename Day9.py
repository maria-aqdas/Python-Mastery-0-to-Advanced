#Today i study how we join list
#By using '+' operator
# list1=["ALLAH","ALMIGHTY","KIND"]
# list2=["PROPHET","MUHAMMAD","AHMAD"]
# list3=list1+list2
# print(f"Final List is : {list1+list2}")

# #using 'append' mathod
# list1=["ALLAH","ALMIGHTY","KIND"]
# list2=["PROPHET","MUHAMMAD","AHMAD"]
# for x in list2:
#     list1.append(x)
# print(list1)    


# #using 'extand' method
# list1=["ALLAH","ALMIGHTY","KIND"]
# list2=["PROPHET","MUHAMMAD","AHMAD"]
# list1.extend(list2)
# print(list1)

## LIST COMPERHENSIONS ##
# list=[x**2 for x in range(1,6)]
# print(list)

# list=[x for x in range(1,20) if x%2==0]
# print(list)

# name=["Ayesha","abu huraira","ahmad","maria", "alia","khadijha","mahien"]
# print(name)
# n=[lst.upper() for lst in name]
# print(n)

# for i in range(1,11):



import matplotlib.pyplot as plt
x=[1,2,3]
y=[10,20,30,40] 
plt.plot(x,y)
plt.title("MY FIRST PROGRAM OF MATPLOTLIP IN V S CODE")   
plt.xlabel("IT IS X-AXIS")
plt.ylabel("IT IS Y-AXIS")
plt.show
