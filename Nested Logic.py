# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
k = input()
day1, month1, year1= s.split()
day2 , month2, year2 = k.split()

if int(year1) == int(year2):
    if int(month1) == int(month2): 
        if int(day1) > int(day2):
            print(15*(int(day1)-int(day2)))
            
        elif int(day1) == int(day2) or int(day1) < int(day2):
            print('0')
    
    elif int(month1) < int(month2):
        print('0')
    else:
        print(500*(int(month1)-int(month2)))
        
elif int(year1)+1 == int(year2):
    if int(month1) + 1 == int(month2):

        print('0')
    elif int(month1) == 12 and int(month2) == 1:
        print('0')
elif int(year1)==int(year2) and int(month1) == int(month2) and int(day1) == int(day2):
    print('0')
elif int(year1) < int(year2):
    print('0')
else:
    print('10000')        
    
        
