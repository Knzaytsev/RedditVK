from abc import ABCMeta, abstractmethod

class DownloadingPics():
    __metaclass__ = ABCMeta

    @abstractmethod
    def download(self):
        pass