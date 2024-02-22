import tkinter as tk
from tkinter import messagebox

class PasswordManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")

        self.label_service = tk.Label(master, text="Service:")
        self.label_service.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.entry_service = tk.Entry(master)
        self.entry_service.grid(row=0, column=1, padx=5, pady=5)

        self.label_username = tk.Label(master, text="Username:")
        self.label_username.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.entry_username = tk.Entry(master)
        self.entry_username.grid(row=1, column=1, padx=5, pady=5)

        self.label_password = tk.Label(master, text="Password:")
        self.label_password.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.grid(row=2, column=1, padx=5, pady=5)

        self.button_save = tk.Button(master, text="Save", command=self.save_password)
        self.button_save.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.label_services = tk.Label(master, text="Saved Services:")
        self.label_services.grid(row=0, column=2, padx=5, pady=5, sticky="e")

        self.listbox_services = tk.Listbox(master, width=30, height=10)
        self.listbox_services.grid(row=1, column=2, rowspan=3, padx=5, pady=5, sticky="nsew")
        self.listbox_services.bind("<Double-Button-1>", self.print_service_data)

    def save_password(self):
        service = self.entry_service.get()
        username = self.entry_username.get()
        password = self.entry_password.get()

        if service and username and password:
            # Here you would typically save the password securely, for example, using encryption
            self.listbox_services.insert(tk.END, service)
            messagebox.showinfo("Success", "Password saved successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def print_service_data(self, event):
        selected_index = self.listbox_services.curselection()
        if selected_index:
            service = self.listbox_services.get(selected_index)
            # Here you can print or do whatever you want with the service data
            messagebox.showinfo("Service Data", f"Service: {service}\nUsername: <username>\nPassword: <password>")
        else:
            messagebox.showerror("Error", "Please select a service.")

def main():
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
