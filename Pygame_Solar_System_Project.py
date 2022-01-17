import pygame
import sys
import random
import time

def main_menu():
    global mouse_pressed_quit  
    global mouse_pressed_lesson 
    global mouse_pressed_instruction 
    global mouse_pressed_game
    global mouse_pressed_quiz
    global mouse_pressed_result
    
    screen.blit(galaxy,(0,0))
    main_menu_text = font.render("Main Menu", False, "White")   
    instruction_text = average_font.render("Instructions", False, "Black")
    lesson_text = average_font.render("Lesson", False, "Black") 
    game_text = average_font.render("Game", False, "Black")
    quiz_text = average_font.render("Quiz", False, "Black") 
    result_text = average_font.render("Results", False, "Black") 
    quit_text = average_font.render("Quit", False, "Black") 
    
       

    
    mouse_pos = pygame.mouse.get_pos() 
    
    instruction_button = button(160, 67, 30, 500,"Light Grey")
    if event.type == pygame.MOUSEBUTTONDOWN:
        if instruction_button.collidepoint(mouse_pos):
            mouse_pressed_instruction = True
    
    lesson_button = button(160, 67, 240, 500,"Light Grey")
    if event.type == pygame.MOUSEBUTTONDOWN:
        if lesson_button.collidepoint(mouse_pos):
            mouse_pressed_lesson = True    
            
    game_button = button(160, 67, 450, 500,"Light Grey")
    if event.type == pygame.MOUSEBUTTONDOWN:
        if game_button.collidepoint(mouse_pos):
            mouse_pressed_game = True   
    
    quiz_button = button(160, 67, 660, 500,"Light Grey")
    if event.type == pygame.MOUSEBUTTONDOWN:
        if quiz_button.collidepoint(mouse_pos):
            mouse_pressed_quiz = True   
            
    result_button = button(160, 67, 870, 500,"Light Grey")
    if event.type == pygame.MOUSEBUTTONDOWN:
        if result_button.collidepoint(mouse_pos):
            mouse_pressed_result = True   
    
    quit_button = button(160, 67, 1080, 500,"Light Grey")
    if event.type == pygame.MOUSEBUTTONDOWN:
        if quit_button.collidepoint(mouse_pos):
            mouse_pressed_quit = True   
        
    screen.blit(instruction_text, (75, 520))
    screen.blit(lesson_text, (255, 520))
    screen.blit(game_text, (500, 520))  
    screen.blit(quiz_text, (715, 520))    
    screen.blit(result_text, (915, 520))  
    screen.blit(quit_text, (1135, 520))           
    screen.blit(main_menu_text,(460,300))      
        
    if mouse_pressed_instruction == True:
        instruction()
    
    if mouse_pressed_lesson == True:
        lesson()
    
    if mouse_pressed_game == True:
        mercury_level()
    
    if mouse_pressed_quiz == True:
        quiz()
    
    if mouse_pressed_result == True:
        result()
    
    if mouse_pressed_quit == True:
        pygame.quit()
        sys.exit()

