import tkinter as tk
from tkinter import messagebox
from viewListener import ViewListener
from view import View
class Controller(ViewListener):

    _view : View
    def __init__(self):
        root = tk.Tk()
        _view = View(root)
        _view.set_listener(self)
        root.mainloop()

    def on_save(self,service,username,password):
        if service and username and password:
            messagebox.showinfo("Success", "Password saved successfully!")
        else:
            messagebox.showinfo("ERROR", "ERROR!")

    def on_double_click(self,item):
        if item:
            # Here you can print or do whatever you want with the service data
            messagebox.showinfo("Service Data", f"Service: {item}\nUsername: <username>\nPassword: <password>")
        else:
            messagebox.showerror("Error", "Please select a service.")

    def on_ctrl_c(self,item):
        print('test')