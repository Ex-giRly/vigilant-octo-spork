import pygame

pygame.init()

pink = pygame.display.set_mode((400, 300))  
purple = False                              

while not purple:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            purple = True

    pygame.draw.rect(pink, (255, 171, 244), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()

pygame.quit()