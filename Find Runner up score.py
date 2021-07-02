if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    res = [int(x) for x in arr]
    k = list(set(res))
    k.remove(max(k))
    print(max(k))
