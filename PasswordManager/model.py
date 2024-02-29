import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import pyperclip
import threading
from service import Service
from dbcontroller import DBController


class Model:
    __service_list = []
    __thread1 : threading
    __dbcontroller : DBController
    __KEY = b'1234567890123456'
    made_changes = False

    def __init__(self):
        self.__service_list = []
        self.__dbcontroller = DBController()
        self.__service_list = self.__dbcontroller.load_services()

    @property
    def service_list(self) -> list:
        return self.__service_list

    def add_entry(self, service, username, password, domain):
        password = self.__encrypt_password(password)
        service = Service(service, username, password,domain)
        self.__service_list.append(service)
        self.__dbcontroller.add_service(service)
        self.made_changes = True

    def copy_domain_to_clipboard(self, index):
        domain = self.__service_list[index[0]].domain
        pyperclip.copy(domain)

    def copy_password_to_clipboard(self, index):
        password = self.__service_list[index[0]].password
        password = self.__decrypt_password(password)
        pyperclip.copy(password)
        self.__thread1 = threading.Thread(target=self.__delete_password_from_clipboard)
        self.__thread1.start()

    def __delete_password_from_clipboard(self):
        time.sleep(20)
        pyperclip.copy('')

    def copy_username_to_clipboard(self, index):
        username = self.__service_list[index[0]].username
        pyperclip.copy(username)

    def commit(self):
        self.__dbcontroller.commit_services()

    def delete_service(self, index):
        service = self.__service_list[index[0]]
        self.__service_list.remove(service)
        self.__dbcontroller.delete_service(service)
        self.made_changes = True

    def rollback(self):
        self.__dbcontroller.rollback()

    def __encrypt_password(self, password):
        backend = default_backend()
        iv = os.urandom(16)  # Generate a random 128-bit (16 bytes) IV
        cipher = Cipher(algorithms.AES(self.__KEY), modes.CBC(iv), backend=backend)
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()

        padded_data = padder.update(password.encode()) + padder.finalize()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        return iv + encrypted_data

    def __decrypt_password(self, encrypted_password):
        backend = default_backend()
        iv = encrypted_password[:16]  # Extract the IV from the ciphertext
        ciphertext = encrypted_password[16:]

        cipher = Cipher(algorithms.AES(self.__KEY), modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()

        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

        return unpadded_data.decode()

