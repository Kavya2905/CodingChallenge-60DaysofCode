def count_substring(string, sub_string):

    s=0
    
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            s += 1
        
    return s

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
