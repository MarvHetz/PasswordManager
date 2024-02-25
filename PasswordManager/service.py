class Service:
    _service : str
    _username : str
    _password : str
    _domain : str

    def __init__(self, service, username, password, domain):
        self._service = service
        self._username = username
        self._password = password
        self._domain = domain

    @property
    def service(self) -> str:
        return self._service

    @service.setter
    def service(self, service: str):
        self._service = service

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, username: str):
        self._username = username

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = password

    @property
    def domain(self) -> str:
        return self._domain

    @domain.setter
    def domain(self, domain: str):
        self._domain = domain

    def __str__(self):
        return self._service
