import random
import tkinter as tk

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

string = upper_case + lower_case + numbers + symbols

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        self.length_label = tk.Label(master, text="Enter length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(master)
        self.length_entry.pack()

        self.generate_button = tk.Button(master, text="Generate", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(master, text="Generated password:")
        self.password_label.pack()

        self.password_text = tk.Text(master, height=1, width=15)  
        self.password_text.pack()

        self.strength_label = tk.Label(master, text="Password strength:")
        self.strength_label.pack()

        self.strength_text = tk.Text(master, height=1, width=15)
        self.strength_text.pack()

        self.response_label = tk.Label(master, text="Do you like this password? (y/n):")
        self.response_label.pack()

        self.response_entry = tk.Entry(master)
        self.response_entry.pack()

        self.response_button = tk.Button(master, text="submit", command=self.check_response)
        self.response_button.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        password = "".join(random.sample(string, length))
        self.password_text.delete(1.0, tk.END)
        self.password_text.insert(tk.END, password)

        if length < 6:
            self.strength_text.delete(1.0, tk.END)
            self.strength_text.insert(tk.END, " weak")
        elif length < 10:
            self.strength_text.delete(1.0, tk.END)
            self.strength_text.insert(tk.END, " moderate")
        else:
            self.strength_text.delete(1.0, tk.END)
            self.strength_text.insert(tk.END, "strong")

    def check_response(self):
        response = self.response_entry.get()
        if response.lower() == 'y':
            self.master.destroy()
        else:
            self.length_entry.delete(0, tk.END)
            self.password_text.delete(1.0, tk.END)
            self.strength_text.delete(1.0, tk.END)
            self.response_entry.delete(0, tk.END)

root = tk.Tk()
my_gui = PasswordGenerator(root)
root.mainloop()