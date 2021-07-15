# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
r_pattern = pattern[::-1]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + r_pattern))
