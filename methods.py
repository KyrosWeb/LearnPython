# Python Methods

# Without methods, we would have to write the same code over and over again
# For example, if we want to greet a user, we would have to write the following code every time:

print("Hello, User1")
print("Hello, User2")
print("Hello, User3")

# With methods, we can write the code once and reuse it
# Here's a method that greets a user:

def greet_user(user_name):
    print(f"Hello, {user_name}")

# Now we can use this method to greet any user:

greet_user("User1")
greet_user("User2")
greet_user("User3")