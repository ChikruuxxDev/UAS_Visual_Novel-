import pygame
import os

class SoundManager:
    def __init__(self):
        pygame.mixer.init()

        self._CurrentBGM = None

        self.BGMFolder = os.path.join(
            os.path.dirname(__file__),
            "BGM"
        )

        self.SFXFolder = os.path.join(
            os.path.dirname(__file__),
            "SFX"
        )

    def PlayBGM(self, bgm_name):

        if bgm_name == "" or bgm_name is None:
            return
        
        if self._CurrentBGM == bgm_name:
            return
        
        path = os.path.join(self.BGMFolder, f"{bgm_name}.mp3")

        if not os.path.exists(path):
            print(f"BGM '{bgm_name}' not found")

        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)
        
        self._CurrentBGM = bgm_name

    def StopBGM(self):
        pygame.mixer.music.stop()
        self._CurrentBGM = None

    def PlaySFX(self, sfx_name):
        
        if sfx_name == "" or sfx_name is None:
            return

        path = os.path.join(
            self.SFXFolder,
            f"{sfx_name}.mp3"
        )

        if not os.path.exists(path):
            print(f"SFX '{sfx_name}' not found")
            return

        pygame.mixer.Sound(path).play()

    def get_CurrentBGM(self):
        return self._CurrentBGM    