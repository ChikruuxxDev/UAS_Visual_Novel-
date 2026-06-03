from abc import ABC, abstractmethod

class Serialisasi(ABC):
    @abstractmethod
    def Save(self): #Saving something to the file
        pass

    @abstractmethod
    def Load(self, rawText: str): #Loading something from the file
        pass