def lesson():   
    global sun_mouse_pressed 
    global mercury_mouse_pressed
    global venus_mouse_pressed
    global earth_mouse_pressed 
    global mars_mouse_pressed 
    global asteroid_belt_pressed 
    global jupiter_mouse_pressed 
    global saturn_mouse_pressed 
    global uranus_mouse_pressed 
    global neptune_mouse_pressed 
    global back_mouse_pressed

    font2 = pygame.font.Font("Pixel_Font.ttf", 50)
    screen.blit(solar_system_diagram, (0, 0))
    lesson_text = font2.render("Lesson Menu", False, "White")
    screen.blit(lesson_text, (350, 75))
    mouse_pos = pygame.mouse.get_pos()  

    sun_surface = screen.blit(sun, (0, 181))
    mercury_surface = screen.blit(mercury, (197, 334))
    venus_surface = screen.blit(venus, (252, 329))
    earth_surface = screen.blit(earth, (331, 323))            
    mars_surface = screen.blit(mars, (440, 328)) 
    jupiter_surface = screen.blit(jupiter, (590, 305))
    saturn_surface = screen.blit(saturn, (693, 319))
    uranus_surface = screen.blit(uranus, (843, 318))
    neptune_surface = screen.blit(neptune, (961, 317))                        
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if sun_surface.collidepoint(mouse_pos):
            sun_mouse_pressed = True
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        if mercury_surface.collidepoint(mouse_pos):
            mercury_mouse_pressed = True 
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        if venus_surface.collidepoint(mouse_pos):
            venus_mouse_pressed = True
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        if earth_surface.collidepoint(mouse_pos):
            earth_mouse_pressed = True
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        if mars_surface.collidepoint(mouse_pos):
            mars_mouse_pressed = True 
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        if jupiter_surface.collidepoint(mouse_pos):
            jupiter_mouse_pressed = True 
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        if saturn_surface.collidepoint(mouse_pos):
            saturn_mouse_pressed = True 
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if uranus_surface.collidepoint(mouse_pos):
            uranus_mouse_pressed = True 
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        if neptune_surface.collidepoint(mouse_pos):
            neptune_mouse_pressed = True 
            
    asteroid_belt_button1 = invisible_button(108, 720, 482, 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button1.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button2 = invisible_button(22, 352, 460 , 369)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button2.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button3 = invisible_button(22, 327, 460 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button3.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button4 = invisible_button(7, 272, 453 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button4.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button5 = invisible_button(4, 242, 449 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button5.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button6 = invisible_button(8, 230, 441 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button6.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button7 = invisible_button(8, 230, 433 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button7.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button8 = invisible_button(8, 180, 425 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button8.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button9 = invisible_button(8, 160, 417 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button9.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button10 = invisible_button(8, 145, 409 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button10.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button11 = invisible_button(12, 127, 397 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button11.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button12 = invisible_button(12, 105, 385 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button12.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button13 = invisible_button(12, 90, 373 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button13.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button14 = invisible_button(12, 73, 361 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button14.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button15 = invisible_button(12, 58, 349 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button15.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button16 = invisible_button(12, 45, 337 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button16.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button17 = invisible_button(12, 29, 325 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button17.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button18 = invisible_button(23, 18, 302 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button18.collidepoint(mouse_pos):
            asteroid_belt_pressed = True

    asteroid_belt_button19 = invisible_button(7, 287, 453 , 436)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button19.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button20 = invisible_button(4, 262, 449 , 459)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button20.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button21 = invisible_button(8, 250, 441 , 471)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button21.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button22 = invisible_button(8, 250, 433 , 471)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button22.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button23 = invisible_button(8, 220, 425 , 521)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button23.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button24 = invisible_button(8, 180, 417 , 541)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button24.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button25 = invisible_button(8, 165, 409 , 556)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button25.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button26 = invisible_button(12, 147, 397 , 574)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button26.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button27 = invisible_button(12, 125, 385 , 596)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button27.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button28 = invisible_button(12, 110, 373 , 611)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button28.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button29 = invisible_button(12, 93, 361 , 628)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button29.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button30 = invisible_button(12, 78, 349 , 643)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button30.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button31 = invisible_button(12, 65, 337 , 656)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button31.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button32 = invisible_button(12, 49, 325 , 672)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button32.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button33 = invisible_button(50, 38, 275 , 683)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button33.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button34 = invisible_button(45, 188, 586 , 392)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button34.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
    asteroid_belt_button35 = invisible_button(45, 188, 586 , 117)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if asteroid_belt_button35.collidepoint(mouse_pos):
            asteroid_belt_pressed = True
            
    kuiper_belt_button1 = invisible_button(126, 720, 1024 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if kuiper_belt_button1.collidepoint(mouse_pos):
            kuiper_belt_pressed = True

    kuiper_belt_button2 = invisible_button(31, 317, 993 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if kuiper_belt_button2.collidepoint(mouse_pos):
            kuiper_belt_pressed = True

    kuiper_belt_button3 = invisible_button(16, 272, 977 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if kuiper_belt_button3.collidepoint(mouse_pos):
            kuiper_belt_pressed = True
            
    kuiper_belt_button4 = invisible_button(12, 159, 965 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if kuiper_belt_button4.collidepoint(mouse_pos):
            kuiper_belt_pressed = True

    kuiper_belt_button5 = invisible_button(12, 115, 953 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if kuiper_belt_button5.collidepoint(mouse_pos):
            kuiper_belt_pressed = True
            
    kuiper_belt_button4 = invisible_button(21, 73, 931 , 0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if kuiper_belt_button4.collidepoint(mouse_pos):
            kuiper_belt_pressed = True
            
            
    
    if sun_mouse_pressed == True:
        screen.blit(galaxy,(0,0))
 
    
    if mercury_mouse_pressed == True:
        screen.blit(galaxy,(0,0))
        
    if venus_mouse_pressed == True:
        screen.blit(galaxy,(0,0))
        
    if earth_mouse_pressed == True:
        screen.blit(galaxy,(0,0))  
    
    if mars_mouse_pressed == True:
        screen.blit(galaxy,(0,0))  
        
    if asteroid_belt_pressed == True:
        screen.blit(galaxy,(0,0))  
        
    if jupiter_mouse_pressed == True:
        screen.blit(galaxy,(0,0))  
        
    if saturn_mouse_pressed == True:
        screen.blit(galaxy,(0,0))  

    if uranus_mouse_pressed == True:
        screen.blit(galaxy,(0,0))
        
    if neptune_mouse_pressed == True:
        screen.blit(galaxy,(0,0)) 

def mercury_level():
    global astronaut_x_mercury
    global astronaut_y_mercury
    global astronaut_collide_mercury
    screen.blit(mercury_background,(0,0))        
    screen.blit(fuel,(100,430))
  
    keys = pygame.key.get_pressed() 
    if not event.type == pygame.KEYDOWN:
        screen.blit(astronaut_left,(astronaut_x_mercury,astronaut_y_mercury))
    if event.type == pygame.KEYDOWN and not keys[pygame.K_RIGHT]:
        screen.blit(astronaut_left,(astronaut_x_mercury,astronaut_y_mercury))
    if keys[pygame.K_LEFT]:
        astronaut_x_mercury-=5
        screen.blit(astronaut_left,(astronaut_x_mercury,astronaut_y_mercury))
    if keys[pygame.K_RIGHT]:
        astronaut_x_mercury+=5
        screen.blit(astronaut_right,(astronaut_x_mercury,astronaut_y_mercury))  
    astronaut_button = invisible_button(80, 124, astronaut_x_mercury, astronaut_y_mercury)
    fuel_button1 = invisible_button(25, 91, 100 , 430)
    if (pygame.Rect.colliderect(astronaut_button, fuel_button1)):
        astronaut_collide_mercury = True 
    
    if astronaut_collide_mercury == True:
        venus_level()

def venus_level():
    global astronaut_x_venus
    global astronaut_y_venus
    global astronaut_collide_venus 
    global comet_collide
    global fuel_x_venus
    global fuel_y_venus
    global comet1_x
    global comet1_y
    global comet2_x
    global comet2_y
    global comet3_x
    global comet3_y    
    global comet4_x
    global comet4_y    
    screen.blit(venus_bg,(0,0))
    screen.blit(fuel,(fuel_x_venus, fuel_y_venus))

    keys = pygame.key.get_pressed() 
    if not event.type == pygame.KEYDOWN:
        screen.blit(astronaut_left,(astronaut_x_venus,astronaut_y_venus))
    if event.type == pygame.KEYDOWN and not keys[pygame.K_RIGHT]:
        screen.blit(astronaut_left,(astronaut_x_venus,astronaut_y_venus))
    if keys[pygame.K_LEFT]:
        astronaut_x_venus-=5
        screen.blit(astronaut_left,(astronaut_x_venus,astronaut_y_venus))
    if keys[pygame.K_RIGHT]:
        astronaut_x_venus+=5
        screen.blit(astronaut_right,(astronaut_x_venus,astronaut_y_venus))  
    astronaut_button = invisible_button(80, 124, astronaut_x_venus, astronaut_y_venus)
    fuel_button2 = invisible_button(25, 91, fuel_x_venus , fuel_y_venus)
    comet1_button = invisible_button(101.25, 241.5, comet1_x , comet1_y) 
    comet2_button = invisible_button(101.25, 241.5, comet2_x , comet2_y) 
    comet3_button = invisible_button(101.25, 241.5, comet3_x , comet3_y) 
    comet4_button = invisible_button(101.25, 241.5, comet4_x , comet4_y) 
    
    
    if (pygame.Rect.colliderect(astronaut_button, fuel_button2)):
        astronaut_collide_venus = True 
    if (pygame.Rect.colliderect(astronaut_button, comet1_button)):
        comet_collide = True 
    if (pygame.Rect.colliderect(astronaut_button, comet2_button)):
        comet_collide = True 
    if (pygame.Rect.colliderect(astronaut_button, comet3_button)):
        comet_collide = True 
    if (pygame.Rect.colliderect(astronaut_button, comet4_button)):
        comet_collide = True 
        
    screen.blit(comet,(comet1_x,comet1_y))
    screen.blit(comet,(comet2_x,comet2_y))
    screen.blit(comet,(comet3_x,comet3_y))
    screen.blit(comet,(comet4_x,comet4_y))
    
    fuel_y_venus+=7
    comet1_y+=7.5
    comet2_y+=7.5
    comet3_y+=7.5
    comet4_y+=7.5
    
    if fuel_y_venus>=883:
        fuel_y_venus = random.randint(-1500, -1200)
        fuel_x_venus = random.randint(1, 1280)
    
    
    if fuel_y_venus>=883:
        fuel_y_venus = random.randint(-1000, -100)
        fuel_x_venus = random.randint(1, 1280)
        
    if comet1_y >= 961.5:    
        comet1_x= random.randint(1,1280)
        comet1_y= random.randint(-500, -100)
    if comet2_y >= 961.5:    
        comet2_x= random.randint(1,1280)
        comet2_y= random.randint(-500, -100)
    if comet3_y >= 961.5:    
        comet3_x= random.randint(1,1280)
        comet3_y= random.randint(-500, -100)
    if comet4_y >= 961.5:    
        comet4_x= random.randint(1,1280)
        comet4_y= random.randint(-500, -100)
    
    if astronaut_collide_venus == True:
        asteroid_belt_game()
    
    if comet_collide == True:
        screen.blit(galaxy,(0,0))
        screen.blit(game_over,(290,150))


def asteroid_belt_game():
    screen.blit(galaxy,(0,0))

def quiz():
    global mouse_correct
    global mouse_wrong
    global image_time
    global quiz_counter
    mouse_pos = pygame.mouse.get_pos() 

    title = font1.render("What  is  left  after  a  planetary  nebula  occurs?",False,"White")
    top_left = small_font.render("White dwarf",False,"White")
    top_right = small_font.render("Black  hole",False,"White")
    bottom_left = small_font.render("Neutron  star",False,"White")
    bottom_right = small_font.render("Super  red  giant",False,"White")
    wrong_text = font.render("Incorrect  Answer!", False, "White")
    right_text = font.render("Correct  Answer!", False, "White")

    quiz_background = pygame.image.load("QuizBackground.jpg").convert()
    quiz_title = pygame.image.load("QuizTitle.jpg")
    quiz_button_top_left = pygame.image.load("QuizFunctionButton.jpg")
    quiz_button_top_right = pygame.image.load("QuizFunctionButton.jpg")
    quiz_button_bottom_left = pygame.image.load("QuizFunctionButton.jpg")
    quiz_button_bottom_right = pygame.image.load("QuizFunctionButton.jpg")

    screen.blit(quiz_background,(0,0))
    screen.blit(quiz_title,(174,50))
    top_left_surface = screen.blit(quiz_button_top_left,(172,236))
    top_right_surface = screen.blit(quiz_button_top_right, (663,235))
    bottom_left_surface = screen.blit(quiz_button_bottom_left, (172,374))
    bottom_right_surface = screen.blit(quiz_button_bottom_right, (664,376))

    screen.blit(title,(254,90))
    screen.blit(top_left,(322,276))
    screen.blit(top_right, (833,275))
    screen.blit(bottom_left, (322,414))
    screen.blit(bottom_right, (814,416))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if top_left_surface.collidepoint(mouse_pos):
            mouse_correct = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if top_right_surface.collidepoint(mouse_pos):
            mouse_wrong = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if bottom_left_surface.collidepoint(mouse_pos):
            mouse_wrong = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if bottom_right_surface.collidepoint(mouse_pos):
            mouse_wrong = True

    if mouse_wrong:
        if image_time>0:
            image_time-=1
            screen.blit(quiz_background,(0,0))
            screen.blit(wrong_text,(100,300))
        if image_time<=0:
            pygame.MOUSEBUTTONDOWN == False
            question2()

    if mouse_correct:
        if image_time>0:
            image_time-=1
            screen.blit(quiz_background,(0,0))
            screen.blit(right_text,(130,300))
        if image_time<=0:
            pygame.MOUSEBUTTONDOWN == False
            quiz_counter+=20
            question2()


mouse_wrong2=bool(False)
mouse_correct2=bool(False)
image_time2=30

def question2():
    global mouse_correct2
    global mouse_wrong2
    global image_time2
    global quiz_counter
    mouse_pos = pygame.mouse.get_pos()    

    title2 = font1.render("Where  in  the  solar  system  is  the  asteroid  belt  located?",False,"White")
    top_left2 = small_font.render("Between  Jupiter  and  Saturn",False,"White")
    top_right2 = small_font.render("Between  Mars  and  Jupiter",False,"White")
    bottom_left2 = small_font.render("Between  Mercury  and  Venus",False,"White")
    bottom_right2 = small_font.render("Between  Earth  and  Mars",False,"White")
    wrong_text2 = font.render("Incorrect  Answer!", False, "White")
    right_text2 = font.render("Correct  Answer!", False, "White")

    quiz_background2 = pygame.image.load("QuizBackground.jpg").convert()
    quiz_title2 = pygame.image.load("QuizTitle.jpg")
    quiz_button_top_left2 = pygame.image.load("QuizFunctionButton.jpg")
    quiz_button_top_right2 = pygame.image.load("QuizFunctionButton.jpg")
    quiz_button_bottom_left2 = pygame.image.load("QuizFunctionButton.jpg")
    quiz_button_bottom_right2 = pygame.image.load("QuizFunctionButton.jpg")

    screen.blit(quiz_background2,(0,0))
    screen.blit(quiz_title2,(174,50))
    top_left_surface2 = screen.blit(quiz_button_top_left2,(172,236))
    top_right_surface2 = screen.blit(quiz_button_top_right2, (663,235))
    bottom_left_surface2 = screen.blit(quiz_button_bottom_left2, (172,374))
    bottom_right_surface2 = screen.blit(quiz_button_bottom_right2, (664,376))

    screen.blit(title2,(234,90))
    screen.blit(top_left2,(272,276))
    screen.blit(top_right2, (783,275))
    screen.blit(bottom_left2, (272,414))
    screen.blit(bottom_right2, (774,416))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if top_left_surface2.collidepoint(mouse_pos):
            mouse_wrong2 = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if top_right_surface2.collidepoint(mouse_pos):
            mouse_correct2 = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if bottom_left_surface2.collidepoint(mouse_pos):
            mouse_wrong2 = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if bottom_right_surface2.collidepoint(mouse_pos):
            mouse_wrong2 = True

    if mouse_wrong2:
        if image_time2>0:
            image_time2-=1
            screen.blit(quiz_background2,(0,0))
            screen.blit(wrong_text2,(100,300))
        if image_time2<=0:
            pygame.MOUSEBUTTONDOWN == False
            question3()

    if mouse_correct2:
        if image_time2>0:
            image_time2-=1
            screen.blit(quiz_background2,(0,0))
            screen.blit(right_text2,(130,300))
        if image_time2<=0:
            pygame.MOUSEBUTTONDOWN == False
            quiz_counter+=20
            question3()

mouse_wrong3=bool(False)
mouse_correct3=bool(False)
image_time3=30

def question3():
    global mouse_correct3
    global mouse_wrong3
    global image_time3
    global quiz_counter
    mouse_pos = pygame.mouse.get_pos()    

    title3 = font1.render("How  do  solar  systems  form  and  what  is  this  theory  called?",False,"White")

    top_left3 = small_font.render("Solar  Nebula  Theory  -  Planets  form  from  ",False,"White")
    another_top_left3 = small_font.render("a  stellar  nebula  and  leftovers  form  a  star",False,"White")

    top_right3 = small_font.render("Big  Bang  -  Star  forms  from  a  stellar  nebula  ",False,"White")
    another_top_right3 = small_font.render("and  leftovers  form  planets",False,"White")

    bottom_left3 = small_font.render("Solar  Nebula  Theory  -  Star  forms  from  a  stellar  ",False,"White")
    another_bottom_left3 = small_font.render("nebula  and  leftovers  form  planets",False,"White")

    bottom_right3 = small_font.render("All  of  the  above",False,"White")
    wrong_text3 = font.render("Incorrect  Answer!", False, "White")
    right_text3 = font.render("Correct  Answer!", False, "White")

    quiz_background3 = pygame.image.load("QuizBackground.jpg").convert()
    quiz_title3 = pygame.image.load("QuizTitle.jpg")
    quiz_button_top_left3 = pygame.image.load("QuizFunctionButton.jpg")
    quiz_button_top_right3 = pygame.image.load("QuizFunctionButton.jpg")
    quiz_button_bottom_left3 = pygame.image.load("QuizFunctionButton.jpg")
    quiz_button_bottom_right3 = pygame.image.load("QuizFunctionButton.jpg")

    screen.blit(quiz_background3,(0,0))
    screen.blit(quiz_title3,(174,50))
    top_left_surface3 = screen.blit(quiz_button_top_left3,(172,236))
    top_right_surface3 = screen.blit(quiz_button_top_right3, (663,235))
    bottom_left_surface3 = screen.blit(quiz_button_bottom_left3, (172,374))
    bottom_right_surface3 = screen.blit(quiz_button_bottom_right3, (664,376))

    screen.blit(title3,(210,90))
    screen.blit(top_left3,(192,276))
    screen.blit(another_top_left3,(196,288))
    screen.blit(top_right3, (683,275))
    screen.blit(another_top_right3, (687,287))
    screen.blit(bottom_left3, (172,414))
    screen.blit(another_bottom_left3,(176,426))
    screen.blit(bottom_right3, (814,416))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if top_left_surface3.collidepoint(mouse_pos):
            mouse_wrong3 = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if top_right_surface3.collidepoint(mouse_pos):
            mouse_wrong3 = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if bottom_left_surface3.collidepoint(mouse_pos):
            mouse_correct3 = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if bottom_right_surface3.collidepoint(mouse_pos):
            mouse_wrong3 = True

    if mouse_wrong3:
        if image_time3>0:
            image_time3-=1
            screen.blit(quiz_background3,(0,0))
            screen.blit(wrong_text3,(100,300))
        if image_time3<=0:
            pygame.MOUSEBUTTONDOWN == False
            question4()

    if mouse_correct3:
        if image_time3>0:
            image_time3-=1
            screen.blit(quiz_background3,(0,0))
            screen.blit(right_text3,(130,300))
        if image_time3<=0:
            pygame.MOUSEBUTTONDOWN == False
            quiz_counter+=20
            question4()

mouse_wrong4=bool(False)
mouse_correct4=bool(False)
image_time4=30

def question4():
    global mouse_correct4
    global mouse_wrong4
    global image_time4
    global quiz_counter
    mouse_pos = pygame.mouse.get_pos()    

    title4 = font1.render("What  is  the  correct  timeline  for  a  massive  star?",False,"White")

    top_left4 = small_font.render("Massive star  -  Red Giant  -  Supernova  ",False,"White")
    another_top_left4 = small_font.render("-  Black  hole  or  Neutron  star",False,"White")

    top_right4 = small_font.render("Massive  star  -  Supergiant  -  Planetary  nebula  ",False,"White")
    another_top_right4 = small_font.render("-  Black  hole  or  Neutron  star",False,"White")

    bottom_left4 = small_font.render("All  of  the  above",False,"White")

    bottom_right4 = small_font.render("Massive star  -  Supergiant  -  Supernova  ",False,"White")
    another_bottom_right4 = small_font.render("-  Black  hole  or  Neutron  star",False,"White")

    wrong_text4 = font.render("Incorrect  Answer!", False, "White")
    right_text4 = font.render("Correct  Answer!", False, "White")

    quiz_background4 = pygame.image.load("QuizBackground.jpg").convert()
    quiz_title4 = pygame.image.load("QuizTitle.jpg")
    quiz_button_top_left4 = pygame.image.load("QuizFunctionButton.jpg")
    quiz_button_top_right4 = pygame.image.load("QuizFunctionButton.jpg")
    quiz_button_bottom_left4 = pygame.image.load("QuizFunctionButton.jpg")
    quiz_button_bottom_right4 = pygame.image.load("QuizFunctionButton.jpg")

    screen.blit(quiz_background4,(0,0))
    screen.blit(quiz_title4,(174,50))
    top_left_surface4 = screen.blit(quiz_button_top_left4,(172,236))
    top_right_surface4 = screen.blit(quiz_button_top_right4, (663,235))
    bottom_left_surface4 = screen.blit(quiz_button_bottom_left4, (172,374))
    bottom_right_surface4 = screen.blit(quiz_button_bottom_right4, (664,376))

    screen.blit(title4,(234,90))
    screen.blit(top_left4,(222,276))
    screen.blit(another_top_left4,(226,288))
    screen.blit(top_right4,(683,275))
    screen.blit(another_top_right4,(687,287))
    screen.blit(bottom_left4,(322,414))
    screen.blit(bottom_right4,(714,416))
    screen.blit(another_bottom_right4,(718,428))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if top_left_surface4.collidepoint(mouse_pos):
            mouse_wrong4 = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if top_right_surface4.collidepoint(mouse_pos):
            mouse_wrong4 = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if bottom_left_surface4.collidepoint(mouse_pos):
            mouse_wrong4 = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if bottom_right_surface4.collidepoint(mouse_pos):
            mouse_correct4 = True

    if mouse_wrong4:
        if image_time4>0:
            image_time4-=1
            screen.blit(quiz_background4,(0,0))
            screen.blit(wrong_text4,(100,300))
        if image_time4<=0:
            pygame.MOUSEBUTTONDOWN == False
            question5()

    if mouse_correct4:
        if image_time4>0:
            image_time4-=1
            screen.blit(quiz_background4,(0,0))
            screen.blit(right_text4,(130,300))
        if image_time4<=0:
            pygame.MOUSEBUTTONDOWN == False
            quiz_counter+=20
            question5()

mouse_wrong5=bool(False)
mouse_correct5=bool(False)
image_time5=30

def question5():
    global mouse_correct5
    global mouse_wrong5
    global image_time5
    global quiz_counter
    mouse_pos = pygame.mouse.get_pos()    

    title5 = font1.render("Where  do  comets  come  from?",False,"White")
    left5 = small_font.render("The  asteroid  belt",False,"White")
    right5 = small_font.render("Oort  Cloud  and  Kuiper  Belt",False,"White")
    wrong_text5 = font.render("Incorrect  Answer!", False, "White")
    right_text5 = font.render("Correct  Answer!", False, "White")

    quiz_background5 = pygame.image.load("QuizBackground.jpg").convert()
    quiz_title5 = pygame.image.load("QuizTitle.jpg")
    quiz_button_left5 = pygame.image.load("QuizFunctionButton.jpg")
    quiz_button_right5 = pygame.image.load("QuizFunctionButton.jpg")

    screen.blit(quiz_background5,(0,0))
    screen.blit(quiz_title5,(174,50))
    left_surface5 = screen.blit(quiz_button_left5,(172,236))
    right_surface5 = screen.blit(quiz_button_right5, (663,235))

    screen.blit(title5,(434,90))
    screen.blit(left5,(312,276))
    screen.blit(right5, (763,275))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if left_surface5.collidepoint(mouse_pos):
            mouse_wrong5 = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if right_surface5.collidepoint(mouse_pos):
            mouse_correct5 = True

    if mouse_wrong5:
        if image_time5>0:
            image_time5-=1
            screen.blit(quiz_background5,(0,0))
            screen.blit(wrong_text5,(100,300))
        if image_time5<=0:
            pygame.MOUSEBUTTONDOWN == False
            quiz_end()

    if mouse_correct5:
        if image_time5>0:
            image_time5-=1
            screen.blit(quiz_background5,(0,0))
            screen.blit(right_text5,(130,300))
        if image_time5<=0:
            pygame.MOUSEBUTTONDOWN == False
            quiz_counter+=20
            quiz_end()

def quiz_end():
    quiz_end_background = pygame.image.load("QuizBackground.jpg").convert()
    ending_message = font1.render("Congratulations,  you  have  finished  the  quiz!",False,"White")
    screen.blit(quiz_end_background,(0,0))
    screen.blit(ending_message,(300,300))


def instruction():
    instruction_background = pygame.image.load("instruction.jpg")
    screen.blit(instruction_background, (0,0))

    instruction_title = font.render("Instructions", False, "White")

    instruction_function_text = small_font.render("In  our  pygame  project  the  objective  of  the game  is  for  the  user  to  play  as  an  extraterrestrial  ", False, "White") 

    instruction_function_text_2 = small_font.render("being  in  a  ship  attempting  to  return  home.  There  are  many  obstacles,  some  being:  the  sun  turning", False, "White") 

    instruction_function_text_3 = small_font.render("into  a  red  giant,  planet  levels,  and  the  asteroid  belt.  There  will  be  a  timer  that  informs  you  how  ", False, "White")

    instruction_function_text_4 = small_font.render("long  you  have  before  the  sun  turns  into  a  red  giant. You  will  have  to  be  at  Jupiter  before  ", False, "White")

    instruction_function_text_5 = small_font.render("the  timer  runs  out  or  else  you  lose  the  game.  Additionally,  there  will  be  planet  levels  you  have  to  ", False, "White")

    instruction_function_text_6 = small_font.render("complete  in  order  to  collect  fuel.  Each  planet  has  fuel  because  you  left  behind  a  little  fuel  in  each  ", False, "White")

    instruction_function_text_7 = small_font.render("of  the  planets  accidentally.  In  order  to  collect  fuel  all  you  have  to  do  is  collide  into  it  with  your.  ", False, "White")

    instruction_function_text_8 = small_font.render("character.  You  have  to  collect  fuel  from  each  planet  in  order  to  move  on.  The  controls  in  order  to  ", False, "White") 

    instruction_function_text_9 = small_font.render("move  will  be  the  arrow  keys,  the  top  arrow  key  will  be  used  to  move  to  the  left,  the  bottom  ", False, "White") 

    instruction_function_text_10 = small_font.render("arrow  key  will  be  used  to  move  downwards,  and  the  right  arrow  key  will  be  used  to  move  to  the  right.", False, "White")

    screen.blit(instruction_title, (275,135))
    screen.blit(instruction_function_text,(210,280))
    screen.blit(instruction_function_text_2,(210,295))
    screen.blit(instruction_function_text_3,(210,310))
    screen.blit(instruction_function_text_4,(210,325))
    screen.blit(instruction_function_text_5,(210,340))
    screen.blit(instruction_function_text_6,(210,355))
    screen.blit(instruction_function_text_7,(210,370))
    screen.blit(instruction_function_text_8,(210,385))
    screen.blit(instruction_function_text_9,(210,400))
    screen.blit(instruction_function_text_10,(210,415))

def result():
    result_background = pygame.image.load("SpacePixelArt.jpg").convert()
    screen.blit(result_background,(0,0))
    score = ((quiz_counter/100)*1000)
    result_text = font.render("Your  Score  is",False,"White")
    result_text2 = font.render(str(score),False,"White")
    result_text3 = font.render("Percent",False,"White")
    screen.blit(result_text,(100,200))
    screen.blit(result_text2,(900,200))
    screen.blit(result_text3,(100,300))    
    

def button(width, height, x_surface, y_surface, colour):
    button = pygame.Surface((width, height))
    button.fill(colour)
    mouse_pos = pygame.mouse.get_pos()        
    button_surface = screen.blit(button, (x_surface, y_surface))
    return button_surface

def invisible_button(width, height, x_surface, y_surface):
    button = pygame.Surface((width, height))
    button.set_alpha(0)
    mouse_pos = pygame.mouse.get_pos()        
    button_surface = screen.blit(button, (x_surface, y_surface))
    return button_surface

        

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Solar System Game")
clock = pygame.time.Clock()
font = pygame.font.Font("Pixel_Font.ttf", 75)
font1 = pygame.font.Font("Pixel_Font.ttf", 20)

galaxy = pygame.image.load("SpacePixelArt.jpg").convert()
solar_system_diagram = pygame.image.load("Solar_System_Diagram.jpg").convert()
solar_system_diagram = pygame.transform.scale(solar_system_diagram, (1280, 720))
sun = pygame.image.load("sun_pygame.png").convert_alpha()
sun = pygame.transform.scale(sun, (166, 332))
mercury = pygame.image.load("mercury_pygame.png").convert_alpha()
mercury = pygame.transform.scale(mercury, (30, 30))
venus = pygame.image.load("venus_pygame.png").convert_alpha()
venus = pygame.transform.scale(venus, (37, 36))
earth = pygame.image.load("earth_pygame.png").convert_alpha()
earth = pygame.transform.scale(earth, (49, 49))
mars = pygame.image.load("mars_pygame.png").convert_alpha()
mars = pygame.transform.scale(mars, (41, 41))
jupiter = pygame.image.load("jupiter_pygame.png").convert_alpha()
jupiter = pygame.transform.scale(jupiter, (87, 87))
saturn = pygame.image.load("saturn_pygame.png").convert_alpha()
saturn = pygame.transform.scale(saturn, (116, 59))
uranus = pygame.image.load("uranus_pygame.png").convert_alpha()
uranus = pygame.transform.scale(uranus, (61, 61))
neptune = pygame.image.load("neptune_pygame.png").convert_alpha()
neptune = pygame.transform.scale(neptune, (63, 63))
mercury_background = pygame.image.load("mercury_background.png").convert()
astronaut_right = pygame.image.load("Astronaut_Right.png").convert_alpha()
astronaut_right = pygame.transform.scale(astronaut_right, (80, 124))
astronaut_left = pygame.image.load("Astronaut_Left.png").convert_alpha()
astronaut_left = pygame.transform.scale(astronaut_left, (80, 124))
asteroid = pygame.image.load("Asteroid_Pixel.png").convert_alpha()
fuel = pygame.image.load("fuel.png").convert_alpha()
fuel = pygame.transform.scale(fuel, (25, 93))
venus_bg = pygame.image.load("venus_bg.jpg").convert()
comet = pygame.image.load("comet.png").convert_alpha()
comet = pygame.transform.scale(comet, (101.25, 241.5))

text1 = font.render("Solar  Escape",False, "White")
text2 = font1.render("Press  any  key  to  start",False, "White")
game_over = font.render("Game  Over",False, "Red")
font = pygame.font.Font("Pixel_Font.ttf", 75)
font1 = pygame.font.Font("Pixel_Font.ttf", 20)
font2 = pygame.font.Font("Pixel_Font.ttf", 15)
small_font = pygame.font.Font("Pixel_Font.ttf", 12)
date_text=small_font.render("January  17,  2022", False, "White")
average_font = pygame.font.Font("Pixel_Font.ttf", 15)

date_text=small_font.render("January  17,  2022", False, "White")
name_text=average_font.render("By:  Awais  and  Zubair", False, "White")
teacher_text=average_font.render("Instructor:  Ms.  Keras", False, "White")
class_code_text=average_font.render("Class:  ICS207", False, "White")

astronaut_x_mercury = 1024
astronaut_y_mercury = 399
astronaut_x_venus = 640
astronaut_y_venus = 400

asteroid_x = 1280
asteroid_y = 200

fuel_x_venus = random.randint(1,1280)
fuel_y_venus = random.randint(-1500, -1200)

comet1_x= random.randint(1,1280)
comet1_y= -200
comet2_x= random.randint(1,1280)
comet2_y= -500
comet3_x= random.randint(1,1280)
comet3_y=-300
comet4_x= random.randint(1,1280)
comet4_y=-50

key_pressed = False

mouse_pressed = False
mouse_pressed_instruction = False
mouse_pressed_quit = False
mouse_pressed_lesson = False
mouse_pressed_game = False
mouse_pressed_quiz = False
mouse_pressed_result = False
sun_mouse_pressed = False
mercury_mouse_pressed = False
venus_mouse_pressed = False
earth_mouse_pressed = False
mars_mouse_pressed = False
asteroid_belt_pressed = False
jupiter_mouse_pressed = False
saturn_mouse_pressed = False
uranus_mouse_pressed = False
neptune_mouse_pressed = False
back_mouse_Pressed = False
astronaut_collide_mercury =  False
astronaut_collide_venus =  False
comet_collide = False

quiz_counter=int(0)
mouse_wrong=bool(False)
mouse_correct=bool(False)
image_time=30



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

   

    keys = pygame.key.get_pressed()    

          
    screen.blit(galaxy,(0,0))
    screen.blit(text1,(290,150))
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