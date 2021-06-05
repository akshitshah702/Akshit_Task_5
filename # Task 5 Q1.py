# Task 5 Q1
try: 
    k = 5//0 # raises divide by zero exception. 
    print(k) 
    
# handles zerodivision exception     
except ZeroDivisionError:    
    print("Can't divide by zero") 
        
finally: 
    print('This is always executed')