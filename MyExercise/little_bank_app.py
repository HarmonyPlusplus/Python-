user = {}

user["name"] = input("Enter Your Name: ")
user["email"] = input("Enter your email: ")
user["opening_balance"] = int(input("Enter opening balance: "))

print("Account created successfully!")

print(f"Name: {user["name"]}")
print(f"Email: {user['email']}")
print(f"Opening Balance: {user["opening_balance"]}")

user["updated_balance"] = int(input("How much do you want to deposit?: "))

user["opening_balance"]+=user["updated_balance"]

print(f"your new balance is {user['opening_balance']}")
