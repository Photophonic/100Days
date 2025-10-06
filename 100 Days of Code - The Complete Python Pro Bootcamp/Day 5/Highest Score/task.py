student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))


print(f'total scores {sum(student_scores)}')
print(f'highest score {max(student_scores)}')

# manual loop
total_score = 0

for score in student_scores:
    total_score += score
print(f'total scores {total_score}')

# manual max score
max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score
print(f'max score {max_score}')