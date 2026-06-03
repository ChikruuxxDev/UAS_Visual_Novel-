import pygame
import os
from AbstractRendering.Rendering import Rendering

class ChoiceBoxManager(Rendering):
    def __init__(self, ListOfChoices):
        # Data Text
        self._Choices = ListOfChoices
        self._Visible = True
        self.ChoicesList = []

        # --- 1. LOAD FONT OSWALD ---
        try:
            font_path = os.path.join("Assets", "Fonts", "Nickname", "Oswald-Medium.ttf")
            self.Font = pygame.font.Font(font_path, 24)
        except FileNotFoundError:
            print("[UI Warning] Font Oswald tidak ditemukan, memakai font bawaan.")
            self.Font = pygame.font.Font(None, 36)

        # --- 2. LOAD ASET FIGMA ---
        try:
            path_statis = os.path.join("Assets", "UI", "choice_btn_statis.png")
            path_hover = os.path.join("Assets", "UI", "choice_btn_hover.png")
            self.bg_statis = pygame.image.load(path_statis).convert_alpha()
            self.bg_hover = pygame.image.load(path_hover).convert_alpha()
        except FileNotFoundError:
            self.bg_statis = None
            self.bg_hover = None
            print("[UI Warning] Aset choice_btn_statis/hover.png tidak ditemukan!")

    def DrawBox(self, screen):
        if not self._Visible:
            return
        
        # [PENTING] Kosongkan list setiap frame agar tidak terjadi memory leak (Bug Fix)
        self.ChoicesList.clear() 
        
        mouse_pos = pygame.mouse.get_pos()

        # Pengaturan Tata Letak Otomatis (Tengah Layar)
        center_x = 1280 // 2
        button_height = 65 # Sesuaikan dengan tinggi aset PNG kamu
        spacing = 20
        
        # Hitung titik awal Y agar responsif berapapun jumlah pilihannya
        total_height = (len(self._Choices) * button_height) + ((len(self._Choices) - 1) * spacing)
        start_y = (720 // 2) - (total_height // 2)

        for i, Choices in enumerate(self._Choices):
            img = self.bg_statis
            
            # Buat area klik (Rect)
            if img:
                rect = img.get_rect(center=(center_x, start_y + (button_height // 2)))
            else:
                # Fallback jika gambar hilang
                rect = pygame.Rect(center_x - 440, start_y, 880, 50)

            # --- LOGIKA HOVER EFFECT ---
            if rect.collidepoint(mouse_pos) and self.bg_hover:
                img = self.bg_hover

            self.ChoicesList.append(rect)

            # Render Tombol (Prioritas PNG, fallback kotak warna)
            if img:
                screen.blit(img, rect)
            else:
                pygame.draw.rect(screen, (30, 30, 30), rect)
                pygame.draw.rect(screen, (255, 255, 255), rect, 2)

            # Render Teks (Di tengah-tengah tombol)
            TextSurface = self.Font.render(Choices["Text"], True, (255, 255, 255))
            txt_rect = TextSurface.get_rect(center=rect.center)
            screen.blit(TextSurface, txt_rect)
            
            # Turunkan koordinat untuk tombol berikutnya
            start_y += button_height + spacing

    def CheckMouseClick(self, event):
        if not self._Visible:
            return
        
        mousePos = pygame.mouse.get_pos()
        
        for i, Rect in enumerate(self.ChoicesList):
            if Rect.collidepoint(mousePos):
                self._Visible = False
                return self._Choices[i]["Next"]
            
    def Update(self):
        pass

    def Render(self, screen):
        # Beri overlay gelap sedikit agar pemain fokus ke pilihan
        overlay = pygame.Surface((1280, 720), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 100))
        screen.blit(overlay, (0, 0))
        
        self.DrawBox(screen)