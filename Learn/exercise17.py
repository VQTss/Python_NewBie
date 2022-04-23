n = int(input())
matrix  = []
for i in range(n):
    name  = input()
    grade = float(input())
    matrix.append([name,grade])
# Find a student have minimum grade in class
min_grade =  matrix[0][1]

# Find list student have grade greater than min
matrix_min = []
for i in range(n):
    a = matrix[i][1]
    if a < min_grade:
        min_grade = a

for i in range(n):
    a = matrix[i][1]
    if a > min_grade:
        matrix_min.append(matrix[i])

min_grade = matrix_min[0][1]
matrix_t = []
for i  in range(len(matrix_min)):
    a = matrix_min[i][1]
    if a <= min_grade:
        matrix_t.append(matrix_min[i])

result = []

if len(matrix_t) > 1:
    for i in range(len(matrix_t)):
        result.append(matrix_t[i][0])
    result.sort()
    for i in range(len(result)):
        print(result[i])
else:
    print(result[0][0])


    


