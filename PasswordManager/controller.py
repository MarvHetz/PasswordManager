import tkinter as tk
from tkinter import messagebox
from viewListener import ViewListener
from view import View
from model import Model
class Controller(ViewListener):

    __view : View
    __model : Model
    def __init__(self):

        root = tk.Tk()
        self.__model = Model()
        serviceList = self.__model.service_list
        self.__view = View(root, serviceList)
        self.__view.set_listener(self)
        root.mainloop()

    def on_save(self, service, username, password, domain):
        if service and username and password and domain:
           self.__model.add_entry(service, username, password, domain)
           self.__view.update_listbox(self.__model.service_list)
        else:
            messagebox.showinfo("ERROR", "ERROR!")

    def on_double_click(self, index):
        if index:
            self.__model.copy_password_to_clipboard(index)
        else:
            messagebox.showerror("Error", "Please select a service.")

    def on_ctrl_d(self, index):
        if index:
            self.__model.copy_domain_to_clipboard(index)
        else:
            messagebox.showerror("Error", "Please select a service.")

    def on_ctrl_c(self, index):
        if index:
            self.__model.copy_username_to_clipboard(index)
        else:
            messagebox.showerror("Error", "Please select a service.")

    def on_close(self):
        self.__model.commit()

    def on_backspace(self, index):
        if index:
            self.__model.delete_service(index)
            self.__view.update_listbox(self.__model.service_list)
        else:
            messagebox.showerror("Error", "Please select a service.")