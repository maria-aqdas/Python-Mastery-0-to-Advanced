#Today I learn 'while' loop, 'for' loop, 'pass' Statement, 'Break' Statement and 'Continuou' Statement
## WHILE LOOP ##
n=1
while n<10:
    print(n)
    n+=1

## FOR LOOP ##
God="ALLAH ALMIGHTY"
for x in God:
    print(x)


## PASS STATEMENT ##
n=1
while n<10:
    if(n==5):
        pass
    else:
        print(n)
    n+=1

for x in range(1,5):
    if(x==3):
        pass
    else:
        print(x)    


## BREAK STATEMENT ##
n=1
while n<10:
    if(n==5):
        break
    else:
        print(n)
    n+=1

for x in range(1,5):
    if(x==3):
        break
    else:
        print(x)   


# # CONTINUOU STATEMENT ##
# n=1
# while n<10:
#     if(n==5):
#         continue
#     else:
#         print(n)
#     n+=1

# for x in range(1,5):
#     if(x==3):
#         continue
#     else:
#         print(x)   


#Now as a practice we print 1 to 50 no using for loop
for a in range(51):
    print(a)        

#1.	Count Even Numbers
n=int(input("Enter no. of range of even no. : "))
print(f"Even numbers from 1 to {n} are ")
for i in range(1,n+1):
    if i%2==0:
        print(i, end=", ")






# #Now as a practice we print table of 5 using while loop
# n=1
# while n<=10:
#     result=5*n
#     print(f"5 * {n} = {result}")
#     n+=1
