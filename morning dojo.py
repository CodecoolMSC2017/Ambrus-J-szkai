import sys

def solve(grades):
    i = 0
    while i < len(grades):
        if grades[i] < 37:
            print(grades[i])
            i = i + 1
        elif grades[i] % 5 == 0:
            print(grades[i])                     
            i = i + 1
        elif grades[i] % 5 == 4:
            gradesnew = grades[i] + 1
            print(gradesnew)
            i = i + 1
        elif grades[i] % 5 == 3:
            gradesnew = grades[i] + 2
            print(gradesnew)
            i = i + 1
        else:
            print(grades[i])
            i = i + 1

n = int(input("give me the numbers of students ").strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input("what is the grade ").strip())
    grades.append(grades_t)
result = solve(grades)
print("\n".join(map(str, result)))