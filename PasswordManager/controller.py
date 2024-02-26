import tkinter as tk
from tkinter import messagebox
from viewListener import ViewListener
from view import View
from model import Model
class Controller(ViewListener):

    _view : View
    _model : Model
    def __init__(self):

        root = tk.Tk()
        self._model = Model()
        serviceList = self._model.serviceList
        self._view = View(root, serviceList)
        self._view.set_listener(self)
        root.mainloop()

    def on_save(self, service, username, password, domain):
        if service and username and password and domain:
           self._model.add_entry(service, username, password, domain)
           self._view.update_listbox(self._model.serviceList)
        else:
            messagebox.showinfo("ERROR", "ERROR!")

    def on_double_click(self, index):
        if index:
            self._model.copy_password_to_clipboard(index)
        else:
            messagebox.showerror("Error", "Please select a service.")

    def on_ctrl_c(self, index):
        if index:
            self._model.copy_domain_to_clipboard(index)
        else:
            messagebox.showerror("Error", "Please select a service.")