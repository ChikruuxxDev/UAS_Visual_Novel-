import json
import pygame
import os

class CharacterManager:
    def __init__(self):

        self.Characters = {}
        self.Images = {}

        self.LoadCharacterData()
        self.LoadImages()

    def LoadCharacterData(self):

        JsonPath = os.path.join(
            os.path.dirname(__file__),
            "Characters_Data.json"
        )

        with open(JsonPath, "r", encoding="utf-8") as file:
            self.Characters = json.load(file)

    def LoadImages(self):

        for char_name, char_data in self.Characters.items():

            self.Images[char_name] = []

            for expression in char_data["Expresion"]:

                image_path = os.path.join(
                    os.path.dirname(__file__),
                    "CharacterFiles",
                    char_name,
                    expression + ".png"
                )

                image = pygame.image.load(
                    image_path
                ).convert_alpha()

                self.Images[char_name].append(image)

    def GetCharacterImage(self, char_name, expression_index):

        if char_name not in self.Images:
            return None

        if expression_index >= len(self.Images[char_name]):
            return None

        return self.Images[char_name][expression_index]

    def draw_character(self, screen, char_name, expression_index, pos):

        image = self.GetCharacterImage(
            char_name,
            expression_index
        )

        if image:
            screen.blit(image, pos)