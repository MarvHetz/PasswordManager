import time
import pyperclip
import threading
from service import Service
from dbcontroller import DBController


class Model:
    __service_list = []
    __thread1 : threading
    __dbcontroller : DBController

    def __init__(self):
        self.__service_list = []
        self.__dbcontroller = DBController.get_instance()

    @property
    def service_list(self) -> list:
        return self.__service_list

    def add_entry(self, service, username, password, domain):
        self.__service_list.append(Service(service, username, password, domain))

    def copy_domain_to_clipboard(self, index):
        domain = self.__service_list[index[0]].domain
        pyperclip.copy(domain)

    def copy_password_to_clipboard(self, index):
        password = self.__service_list[index[0]].password
        pyperclip.copy(password)
        self.__thread1 = threading.Thread(target=self.__delete_password_from_clipboard)
        self.__thread1.start()

    def __delete_password_from_clipboard(self):
        time.sleep(20)
        pyperclip.copy('')

    def copy_username_to_clipboard(self, index):
        username = self.__service_list[index[0]].username
        pyperclip.copy(username)
