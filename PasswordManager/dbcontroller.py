import sqlite3
from service import Service


class DBController(object):
    def __init__(self):
        self.__connection = sqlite3.connect('services.db')


    def load_services(self):
        cursor = self.__connection.cursor()
        cursor.execute('SELECT * FROM services')
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def add_service(self, service : Service):
        cursor = self.__connection.cursor()
        cursor.execute('INSERT INTO services(service, username, password, domain) VALUES (?,?,?,?)', (service.service, service.username, service.password, service.domain))
        cursor.close()
