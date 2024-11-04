# Assignment
# students_names = ["sandra", "Patricia", "Faith", "Phionah", "Anitah", "Michele"]
# students_marks = [80, 56, 78, 90]
# 1 Print Patricia, Faith, Phionah and Anitah
# 2 Add Masha at the forth position
# 3 Update the name Phionah Aladinah
# 4 Dispaly the length of the students lists.
# 5 Print all the students names using a for loop
# 6 Calculate the total marks for the student variable and the answer = 304


student_names = ['sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michele']
print(student_names[1:4]) 

#question 2
student_names = ['sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michele']
student_names.insert(4, "Marsha")
print(student_names)

#question 3
student_names = ['sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michele']
student_names[3]="Phionah Aladinah"
print(student_names)

#question 4
student_names = ['sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michele']
print(len(student_names))


#question 5
student_names = ['sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michele']
for name in student_names:
    print(name)

#question 6
def total_mark_of_students():
    student_marks = [80,56,78,90] 
    sum=(80+56+78+90) 
    print(f'The total marks for student mark is{sum}') 
total_mark_of_students()
