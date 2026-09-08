# # experiment number one 
# university student information system 
roll_no=int(input("enter student roll number :"))
student_name= input("enter student name :")

marks1=int(input("enter student  marks :"))
marks2=int(input("enter student  marks :"))
marks3=int(input("enter student  marks :"))
marks4=int(input("enter student  marks :"))
marks5=int(input("enter student  marks :"))

if (marks1 < 0 or marks1>100 or marks2 < 0 or marks2>100 or marks3 <0 or marks3 >100 or marks4 <0  or marks4 > 100 or marks5 <0 or marks5> 100 ):
    print("invalid njmber ! \n")
    print("enter number between 0 to 100!")

#calculqting percentage 
total_marks=marks1 + marks2+ marks3 + marks4 + marks5
percentage =( total_marks/500)*100

#grade 
if(percentage>90):
    grade="a+"
elif(percentage>70 and percentage <90 ):
    grade="a"
elif(percentage > 50 and percentage <70):
    grade="b"
else:
    grade="c"

if (grade == "c" ):
    result="fail"
else:
    result="pass"

print("result:")
print("rollnumnrer:",roll_no)
print("name:",student_name)
print("percentage:", percentage )
print("grade:",grade)
print("result:",result)




