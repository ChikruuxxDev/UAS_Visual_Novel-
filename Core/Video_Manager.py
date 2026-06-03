from AbstractRendering.Rendering import Rendering
import pygame

class VideoManager(Rendering):
    def __init__(self, video_data_list, bg_manager):
        self._VideoData = video_data_list   # Array/List dari JSON
        self._BGManager = bg_manager        # Akses untuk mengganti layar
        
        self._CurrentIndex = 0
        self.IsFinished = False
        
        # Mulai hitung waktu (menggunakan milidetik)
        self._StartTime = pygame.time.get_ticks()
        self._UpdateBackground()

    def _UpdateBackground(self):
        """Memerintahkan BGManager mengganti latar belakang sesuai indeks saat ini"""
        if self._CurrentIndex < len(self._VideoData):
            bg_name = self._VideoData[self._CurrentIndex]["BG"]
            self._BGManager.ShowBackground(bg_name)

    def Update(self):
        """Dipanggil setiap frame (60 FPS) untuk mengecek apakah waktunya ganti gambar"""
        if self.IsFinished:
            return

        # Ambil delay dalam bentuk detik dari JSON, ubah ke milidetik (* 1000)
        current_delay_sec = self._VideoData[self._CurrentIndex]["Delay"]
        current_delay_ms = current_delay_sec * 1000
        time_now = pygame.time.get_ticks()

        # Jika durasi tayang gambar ini sudah habis...
        if time_now - self._StartTime >= current_delay_ms:
            self._CurrentIndex += 1 # Pindah ke gambar selanjutnya
            
            # Jika gambar sudah habis semua = Video Selesai!
            if self._CurrentIndex >= len(self._VideoData):
                self.IsFinished = True
            else:
                self._StartTime = time_now # Reset timer
                self._UpdateBackground()   # Ganti gambar

    def Skip(self):
        """Fungsi jika pemain tidak sabar dan mengklik layar"""
        self.IsFinished = True

    def Render(self, screen):
        # Biarkan kosong. Kita tidak perlu menggambar kotak UI apa pun 
        # karena yang diganti hanya gambar Background (diurus oleh BGManager).
        pass