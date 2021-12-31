import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Solar System Game")
clock = pygame.time.Clock()
font = pygame.font.Font("Downloads/Project/Pixel_Font.ttf", 75)
font1 = pygame.font.Font("Downloads/Project/Pixel_Font.ttf", 20)

galaxy = pygame.image.load("Downloads/Project/SpacePixelArt.jpg").convert()
text1 = font.render("Solar  System",False, "White")
text2 = font1.render("Press  any  button  to  start",False, "White")

key_pressed = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(galaxy,(0,0))
    screen.blit(text1,(290,150))
    screen.blit(text2,(450, 550))   
    if event.type == pygame.KEYUP:
        key_pressed = True
    if key_pressed == True:
        main_menu()

    pygame.display.update()    
    clock.tick(60)