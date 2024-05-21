import hashlib
import os

class UserDatabase:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose a different username.")
            return False
        else:
            
            salt = os.urandom(16)
            hashed_password = self._hash_password(password, salt)
            self.users[username] = {'salt': salt, 'hashed_password': hashed_password}
            print("User created successfully!")
            return True

    def login(self, username, password):
        if username in self.users:
            user_data = self.users[username]
            salt = user_data['salt']
            hashed_password = user_data['hashed_password']
            input_hashed_password = self._hash_password(password, salt)
            if hashed_password == input_hashed_password:
                print("Login successful!")
                print(f"Salt: {salt.hex()}")
                print(f"Hashed Password: {hashed_password}")
            else:
                print("Incorrect password.")
        else:
            print("User not found.")

    def _hash_password(self, password, salt):
        return hashlib.sha256(password.encode() + salt).hexdigest()

db = UserDatabase()

while True:
    print("\nSelect an option:")
    print("1. Create a new user")
    print("2. Login")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        db.create_user(username, password)
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        db.login(username, password)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
