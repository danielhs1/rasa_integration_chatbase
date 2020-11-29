import abc


class EventConsumer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def start_consumption(self, callback):
        raise NotImplementedError
