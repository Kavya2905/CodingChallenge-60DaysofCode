if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    percent = {}
    
    for key in student_marks: 
        percent[key] = '{:.2f}'.format(sum(student_marks[key])/3) 
    print(percent[query_name])
    
        
