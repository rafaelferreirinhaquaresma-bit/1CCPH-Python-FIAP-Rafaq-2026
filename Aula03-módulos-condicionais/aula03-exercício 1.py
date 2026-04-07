import pygame

# Inicializa o mixer
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load("musica.mp3")

# Toca o áudio
pygame.mixer.music.play()

# Mantém o programa rodando enquanto o áudio toca
while pygame.mixer.music.get_busy():
    continue