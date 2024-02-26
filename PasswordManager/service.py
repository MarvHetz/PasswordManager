class Service:
    __service : str
    __username : str
    __password : str
    __domain : str

    def __init__(self, service, username, password, domain):
        self.__service = service
        self.__username = username
        self.__password = password
        self.__domain = domain

    @property
    def service(self) -> str:
        return self.__service

    @service.setter
    def service(self, service: str):
        self.__service = service

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    def __str__(self):
        return self.__service
