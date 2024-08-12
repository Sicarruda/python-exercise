#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    sum_student = float(0)
    
    for student in student_marks[query_name]:
        sum_student = float(student) + sum_student
    
    media = sum_student / 3
    
    print("{:.2f}".format(media))