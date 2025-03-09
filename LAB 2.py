#Act 3
def check_number():
    num = int(input("Attach a number: "))
    if num % 2 == 0:
        print(f"{num} is an Even number.")
    else:
        print(f"{num} is an Odd number.")
    user_input = input("Wanna check a different number? (y/n): ")
    if user_input == 'y' or user_input == 'y':
        check_number()
    else:
        print("You do not, why?.")
    
check_number()
#Ian Dave Ching