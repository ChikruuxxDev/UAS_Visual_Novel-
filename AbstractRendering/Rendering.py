from abc import ABC , abstractmethod

class Rendering(ABC):
    @abstractmethod
    def Render(self): #Putting something to the screen
        pass
        
    @abstractmethod
    def Update(self): #Updating something that already on the screen
        pass