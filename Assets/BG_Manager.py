import os
import pygame

class BGManager:
    def __init__(self):
        self.CurrentActiveBG = None
        self.CurrentBGName = None

        self.BackgroundFolder = os.path.join(os.path.dirname(__file__),"Background", "BackgroundScene")

    def ShowBackground(self, BGName):
        
        if BGName == "" or BGName is None:
            return
        
        if BGName == self.CurrentBGName:
            return

        path = os.path.join(
            self.BackgroundFolder,
            f"{BGName}.png"
        )

        if not os.path.exists(path):
            print(f"Background '{BGName}' not found")
            return

        self.CurrentActiveBG = pygame.image.load(path).convert()
        self.CurrentBGName = BGName

    def Render(self, screen):

        if self.CurrentActiveBG:
            screen.blit(self.CurrentActiveBG,(0, 0))

    def GetCurrentBG(self):
        return self.CurrentBGName