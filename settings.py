import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("NeuralNetworkVisualization")

WIDTH, HEIGHT = 1435, 800
FPS = 50
GRAVITY = 0.3
BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
FONT = pygame.font.Font('freesansbold.ttf', 20)
