student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
def score(value):
    if value >= 91:
        scoring='Outstanding'
    elif value >=81:
        scoring='Exceed Expectations'
    elif value >= 71:
        scoring='Acceptable'
    else:
        scoring='Fail'
    return scoring

for i in student_scores:
    student_grades[i]=score(student_scores[i])

print(student_grades)