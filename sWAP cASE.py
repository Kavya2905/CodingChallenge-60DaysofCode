def swap_case(s):
    x = ''
    for letter in s:
        if letter.islower():
            x += letter.upper()
        else:
            x += letter.lower()
    return x
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
