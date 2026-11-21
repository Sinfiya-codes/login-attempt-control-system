print("LOGIN ATTEMPT CONTROL SYSTEM")

correct_username = "admin"
correct_password = "12345"

max_attempts = 3

for attempt in range(max_attempts):

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful!")
        break

    else:
        remaining = max_attempts - attempt - 1
        print("Invalid username or password!")

        if remaining > 0:
            print("Attempts remaining:", remaining)

        else:
            print("Account Locked!")
            print("Too many failed attempts.")

print("Program Ended")
