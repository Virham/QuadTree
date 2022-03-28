import pygame
import random
from QuadTree import QuadTree

capacity = int(input("Capacity for the quad trees: "))

width = 1280
height = 720

win = pygame.display.set_mode((width, height))

tree = QuadTree(pygame.Rect(0, 0, width, height), capacity)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            tree.add(pygame.mouse.get_pos())

    for point in tree.points:
        pygame.draw.circle(win, (255, 0, 0), point, 5)

    tree.draw(win)
    pygame.display.update()

