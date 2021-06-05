# Task 5 Q3
def mult_digits():
        x = input("Enter number ")    
        while type(x) is not int:
            try:
                while int(x) <= 1:
                    x = input("Please enter a number greater than 1: ")
                    x = int(x)
            except ValueError:
                  x = input("Please enter integer values only: ")
                  x = int(x)       
        print(f"Yes, you have entered {x}.")