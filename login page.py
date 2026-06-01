from tkinter import *

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "password":
        label_result.config(text="Login successful!", fg="green")
    else:
        label_result.config(text="Login failed. Try again.", fg="red")
# Create the main application window
root = Tk()
root.title("Login Form")
root.geometry("300x200")
# Create and place the username label and entry
label_username = Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = Entry(root)
entry_username.pack(pady=5)
# Create and place the password label and entry
label_password = Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = Entry(root, show="*")
entry_password.pack(pady=5)
# Create and place the login button
button_login = Button(root, text="Login", command=login)
button_login.pack(pady=10)
# Create and place the result label
label_result = Label(root, text="")
label_result.pack(pady=5)
# Start the main event loop
root.mainloop()
