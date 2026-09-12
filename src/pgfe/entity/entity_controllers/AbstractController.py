
import abc


class AbstractController(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def return_movement(self):
        pass
