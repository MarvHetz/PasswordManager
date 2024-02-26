import tkinter as tk
from viewListener import ViewListener

class View:

    _listener : ViewListener
    _listbox_listvar : tk.StringVar
    def __init__(self, master, serviceList):
        self.master = master
        self.master.title("Password Manager")

        self.label_domain = tk.Label(master, text="Domain:")
        self.label_domain.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.entry_domain = tk.Entry(master)
        self.entry_domain.grid(row=0, column=1, padx=5, pady=5)

        self.label_service = tk.Label(master, text="Service:")
        self.label_service.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.entry_service = tk.Entry(master)
        self.entry_service.grid(row=1, column=1, padx=5, pady=5)

        self.label_username = tk.Label(master, text="Username:")
        self.label_username.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.entry_username = tk.Entry(master)
        self.entry_username.grid(row=2, column=1, padx=5, pady=5)

        self.label_password = tk.Label(master, text="Password:")
        self.label_password.grid(row=3, column=0, padx=5, pady=5, sticky="e")

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.grid(row=3, column=1, padx=5, pady=5)

        self.button_save = tk.Button(master, text="Save", command=self._save_password)
        self.button_save.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.label_services = tk.Label(master, text="Saved Services:")
        self.label_services.grid(row=0, column=2, padx=5, pady=5, sticky="e")

        self._listbox_listvar = tk.StringVar(value=serviceList)
        self.listbox_scrollbar = tk.Scrollbar(master, orient=tk.VERTICAL)
        self.listbox_services = tk.Listbox(master, width=30, height=10, yscrollcommand=self.listbox_scrollbar.set, selectmode=tk.SINGLE, listvariable=self._listbox_listvar)
        self.listbox_scrollbar.config(command=self.listbox_services.yview)
        self.listbox_scrollbar.grid(row=1, column=3, rowspan=4, padx=0, pady=5, sticky="ns")
        self.listbox_services.grid(row=1, column=2, rowspan=4, padx=5, pady=5, sticky="nsew")
        self.listbox_services.bind("<Control-d>", lambda x: self._on_control_d())
        self.listbox_services.bind("<Double-Button-1>", self._on_double_click)
        self.listbox_services.bind("<Control-c>", self._on_control_c)

    def _on_control_d(self):
        selected_index = self.listbox_services.curselection()
        self._listener.on_ctrl_d(selected_index)

    def _save_password(self):
        service = self.entry_service.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        domain = self.entry_domain.get()

        self._listener.on_save(service, username, password, domain)

    def _on_double_click(self, event):
        selected_index = self.listbox_services.curselection()
        self._listener.on_double_click(selected_index)

    def set_listener(self, listener : ViewListener):
        self._listener = listener

    def update_listbox(self, serviceList):
        self._listbox_listvar.set(serviceList)

    def _on_control_c(self, event):
        selected_index = self.listbox_services.curselection()
        self._listener.on_ctrl_c(selected_index)
