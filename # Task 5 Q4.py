# Task 5 Q4
print('Enter correct username and password')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Abcd@123' and username=='admin':
        print('Access granted')
        break
    else:
        print('Write password again')
        count += 1