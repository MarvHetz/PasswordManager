import pyperclip

from service import Service


class Model:
    _serviceList = []

    def __init__(self):
        self._serviceList = []


    @property
    def serviceList(self) -> list:
        return self._serviceList

    def add_entry(self, service, username, password, domain):
        self._serviceList.append(Service(service, username, password, domain))

    def copy_domain_to_clipboard(self, index):
        domain = self._serviceList[index[0]].domain
        pyperclip.copy(domain)

    def copy_password_to_clipboard(self, index):
        password = self._serviceList[index[0]].password
        pyperclip.copy(password)