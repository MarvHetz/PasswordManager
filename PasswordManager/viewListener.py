from abc import ABC, abstractmethod
class ViewListener(ABC):

    @abstractmethod
    def on_save(self, service, username, password, domain):
        pass

    @abstractmethod
    def on_double_click (self, index):
        pass

    @abstractmethod
    def on_ctrl_d (self, index):
        pass

    @abstractmethod
    def on_ctrl_c(self, index):
        pass

    @abstractmethod
    def on_close(self):
        pass