cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    l = [0, 1]
    for i in range(2, n):
        l.append(l[i-1] + l[i-2])
    return l
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
