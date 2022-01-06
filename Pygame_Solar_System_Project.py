import pygame
import sys
import random
import time

def main_menu():
    global mouse_pressed
    global mouse_pressed_quit  
    global mouse_pressed_lesson 
    screen.blit(galaxy,(0,0))
    main_menu_text = font.render("Main Menu", False, "White")   
    instruction_text = font2.render("Instruction", False, "Black")
    lesson_text = font2.render("Lesson", False, "Black") 
    quiz_text = font2.render("Quiz", False, "Black") 
    result_text = font2.render("Results", False, "Black") 
    quit_text = font2.render("Quit", False, "Black") 
    
    screen.blit(instruction_button,(80, 500))
    screen.blit(lesson_button,(320, 500))
    screen.blit(game_button,(560, 500))
    screen.blit(quiz_button,(800, 500))
    screen.blit(quit_button,(1040, 500))  
    
    screen.blit(instruction_text, (100, 530))
    screen.blit(lesson_text, (350, 530))  
    screen.blit(quiz_text, (610, 530))    
    screen.blit(result_text, (840, 530))  
    screen.blit(quit_text, (1090, 530))           
    
    
    screen.blit(main_menu_text,(410,150))
    

       
    mouse_pos = pygame.mouse.get_pos()    
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if instruction_surface.collidepoint(mouse_pos):
            mouse_pressed = True
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if lesson_surface.collidepoint(mouse_pos):
            mouse_pressed = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if game_surface.collidepoint(mouse_pos):
            mouse_pressed = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if quiz_surface.collidepoint(mouse_pos):
            mouse_pressed = True
    if event.type == pygame.MOUSEBUTTONDOWN:
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
font = pygame.font.Font("Pixel_Font.ttf", 75)
font1 = pygame.font.Font("Pixel_Font.ttf", 20)
font2 = pygame.font.Font("Pixel_Font.ttf", 15)
small_font = pygame.font.Font("Pixel_Font.ttf", 12)
average_font = pygame.font.Font("Pixel_Font.ttf", 15)


galaxy = pygame.image.load("SpacePixelArt.jpg").convert()
text1 = font.render("SolarEscape",False, "White")
text2 = font1.render("Press  any  key  to  start",False, "White")
date_text=small_font.render("January  2,  2022", False, "White")
name_text=average_font.render("By:  Awais  and  Zubair", False, "White")
teacher_text=average_font.render("Instructor:  Ms.  Keras", False, "White")
class_code_text=average_font.render("Class:  ICS207", False, "White")

pygame.mixer.music.load("title.wav")
pygame.mixer.music.play(-1)

instruction_button = pygame.Surface((160, 100))
instruction_button.fill("Grey")
instruction_surface = screen.blit(instruction_button,(80, 500))

lesson_button = pygame.Surface((160, 100))
lesson_button.fill("Grey")
lesson_surface = screen.blit(lesson_button,(320, 500))

game_button = pygame.Surface((160, 100))
game_button.fill("Grey")
game_surface = screen.blit(game_button,(560, 500))

quiz_button = pygame.Surface((160, 100))
quiz_button.fill("Grey")
quiz_surface = screen.blit(quiz_button,(800, 500))

quit_button = pygame.Surface((160, 100))
quit_button.fill("Grey")
quit_surface = screen.blit(quit_button,(1040, 500))

keys = pygame.key.get_pressed()
key_pressed = False
mouse_pressed = False
mouse_pressed_quit = False
mouse_pressed_lesson = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(galaxy,(0,0))
    screen.blit(text1,(290,100))
    screen.blit(text2,(450, 550))
    screen.blit(date_text,(0,0)) 
    screen.blit(name_text,(920,560))  
    screen.blit(teacher_text,(920,600))
    screen.blit(class_code_text,(920,640))
    if event.type == pygame.KEYUP:
        key_pressed = True
    if key_pressed == True:
        main_menu()

    pygame.display.update()    
    clock.tick(60)