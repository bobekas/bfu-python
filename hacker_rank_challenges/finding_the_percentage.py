if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    current_student_marks = student_marks[query_name]
    result = 0

    for mark in current_student_marks:
        result += mark

    result = result / len(current_student_marks)

    print (format(round(result, 2), '.2f'))
