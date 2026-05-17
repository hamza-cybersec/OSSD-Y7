import tkinter as tk
# login reading from file
def read_file():
    
    pass

def write_file():
    pass


def login():
    username = username_entry.get()
    password = password_entry.get()

    file = open("users.txt", "r")
    users = file.readlines()
    file.close()

    for user in users:
        stored_username, stored_password = user.strip().split(",")

        if username == stored_username and password == stored_password:
            print("Login successful")
            return

    print("Invalid username or password")

def signup():
    username = username_entry.get()
    password = password_entry.get()

    file = open("users.txt", "a")
    file.write(username + "," + password + "\n")
    file.close()

    print("Signup successful")

def main():
    pass

root = tk.Tk()
root.title("Login System")
root.geometry("400x300")
username_label = tk.Label(root, text="Username")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=5)

signup_button = tk.Button(root, text="Signup", command=signup)
signup_button.pack(pady=5)



root.mainloop()