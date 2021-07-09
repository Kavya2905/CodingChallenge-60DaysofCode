if __name__ == '__main__':
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append([name,score])
    x = sorted(list(set([score for name,score in score_list])))[1]
    y = '\n'.join([n for n,mark in sorted(score_list) if  mark == x])
    print(y)

        
        
