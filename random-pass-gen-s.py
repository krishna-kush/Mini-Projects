import random, time

# incialising functions
def clear(): # for clearing the console
    print('\033[2J')
def sleep(sec): # for clearing the console
    time.sleep(sec)
def mustBe(main, greaterOrNot, limit):
    print(f"{main}, must be {greaterOrNot} than {limit} \U0001F915")


# incialising variables
run = "y"

sleep_short = 1
sleep_midium = 2
sleep_long = 3

while run[0].lower() == "y":
    print('''
        WELCOME TO THE PASSWORD GENERATOR \U0001F609
        May you have a Secure Password ...
    ''')

    password = ""

    sleep(sleep_long)
    clear()

    pass_strength = input("Select Password Strength: Weak/Medium/Strong(w/m/s): ")
    if pass_strength[0].lower() == "s":
        pass_length = int(input("Enter Password Length(Must be > Than 12): "))
        clear()
        while pass_length <= 12:
            print("Password Length Must be > Than 12")
            pass_length = int(input("Enter Password Length(Must be > Than 12): "))
            clear()
    else:
        pass_length = int(input("Enter Password Length: "))

    clear()

    # percentage of numbers and symbols in password should be multiple of 10 bcz we are rounding off the numbers further in code
    if pass_strength[0].lower() == "w":
        num_percentage = 10
        symbol_percentage = 10
    elif pass_strength[0].lower() == "m":
        num_percentage = 30
        symbol_percentage = 30
    elif pass_strength[0].lower() == "s":
        num_percentage = 50
        symbol_percentage = 40


    # defining length of numbers and symbols
    num_len = (num_percentage/100) * pass_length
    symbol_len = (symbol_percentage/100) * pass_length

    # adding alphabets to password
    for i in range(pass_length-int(num_len)-int(symbol_len)):
        alpha_lower = chr(random.randint(97, 122)) # ascii values of a-z
        alpha_capital = chr(random.randint(65, 90)) # ascii values of A-Z

        password += random.choice(alpha_lower + alpha_capital)
    
    # adding numbers to password
    for i in range(int(num_len)):
        num = random.randint(0, 9)

        if len(password) != 0: # if password is empty(when num and symbol percentage addsup to 100 %), following alogorithm wil fail, thats why we are checking if password is empty or not
            where = random.randint(0, len(password)-1)
        else:
            where = 0

        password = password[:where] + str(num) + password[where:]
    
    # adding symbols to password
    for i in range(int(symbol_len)):
        symbol_ascii = []
        for i in range(33, 48): # ascii values of symbols not @
            symbol_ascii.append(i)
        symbol_ascii.append(64) # ascii value of @ symbol
        
        symbol = chr(random.choice(symbol_ascii)) # ascii values of symbols

        if len(password) != 0:
            where = random.randint(0, len(password)-1)
        else:
            where = 0

        password = password[:where] + symbol + password[where:]

    # Password Generation Completed
    
    clear()
    print("Generating Password...")
    sleep(sleep_short)
    print(f"Your Password is: {password}")


    run = input("Do you want to Generate another Password(y/n): ")
    clear()

    while not run[0].lower() in 'yn':
        print("Please Enter Valid Input")
        run = input("Do you want to Generate another Password(y/n): ")
        clear()


print("Thank You for using our Service,")
sleep(sleep_short)
print("Please Visit Again for Using Safe And Secure Passwords \U0001F918")
sleep(sleep_short)
print("Have a Nice Day!!!")
sleep(sleep_midium)
clear()
