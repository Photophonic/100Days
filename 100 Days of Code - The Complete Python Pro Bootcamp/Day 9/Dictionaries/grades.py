student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    grade = ''
    if 91<= student_scores[key] <= 100:
        grade = 'Outstanding'
    elif 81<= student_scores[key] <= 90:
        grade = 'Exceeds Expectations'
    elif 70<= student_scores[key] <= 80:
        grade = 'Acceptable'
    else:
        grade = 'Fail'

    student_grades[key] = grade

print(student_grades)