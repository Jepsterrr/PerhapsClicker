import pygame
pygame.init()

# Pygame screen display
width=700
height=500
screen=pygame.display.set_mode([width, height])
clock = pygame.time.Clock()

# Pygame writing & text
FONT_SIZE = 20
TEXT_COLOR = (215, 215, 215)
ENERGY_COLOR = (255, 225, 70)
GOLDEN_COLOR = (220, 165, 30)
YES_COLOR = (0, 255, 0)
NO_COLOR = (255, 50, 0)
GAME_FONT = pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE)

# Energy values & shop
energyNum = 10000000.0
autoEnergy = 0.0
EnergyMultiplier = 10
goldenEnergy = 1000000.0
Shop = False

# Golden Variables
energyX = 1
upgradeLessCost = 1
incomeLessCost = 1
autoEnergyTimer = 100