# def caculate_area(length, width):
#     answer=length*width
#     return answer

# result=caculate_area(10, 20)
# print("So, the final result is : ",result)

# def average(math=80, english=48):
#     Final_result=(math+english)/2
#     return Final_result

# marks=average()
# print(f"Average marks of math and english is : {marks}.")


# def average(math, english):
#     Final_result=(math+english)/2
#     return Final_result

# marks=average(76,87)
# print(f"Average marks of math and english is : {marks}.")


def calculate_average(math,science,english,urdu):
    total=math+science+english+urdu
    average=total/4
    return total

def calculate_grade(average_mark):
    if average_mark >=90:
        return 'A+'
    elif average_mark>=80:
        return 'A'
    elif average_mark >=70:
        return 'B'
    elif average_mark >=60:
        return 'C'
    elif average_mark >=50:
        return 'D'
    else:
        print("YOU ARE 'FAIL'!!! PLEASE TRY AGAIN.....")

def display_report(name, m,s,e,u):
    avg_marks=calculate_average(m,s,e,u)
    grade=calculate_grade(avg_marks)

    print("-"*30)
    print("  |Student grade book.|  ")
    print("-"*30)
    print(f"Student Name : {name} .") 
    print(f"Average Marks : {avg_marks:.2f}")
    print(f"Final Grade : {grade}")   
    print("-"*30)

display_report("Maria",22,23,24,22)
display_report("Khadijha",21,23,22,17)
display_report("Ali",12,13,17,14)

