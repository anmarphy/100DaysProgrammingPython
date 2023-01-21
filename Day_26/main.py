import random
import pandas as pd
names=['Alex', 'Berth', 'Caroline']

student_score={student: random.randint(1,10) for student in names }
print(student_score)



pass_student={student:score for (student, score) in student_score.items() if score>6}
print(pass_student)

student_dic={
    'student':names,
    'score':[54, 23, 67]
}
df_student=pd.DataFrame(student_dic)
print(df_student)

for (index, row) in df_student.iterrows():
    if row.student=='Alex':
        print(row)