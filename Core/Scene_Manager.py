from Core.DialogueBox_Manager import DialogeBoxManager
from Core.ChoiceBox_Manager import ChoiceBoxManager
from Core.Video_Manager import VideoManager
from Sound.Sound_Manager import SoundManager
from Assets.BG_Manager import BGManager
from Character.Character_Manager import CharacterManager
from AbstractRendering.Rendering import Rendering

import pygame
import json
import os

class SceneManager(Rendering):
    def __init__(self):
        #JSON to Nodes
        JsonPath = os.path.join(
            os.path.dirname(__file__),  # Core
            "..",                       # REALGAMING
            "Story_Data.json"
        )

        JsonPath = os.path.abspath(JsonPath)

        with open(JsonPath, "r", encoding="utf-8") as file:
            self.Story_Data = json.load(file)
    
        #Scenes 1
        self.CurrentScenesName = "Scene 1"
        self.CurrentScenesData = self.Story_Data[self.CurrentScenesName]

        self.CurrentNode = None

        self.SoundManager = SoundManager()
        self.BGManager = BGManager()
        self.Charactermanager = CharacterManager()

        self.LoadScene(self.CurrentScenesName)
        self.UpdateAudio()

    def LoadScene(self, SceneName):

        if SceneName not in self.Story_Data:
            print(f"Scene'{SceneName}' Can't found")
            return
        
        self.CurrentScenesName = SceneName
        self.CurrentScenesData = self.Story_Data[self.CurrentScenesName]

        #self.BGManager.ShowBackground(self.CurrentScenesData["BG"])

        SceneType = self.CurrentScenesData["Type"]

        bg_data = self.CurrentScenesData.get("BG")
        if isinstance(bg_data, str) and bg_data != "":
            self.BGManager.ShowBackground(bg_data)

        if SceneType == "Dialogue":
            self.CurrentNode = DialogeBoxManager(self.CurrentScenesData["Text"])

        elif SceneType == "Choice":
            self.CurrentNode = ChoiceBoxManager(self.CurrentScenesData["Option"])
        
        elif SceneType == "Video":
            self.CurrentNode = VideoManager(self.CurrentScenesData["BG"], self.BGManager)

        elif SceneType == "PPT":
            pass

        self.UpdateAudio()
    
    def Eventhandler(self,event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return
        
        SceneType = self.CurrentScenesData["Type"]

        if SceneType == "Dialogue":

            Finished = self.CurrentNode.NextDialogue()

            if Finished:
                NextScene = self.CurrentScenesData["Next"]
                self.LoadScene(NextScene)

            self.UpdateAudio()
        
        elif SceneType == "Choice":
            NextScene = self.CurrentNode.CheckMouseClick(event)

            if NextScene:
                self.LoadScene(NextScene)

        elif SceneType == "Video":
            self.CurrentNode.Skip()
            
    
    def UpdateAudio(self):

        SceneType = self.CurrentScenesData["Type"]

        if SceneType != "Dialogue":
            return
        
        DialogIndex = self.CurrentNode._CurrentDialogue

        if DialogIndex >= len(self.CurrentScenesData["Text"]):
            return
        
        DialogData = self.CurrentScenesData["Text"][DialogIndex]

        BGM = DialogData["BGM"]
        SFX = DialogData["SFX"]

        if BGM == "Stop":
            self.SoundManager.StopBGM()
            return
        elif BGM != "" and BGM != self.SoundManager.get_CurrentBGM():
            self.SoundManager.PlayBGM(BGM)

        if SFX != "":
            self.SoundManager.PlaySFX(SFX)

    def Update(self):
        if self.CurrentNode:
            self.CurrentNode.Update()

            SceneType = self.CurrentScenesData.get("Type")
            if SceneType == "Video":
                if getattr(self.CurrentNode, 'IsFinished', False):
                    NextScene = self.CurrentScenesData.get("Next", "")
                    if NextScene and NextScene.strip() != "":
                        self.LoadScene(NextScene)
                    else:
                        print("Peringatan: JSON Video tidak memiliki 'Next' yang valid!")

    def Render(self, screen):

        self.BGManager.Render(screen)

        SceneType = self.CurrentScenesData["Type"]

        if SceneType == "Dialogue":

            DialogIndex = self.CurrentNode._CurrentDialogue
            TextDataList = self.CurrentScenesData["Text"]

            if DialogIndex < 0 or DialogIndex >= len(TextDataList):
                DialogIndex = 0

            if len(TextDataList) > 0:

                CurrentTextData = TextDataList[DialogIndex]

                CharName = CurrentTextData["Char"]
                CharEx = CurrentTextData["CharEx"]
                CharPos = CurrentTextData.get("Pos", "Center")

                if CharPos == "Left":
                    pos_x = 50
                elif CharPos == "Right":
                    pos_x = 550
                else:
                    pos_x = 250

                pos_y = -10

                self.Charactermanager.draw_character(
                    screen,
                    CharName,
                    CharEx,
                    (pos_x, pos_y)
                )

        if self.CurrentNode:
            self.CurrentNode.Render(screen)