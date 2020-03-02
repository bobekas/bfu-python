if __name__ == '__main__':
    dictionary = {}
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dictionary[name] = score

    min_grade = 1000
    second_lowest_grade = 1000

    for student_name in dictionary:
        if(min_grade > dictionary[student_name]):
            min_grade = dictionary[student_name]

    for studentName in dictionary:
        if(second_lowest_grade > dictionary[student_name] and min_grade < dictionary[student_name]):
            second_lowest_grade = dictionary[student_name]

    for studentName in dictionary:
        if(second_lowest_grade == dictionary[student_name]):
            names.append(student_name)

    names.sort()

    for name in names:
        print(name)
