#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    list_students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_students.append((name, score))
    
    list_students = sorted(list_students, key=lambda grade: grade[1])
    
    for index in range(len(list_students)):
        if list_students[0][1] < list_students[index][1]:
            second_lowest_grade = list_students[index][1]
            break
            
    students_second_lowest_grade = []
    
    for student in list_students:
        if student[1] == second_lowest_grade:
            students_second_lowest_grade.append(student[0])
    
    students_second_lowest_grade.sort()
    
    for name in students_second_lowest_grade:
        print(name)