import sqlite3
from service import Service


class DBController(object):
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