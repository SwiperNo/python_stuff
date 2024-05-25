users = [
    (0, "Bob", "password"),
    (1, "Jack", "jack123"),
    (2, "John", "john123"),
    (3, "Bobby", "password1"),
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect!")