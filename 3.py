import random
students = ['Алексей', 'Мария', 'Иван', 'Екатерина', 'Андрей']

results = {}
for student in students:
    results[student] = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]

average_scores = {}
for student, scores in results.items():
    average_score = sum(scores) / len(scores)
    average_scores[student] = average_score

sorted_students = sorted(average_scores, key=average_scores.get, reverse=True)

print(results)
for student in sorted_students:
    print(f"{student}: {average_scores[student]}")