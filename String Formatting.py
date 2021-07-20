def print_formatted(number):
    # your code goes here
    w = len(bin(number)[2:])
    for i in range(1, number+1):
        a = str(i)
        b = str(oct(i)[2:])
        c = str(hex(i)[2:]).upper()
        d = str(bin(i)[2:])
        
        print(a.rjust(w), b.rjust(w), c.rjust(w), d.rjust(w))

if __name__ == '__main__':
