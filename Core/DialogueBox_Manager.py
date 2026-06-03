from AbstractRendering.Rendering import Rendering
import pygame
import os

class DialogeBoxManager(Rendering):
    def __init__(self, text):
        # Text Settings
        self._VisibleDialogue = ""
        self._Dialogue = ""

        self._TypingSpeed = 30 # between 0 - 1000
        self._CharIndex = 0
        self._LastUpdate = pygame.time.get_ticks()

        # Data Text
        self.Text = text # type List
        self._CurrentDialogue = 0
        self._Visible = True
        self._Character = ""

        # --- 1. LOAD FONTS (OSWALD) ---
        try:
            path_oswald_medium = os.path.join("Assets", "Fonts", "Nickname", "Oswald-Medium.ttf")
            path_oswald_semibold = os.path.join("Assets", "Fonts", "Nickname", "Oswald-SemiBold.ttf")
            self.Font = pygame.font.Font(path_oswald_medium, 24)        # Untuk isi teks dialog
            self.NameFont = pygame.font.Font(path_oswald_semibold, 28)  # Untuk nama karakter & indikator
        except FileNotFoundError:
            print("[UI Warning] Font Oswald tidak ditemukan. Menggunakan font default.")
            self.Font = pygame.font.Font(None, 36)
            self.NameFont = pygame.font.Font(None, 40)

        # --- 2. LOAD ASET FIGMA (DIALOG BOX) ---
        try:
            image_path = os.path.join("Assets", "UI", "dialogBox_bg.png")
            self.dialogue_bg = pygame.image.load(image_path).convert_alpha()
            
            # Posisikan dialog box di tengah bawah layar (X=Tengah, Y=490)
            self._sizeBox = self.dialogue_bg.get_rect(centerx=1280 // 2, y=490)
        except FileNotFoundError:
            print(f"[UI Warning] Gambar tidak ditemukan di {image_path}! Menggunakan procedural rect.")
            self.dialogue_bg = None
            # Fallback koordinat jika PNG gagal dimuat
            self._sizeBox = pygame.Rect(140, 500, 1000, 200)

    def TextWrap(self, text, max_width):
        Words = text.split(' ')
        Lines = []
        CurrentLine = ""

        for word in Words:
            Temp = CurrentLine + word + " "
            if self.Font.size(Temp)[0] <= max_width:
                CurrentLine = Temp
            else:
                Lines.append(CurrentLine)
                CurrentLine = word + " "

        if CurrentLine:
            Lines.append(CurrentLine)

        return Lines

    def DrawBox(self, screen):
        if not self._Visible:
            return 
        
        # --- RENDER PNG FIGMA ATAU FALLBACK KOTAK ---
        if hasattr(self, 'dialogue_bg') and self.dialogue_bg:
            screen.blit(self.dialogue_bg, self._sizeBox)
        else:
            pygame.draw.rect(screen, (30, 30, 40), self._sizeBox)
            pygame.draw.rect(screen, (200, 200, 200), self._sizeBox, 3)

    def NextDialogue(self):
        if self._VisibleDialogue != self._Dialogue:
            self._VisibleDialogue = self._Dialogue
            self._CharIndex = len(self._Dialogue)
            return False

        if self._CurrentDialogue < len(self.Text) - 1:
            self._CurrentDialogue += 1
            return False
        
        return True

    def IsFinished(self):
        return (self._CurrentDialogue >= len(self.Text) - 1 and self._VisibleDialogue == self._Dialogue)

    def Update(self):
        if self._CurrentDialogue >= len(self.Text):
            return
        
        DialogueData = self.Text[self._CurrentDialogue]
        self._Character = DialogueData["Char"]

        if self._Dialogue != DialogueData["Text"]:
            self._Dialogue = DialogueData["Text"]
            self._VisibleDialogue = ""
            self._CharIndex = 0

        CurrentTime = pygame.time.get_ticks()

        if CurrentTime - self._LastUpdate > self._TypingSpeed:  
            self._LastUpdate = CurrentTime
        
            if self._CharIndex < len(self._Dialogue):
                self._VisibleDialogue += self._Dialogue[self._CharIndex]
                self._CharIndex += 1

    def Render(self, screen):
        self.Update()

        if not self._Visible:
            return 
        
        self.DrawBox(screen)

        # --- 3. RENDER NAMA KARAKTER ---
        # Menggunakan warna kuning/gold untuk nama karakter agar kontras
        CharacterName = self.NameFont.render(self._Character, True, (255, 204, 0)) 
        screen.blit(CharacterName, (self._sizeBox.x + 40, self._sizeBox.y + 20))

        # --- 4. RENDER TEKS (DENGAN TEXT WRAP) ---
        # Beri padding (jarak aman) 80 pixel agar teks tidak nabrak ujung kanan kotak
        lines = self.TextWrap(self._VisibleDialogue, self._sizeBox.width - 80)
        
        y = self._sizeBox.y + 60
        for line in lines:
            DialogueSurface = self.Font.render(line, True, (255, 255, 255))
            screen.blit(DialogueSurface, (self._sizeBox.x + 40, y))
            y += self.Font.get_height() + 5

        # --- 5. ANIMASI NEXT TEXT INDICATOR ---
        # Indikator " . . . " HANYA muncul dan berkedip jika efek mesin tik sudah selesai
        if self._VisibleDialogue == self._Dialogue:
            if pygame.time.get_ticks() % 1000 < 500:
                indicator_surf = self.NameFont.render(" . . . ", True, (255, 255, 255))
                # Posisikan dinamis di pojok kanan bawah dari ukuran gambar Figma-mu
                indicator_x = self._sizeBox.right - 90
                indicator_y = self._sizeBox.bottom - 45
                screen.blit(indicator_surf, (indicator_x, indicator_y))