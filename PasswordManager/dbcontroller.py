import sqlite3


class DBController(object):
    __instance = None
    __connection = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)
        return cls.__instance

    def __new__(cls, *args, **kwargs):
        cls.__connection = sqlite3.connect('services.db')


