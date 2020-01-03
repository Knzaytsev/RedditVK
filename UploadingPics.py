from abc import ABCMeta, abstractmethod

class UploadingPics():
    __metaclass__ = ABCMeta

    @abstractmethod
    def upload(self):
        pass