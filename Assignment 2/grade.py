print("\n===== GradeBook Analyzer =====")
print("1.) Manual Input")
print("2.) CSV Input (name,marks)")

choice = int(input("Enter your choice: "))

marks = {}


if choice == 1:
    n = int(input("How many students? "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        score = int(input("Enter marks: "))
        marks[name] = score

elif choice == 2:
    import csv
    filename = input("Enter CSV file name (with .csv): ")
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            marks[row[0]] = int(row[1])


print("\n--- Data Loaded Successfully ---\n")



scores = list(marks.values())
scores_sorted = sorted(scores)


average = sum(scores) / len(scores)


l = len(scores_sorted)
if l % 2 == 1:        # odd count
    median = scores_sorted[l//2]
else:                 # even count
    median = (scores_sorted[l//2 - 1] + scores_sorted[l//2]) / 2


max_score = max(scores)
min_score = min(scores)

print("Average Marks:", average)
print("Median Marks:", median)
print("Highest Marks:", max_score)
print("Lowest Marks:", min_score)


grades = {}
for name, score in marks.items():
    if score >= 90:
        grades[name] = "A"
    elif score >= 80:
        grades[name] = "B"
    elif score >= 70:
        grades[name] = "C"
    elif score >= 60:
        grades[name] = "D"
    else:
        grades[name] = "F"


grade_count = {"A":0, "B":0, "C":0, "D":0, "F":0}
for g in grades.values():
    grade_count[g] += 1

print("\nGrade Distribution:", grade_count)


passed_students = [name for name, score in marks.items() if score >= 40]
failed_students = [name for name, score in marks.items() if score < 40]

print("\nPassed:", passed_students)
print("Failed:", failed_students)


print("\nName\t\tMarks\tGrade")
print("---------------------------------------")
for name in marks:
    print(f"{name}\t\t{marks[name]}\t{grades[name]}")

print("\nAnalysis complete!")