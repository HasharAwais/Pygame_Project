import pygame
import sys
import random
import time

def main_menu():
    global mouse_pressed
    global mouse_pressed_quit    
    screen.blit(galaxy,(0,0))
    main_menu_text = font.render("Main Menu", False, "White")    
    screen.blit(main_menu_text,(410,150))
    
    screen.blit(instruction_button,(80, 500))
    screen.blit(lesson_button,(320, 500))
    screen.blit(game_button,(560, 500))
    screen.blit(quiz_button,(800, 500))
    screen.blit(quit_button,(1040, 500))

    mouse_pos = pygame.mouse.get_pos()    
    mouse_pressed_lesson = False
    
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if instruction_surface.collidepoint(mouse_pos):
            mouse_pressed = True
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if lesson_surface.collidepoint(mouse_pos):
            mouse_pressed = True
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if game_surface.collidepoint(mouse_pos):
            mouse_pressed = True
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if quiz_surface.collidepoint(mouse_pos):
            mouse_pressed = True
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if quit_surface.collidepoint(mouse_pos):
            mouse_pressed_quit = True
    
    if mouse_pressed == True:
        screen.blit(galaxy,(0,0))
        
    if mouse_pressed_quit == True:
        pygame.quit()
        sys.exit()
        

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Solar System Game")
clock = pygame.time.Clock()
font = pygame.font.Font("Downloads/Project/Pixel_Font.ttf", 75)
font1 = pygame.font.Font("Downloads/Project/Pixel_Font.ttf", 20)

galaxy = pygame.image.load("Downloads/Project/SpacePixelArt.jpg").convert()
solar_system_diagram = pygame.image.load("Downloads/Project/Solar_System_Diagram.jpg").convert()
solar_system_diagram = pygame.transform.scale(solar_system_diagram, (1280, 720))
astronaut = pygame.image.load("Downloads/Project/Astronaut_Fuel.png").convert_alpha()
asteroid = pygame.image.load("Downloads/Project/Asteroid_Pixel.png").convert_alpha()
text1 = font.render("Solar  System",False, "White")
text2 = font1.render("Press  any  button  to  start",False, "White")

instruction_button = pygame.Surface((160, 100))
instruction_button.fill("Red")
instruction_surface = screen.blit(instruction_button,(80, 500))

lesson_button = pygame.Surface((160, 100))
lesson_button.fill("Red")
lesson_surface = screen.blit(lesson_button,(320, 500))

game_button = pygame.Surface((160, 100))
game_button.fill("Red")
game_surface = screen.blit(game_button,(560, 500))

quiz_button = pygame.Surface((160, 100))
quiz_button.fill("Red")
quiz_surface = screen.blit(quiz_button,(800, 500))

quit_button = pygame.Surface((160, 100))
quit_button.fill("Red")
quit_surface = screen.blit(quit_button,(1040, 500))

key_pressed = False
mouse_pressed = False
mouse_pressed_quit = False

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