import sqlite3
from service import Service

class DBControllerMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DBControllerMeta, cls).__call__(*args, **kwargs)
        return cls._instance


class DBController(metaclass=DBControllerMeta):
    def __init__(self):
        self.__connection = sqlite3.connect('services.db')


    def load_services(self):
        cursor = self.__connection.cursor()
        cursor.execute('SELECT service, username, password, domain FROM services')
        rows = cursor.fetchall()
        cursor.close()
        self.__service_list = []
        for row in rows:
            service = Service(row[0], row[1], row[2], row[3])
            self.__service_list.append(service)
        return self.__service_list

    def add_service(self, service : Service):
        cursor = self.__connection.cursor()
        cursor.execute('INSERT INTO services(service, username, password, domain) VALUES (?,?,?,?)', (service.service, service.username, service.password, service.domain))
        cursor.close()

    def commit_services(self):
        self.__connection.commit()

    def delete_service(self, service : Service):
        cursor = self.__connection.cursor()
        cursor.execute('DELETE FROM services WHERE service = ? and domain = ? and username = ? and password = ?', (service.service, service.domain, service.username, service.password))
        cursor.close()

    def rollback(self):
        self.__connection.rollback()