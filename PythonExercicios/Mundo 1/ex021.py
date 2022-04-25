import pygame
pygame.mixer.init()
pygame.init()
print('iniciou')
pygame.mixer.music.load('PythonExercicios\ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('parou')

# Programa não finaliza.