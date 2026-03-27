#Today is my 4th day of python learning and I built a graded scheme in which you enter you marks and subject you will et you result accordin this
#First of all we enter number of subjectsn and their marks
num_subjects=int(input("Enter total number of subjects: "))
marks=[]   

#then using for loop to get subjects number
for i in range(num_subjects):
    mark=float(input(f"Enter obtain marks from(0-100) subject{i+1}."))
    marks.append(mark)

#getting number, total number and percentage
total_obtained=sum(marks) 
total_max=num_subjects*100
percentage=total_obtained/total_max*100

#We show grade using if else statements
if percentage>=90:
    grade="A+"
elif percentage >=80 and percentage<90:
    grade="B+"  
elif percentage >=70 and percentage<80:
    grade="C"  
elif percentage >=60 and percentage<70:
    grade="D"  
elif percentage >=50 and percentage<60:
    grade="E" 
else:
    grade="F"    

#Final output
print("\n " + "=" *40)
print("### GRADE CALCULATER SYSTEM ###")
print("="*40)
print(f"Total Subjects : {num_subjects}")
print(f"Total Marks : {total_obtained}/{total_max}")
print(f"Percentage : {percentage:.2f}%")
print(f"Final Grade : {grade} ")
print("="*40)

