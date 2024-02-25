from abc import ABC, abstractmethod
class ViewListener(ABC):

    @abstractmethod
    def on_save(self, service, username, password, domain):
        pass

    @abstractmethod
    def on_double_click (self, item):
        pass

    @abstractmethod
    def on_ctrl_c (self, item):
        pass