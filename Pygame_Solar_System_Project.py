# Modules
import pygame
import sys
import random
import time

# Using the main menu function, they can access all parts of the game here,
# and return here via back button, or if they lose in the game.
def main_menu():
    global mouse_pressed_quit  
    global main_venus
    global comet_collide
    global mouse_pressed_lesson 
    global mouse_pressed_instruction 
    global mouse_pressed_game
    global mouse_pressed_quiz
    global mouse_pressed_result
    global main_end
    global a_collide
    global j_collide
    global s_collide
    global lesson_exit
    global instruction_exit
    global quiz_exit
    global result_exit    
    global neptune_main
    global pygame_exit_time

    screen.blit(galaxy,(0,0))

    # Detects if back button was pressed, or player loses game, and returns them to main menu
    if lesson_exit == True:
        mouse_pressed_lesson = False

    if instruction_exit == True:
        mouse_pressed_instruction = False

    if quiz_exit == True:
        mouse_pressed_quiz = False

    if result_exit == True:
        mouse_pressed_result = False    

    if comet_collide == True:
        mouse_pressed_game = False

    if neptune_main == True:
        mouse_pressed_game = False

    if a_collide == True:
        mouse_pressed_game = False

    if j_collide == True:
        mouse_pressed_game = False

    if s_collide == True:
        mouse_pressed_game = False


    # Main menu text
    main_menu_text = font.render("Main Menu ", False, "White")   
    instruction_text = average_font.render("Instructions", False, "Black")
    lesson_text = average_font.render("Lesson", False, "Black") 
    game_text = average_font.render("Game", False, "Black")
    quiz_text = average_font.render("Quiz", False, "Black") 
    result_text = average_font.render("Results", False, "Black") 
    quit_text = average_font.render("Quit", False, "Black") 


    # Creating the main menu buttons    
    mouse_pos = pygame.mouse.get_pos()  

    instruction_button = button(160, 67, 30, 500,"Light Grey")
    if event.type == pygame.MOUSEBUTTONDOWN:
        if instruction_button.collidepoint(mouse_pos):
            mouse_pressed_instruction = True

    lesson_button = button(160, 67, 240, 500,"Light Grey")
    if event.type == pygame.MOUSEBUTTONDOWN:
        if lesson_button.collidepoint(mouse_pos):
            mouse_pressed_lesson = True    
            lesson_exit = False

    game_button = button(160, 67, 450, 500,"Light Grey")
    if event.type == pygame.MOUSEBUTTONDOWN:
        if game_button.collidepoint(mouse_pos):
            mouse_pressed_game = True
            comet_collide = False
            a_collide = False
            j_collide = False
            s_collide = False
            neptune_main = False


    quiz_button = button(160, 67, 660, 500,"Light Grey")
    if event.type == pygame.MOUSEBUTTONDOWN:
        if quiz_button.collidepoint(mouse_pos):
            mouse_pressed_quiz = True
            quiz_exit = False

    result_button = button(160, 67, 870, 500,"Light Grey")
    if event.type == pygame.MOUSEBUTTONDOWN:
        if result_button.collidepoint(mouse_pos):
            mouse_pressed_result = True   
            result_exit = False            

    quit_button = button(160, 67, 1080, 500,"Light Grey")
    if event.type == pygame.MOUSEBUTTONDOWN:
        if quit_button.collidepoint(mouse_pos):
            mouse_pressed_quit = True   

    screen.blit(instruction_text, (45, 520))
    screen.blit(lesson_text, (280, 520))
    screen.blit(game_text, (500, 520))  
    screen.blit(quiz_text, (715, 520))    
    screen.blit(result_text, (915, 520))  
    screen.blit(quit_text, (1135, 520))           
    screen.blit(main_menu_text,(410,300))      

    # Detects if main menu buttons are pressed    
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
        if pygame_exit_time>0:
            screen.blit(citations,(0,0))
            pygame_exit_time-=1
        if pygame_exit_time<=0:
            pygame.quit()
            sys.exit()

# User can click on planets, or asteroid belt for further information
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
    global main_lesson
    global lesson_exit
    global sun_exit
    global mercury_exit 
    global venus_exit 
    global earth_exit 
    global mars_exit  
    global asteroid_belt_exit 
    global jupiter_exit 
    global saturn_exit 
    global uranus_exit 
    global neptune_exit
    global instruction_exit 
    global quiz_exit 
    global result_exit  

    #  Returns them to main lesson menu if any back button is clicked
    if sun_exit == True:
        sun_mouse_pressed = False

    if mercury_exit == True:
        mercury_mouse_pressed = False

    if venus_exit == True:
        venus_mouse_pressed = False

    if earth_exit == True:
        earth_mouse_pressed = False

    if mars_exit == True:
        mars_mouse_pressed = False

    if asteroid_belt_exit == True:
        asteroid_belt_pressed = False

    if jupiter_exit == True:
        jupiter_mouse_pressed = False

    if saturn_exit == True:
        saturn_mouse_pressed = False

    if uranus_exit == True:
        uranus_mouse_pressed = False

    if neptune_exit == True:
        neptune_mouse_pressed = False    

    font2 = pygame.font.Font("Pixel_Font.ttf", 50)
    screen.blit(solar_system_diagram, (0, 0))
    lesson_text = font2.render("Lesson Menu", False, "White")
    screen.blit(lesson_text, (350, 75))
    mouse_pos = pygame.mouse.get_pos()  

    # Creates a clickable surface for the planet images
    sun_surface = screen.blit(sun, (0, 181))
    mercury_surface = screen.blit(mercury, (197, 334))
    venus_surface = screen.blit(venus, (252, 329))
    earth_surface = screen.blit(earth, (331, 323))            
    mars_surface = screen.blit(mars, (440, 328)) 
    jupiter_surface = screen.blit(jupiter, (590, 305))
    saturn_surface = screen.blit(saturn, (693, 319))
    uranus_surface = screen.blit(uranus, (843, 318))
    neptune_surface = screen.blit(neptune, (961, 317))                        

    #Back button
    lesson_back_button = screen.blit(back_button,(0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if lesson_back_button.collidepoint(mouse_pos):
            lesson_exit = True  

    # Detects if planets, and asteroid belt were clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
        if sun_surface.collidepoint(mouse_pos):
            sun_exit = False
            sun_mouse_pressed = True

    if event.type == pygame.MOUSEBUTTONDOWN:
        if mercury_surface.collidepoint(mouse_pos):
            mercury_exit = False
            mercury_mouse_pressed = True 

    if event.type == pygame.MOUSEBUTTONDOWN:
        if venus_surface.collidepoint(mouse_pos):
            venus_exit = False
            venus_mouse_pressed = True

    if event.type == pygame.MOUSEBUTTONDOWN:
        if earth_surface.collidepoint(mouse_pos):
            earth_exit = False
            earth_mouse_pressed = True

    if event.type == pygame.MOUSEBUTTONDOWN:
        if mars_surface.collidepoint(mouse_pos):
            mars_exit = False
            mars_mouse_pressed = True 

    if event.type == pygame.MOUSEBUTTONDOWN:
        if jupiter_surface.collidepoint(mouse_pos):
            jupiter_exit = False
            jupiter_mouse_pressed = True 

    if event.type == pygame.MOUSEBUTTONDOWN:
        if saturn_surface.collidepoint(mouse_pos):
            saturn_exit = False
            saturn_mouse_pressed = True 

    if event.type == pygame.MOUSEBUTTONDOWN:
        if uranus_surface.collidepoint(mouse_pos):
            uranus_exit = False
            uranus_mouse_pressed = True 

    if event.type == pygame.MOUSEBUTTONDOWN:
        if neptune_surface.collidepoint(mouse_pos):
            neptune_exit = False
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


    #Displays information if planets or asteroid belt were clicked
    if sun_mouse_pressed == True:
        screen.blit(galaxy,(0,0))
        stellar_title = font.render("Star evolution & galaxy ",False,"White")
        stellar_title2 = font.render("formation",False,"White")
        stellar_text = average_font.render("Scientists  think  the  big  bang  theory  is  the  explanation  for  how  the  universe  came  to  be.  This  helps  us  understand  how  ",False,"White")
        stellar_text2 = average_font.render("stars  formed.  The  expansion  of  the  universe  was  not  equal  and  nebulae  were  the  result.  Nebulae  are  clouds  of  dust  ",False,"White")
        stellar_text3 = average_font.render("and  gas  particles  in  space,  they  are  the  birthplace  of  stars.  Gravity  overtime  makes  the  nebula  start  to  condense,  ",False,"White")
        stellar_text4 = average_font.render("eventually  the  particles  move  and  start  spinning  around  an  axis  faster  and  faster.  Continued  gravitational  ",False,"White")
        stellar_text5 = average_font.render("force  and  rotation  make  the  nebula  shrink  and  the  centre  starts  to  get  hot.  At  10  million  celsius,  nuclear  ",False,"White")
        stellar_text6 = average_font.render("fusion  begins  and  a  star  is  born.  Nuclear  fusion  consumes  hydrogen  to  form  helium.  Depending  on  the  mass  ",False,"White")
        stellar_text7 = average_font.render("of  the  nebula  an  average  star  or  massive  star  will  be  formed.  If  the  mass  of  the  nebula  is  high  then  a  ",False,"White")
        stellar_text8 = average_font.render("massive  star  will  be  formed  and  if  the  mass  of  the  nebula  is  low  then  an  average  star  will  be  formed.  These  ",False,"White")
        stellar_text9 = average_font.render("two  stars  lead  different  life  cycles.  For  an  average  star  it  takes  long  for  it  to  finish  its  fuel,  once  ",False,"White")
        stellar_text10 = average_font.render("all  nuclear  fuel  is  used  the  core  shrinks  and  the  outer  layers  expand.  The  temperature  starts  rising  and  once  ",False,"White")
        stellar_text11 = average_font.render("100  million  celsius  is  reached  helium  fuses  into  carbon  and  a  Red  Giant  is  formed.  Once  a  Red  Giant  is  ",False,"White")
        stellar_text12 = average_font.render("done  using  its  fuel,  its  core  contracts  and  stellar  winds  remove  outer  gases  forming  a  planetary  nebula.  ",False,"White")
        stellar_text13 = average_font.render("Eventually  the  leftover  core  cools  and  shrinks.  No  nuclear  reactions  take  place,  this  new  star  is  called ",False,"White")
        stellar_text14 = average_font.render("a  white  dwarf.  This  is the  life  cycle  for  an  average star.  For  a  massive  star  it  takes  way  less  time  for  ",False,"White")
        stellar_text15 = average_font.render("it  to  finish  its  fuel,  once  all  nuclear  fuel  is  used  the  core  shrinks  and  the  outer  layers  expand.  Since  ",False,"White")
        stellar_text16 = average_font.render("a  massive  star’s  core  is  hotter  it  can  fuse  helium  into  heavier  elements.  This  results  in  a  bigger  expansion  ",False,"White")
        stellar_text17 = average_font.render("and  a  Supergiant  is  formed.  Once  a  Supergiant  is  done  using  its  fuel  the  core  collapses  and  a  ",False,"White")
        stellar_text18 = average_font.render("supernova  occurs  which  is  a  huge  explosion.  If  the  core  of  the  Supergiant  is  less  than  3  solar  mass  ",False,"White")
        stellar_text19 = average_font.render("(1  solar  mass  is  the  mass  of  our  sun)  a  neutron  star  will  be  formed,  else  the  core  will  collapse  into  a  ",False,"White")
        stellar_text20 = average_font.render("black  hole.  This  is  the  life  cycle  for  a  massive  star.  Scientists  believe  the  solar  nebula  theory  explains  ",False,"White")
        stellar_text21 = average_font.render("how  solar  systems  are  formed.  This  theory  states  that  planets  form  after  the  formation  of  a  star.  So  in  our  ",False,"White")
        stellar_text22 = average_font.render("solar  system  that  would  mean  the  Sun  formed  before  any  of  the  planets.  This  relates  back  to  the  formation  of  ",False,"White")
        stellar_text23 = average_font.render("a  star,  after  a  new  star  is  formed  from  a  nebula  there  is  leftover  material  which  starts  to  orbit  the  newly  ",False,"White")
        stellar_text24 = average_font.render("formed  star.  The  material  distribution  is  uneven  and  overtime  material  will  accumulate  due  to  gravity.  Eventually  a  ",False,"White")
        stellar_text25 = average_font.render("planet  is  formed  and  this  newly  formed  planet  will  orbit  the  star.  Newly  formed  solar  systems  are  disorganized  and  ",False,"White")
        stellar_text26 = average_font.render("many  collisions  can  occur.",False,"White")

        screen.blit(stellar_title,(20,0))
        screen.blit(stellar_title2,(20,70))
        screen.blit(stellar_text,(0,190))
        screen.blit(stellar_text2,(0,205))
        screen.blit(stellar_text3,(0,220))
        screen.blit(stellar_text4,(0,235))  
        screen.blit(stellar_text5,(0,250))  
        screen.blit(stellar_text6,(0,265))  
        screen.blit(stellar_text7,(0,280))  
        screen.blit(stellar_text8,(0,295))  
        screen.blit(stellar_text9,(0,310))  
        screen.blit(stellar_text10,(0,325))  
        screen.blit(stellar_text11,(0,340))  
        screen.blit(stellar_text12,(0,355))
        screen.blit(stellar_text13,(0,370))
        screen.blit(stellar_text13,(0,385))
        screen.blit(stellar_text14,(0,400))
        screen.blit(stellar_text15,(0,415))
        screen.blit(stellar_text16,(0,430))
        screen.blit(stellar_text17,(0,445))
        screen.blit(stellar_text18,(0,460))
        screen.blit(stellar_text19,(0,475))
        screen.blit(stellar_text20,(0,490))
        screen.blit(stellar_text21,(0,505))     
        screen.blit(stellar_text22,(0,520))                
        screen.blit(stellar_text23,(0,535))                
        screen.blit(stellar_text24,(0,550))                
        screen.blit(stellar_text25,(0,565))                
        screen.blit(stellar_text26,(0,580)) 

        sun_back_button = screen.blit(back_button,(1200,580))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if sun_back_button.collidepoint(mouse_pos):
                sun_exit = True

    if mercury_mouse_pressed == True:
        screen.blit(galaxy,(0,0))
        mercury_title = font.render("Mercury",False,"White")
        mercury_text = font1.render("Mercury  is  the  closest  planet  to  the  sun  and  the  smallest  planet  in  our  solar  system.  ",False,"White")
        mercury_text2 = font1.render("Mercury  has  no  moons  and  no  atmosphere.  Due  to  having  no  atmosphere  it  is  ",False,"White")
        mercury_text3 = font1.render("very  hot  in  the  day  and  very  cold  in  the  night.",False,"White")
        screen.blit(mercury_title,(380,0))
        screen.blit(mercury_text,(20,120))
        screen.blit(mercury_text2,(20,150))
        screen.blit(mercury_text3,(20,180))

        mercury_back_button = screen.blit(back_button,(1200,580))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mercury_back_button.collidepoint(mouse_pos):
                mercury_exit = True

    if venus_mouse_pressed == True:
        screen.blit(galaxy,(0,0))
        venus_title = font.render("Venus",False,"White")
        venus_text = font1.render("Venus  is  the  brightest  object  in  the  night  sky  because  it  is  very  close  to  the  sun  ",False,"White")
        venus_text2 = font1.render("and  has  an  atmosphere  which  reflects  sunlight.  Venus  is  the  hottest  planet  in  our  ",False,"White")
        venus_text3 = font1.render("solar  system  since  it’s  atmosphere  has  co2  which  contributes  to  the  greenhouse  ",False,"White")
        venus_text4 = font1.render("effect.  ",False,"White")
        screen.blit(venus_title,(460,0))
        screen.blit(venus_text,(20,120))
        screen.blit(venus_text2,(20,150))
        screen.blit(venus_text3,(20,180))
        screen.blit(venus_text4,(20,210))

        venus_back_button = screen.blit(back_button,(1200,580))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if venus_back_button.collidepoint(mouse_pos):
                venus_exit = True

    if earth_mouse_pressed == True:
        screen.blit(galaxy,(0,0))
        earth_title = font.render("Earth",False,"White")
        earth_text = font1.render("The  only  known  planet  to  have  life  in  the  solar  system.  The  atmosphere  of  Earth  is  ",False,"White")
        earth_text2 = font1.render("made  out  of  nitrogen,  oxygen,  and  water  vapour.  The  atmosphere  regulates  ",False,"White")
        earth_text3 = font1.render("temperature  and  70 percent  of  the  Earth  is  covered  in  water.",False,"White")
        screen.blit(earth_title,(460,0))
        screen.blit(earth_text,(20,120))
        screen.blit(earth_text2,(20,150))
        screen.blit(earth_text3,(20,180))

        earth_back_button = screen.blit(back_button,(1200,580))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if earth_back_button.collidepoint(mouse_pos):
                earth_exit = True

    if mars_mouse_pressed == True:
        screen.blit(galaxy,(0,0))
        mars_title = font.render("Mars",False,"White")
        mars_text = font1.render("Mars  is  red  due  to  iron  oxide  (rust)  on  its  surface.  There  have  been  many  ",False,"White")
        mars_text2 = font1.render("rovers  sent  to  Mars  and  information  suggests  that  ancient  Mars  might  have  ",False,"White")
        mars_text3 = font1.render("been  able  to  sustain  life.",False,"White")
        screen.blit(mars_title,(500,0))
        screen.blit(mars_text,(40,120))
        screen.blit(mars_text2,(40,150))
        screen.blit(mars_text3,(40,180))

        mars_back_button = screen.blit(back_button,(1200,580))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mars_back_button.collidepoint(mouse_pos):
                mars_exit = True

    if asteroid_belt_pressed == True:
        asteroid_belt_exit = False
        screen.blit(galaxy,(0,0))
        asteroid_title = font.render("The  Asteroid  Belt",False,"White")
        asteroid_text = font1.render("The  asteroid  belt  is  located  in  between  Mars  and  Jupiter.  An  asteroid  is  a  ",False,"White")
        asteroid_text2 = font1.render("small  rocky  object,  it  ranges  from  5  -  900 km  in  width.  Most  of  the  asteroids  ",False,"White")
        asteroid_text3 = font1.render("in  our  solar  system  originate  from  the  asteroid  belt.  The  Kuiper  Belt  also  ",False,"White")
        asteroid_text4 = font1.render("known  as  the  second  asteroid  belt  consists  of  millions  of  small  objects  orbiting  ",False,"White")
        asteroid_text5 = font1.render("the  sun.  These  objects  are  usually  comets  and  asteroids.  These  objects  are  most  ",False,"White")
        asteroid_text6 = font1.render("likely  left  over  from  the  formation  of  the  solar  system.  Comets  are  composed  of  ",False,"White")
        asteroid_text7 = font1.render("rocky  material,  ice,  and  gas.  The  last  material  in  the  sun’s  gravitational  pull  ",False,"White")
        asteroid_text8 = font1.render("is  the  Oort  Cloud.  It  is  a  spherical  cloud  of  small  icy  fragments  of  debris.  ",False,"White")
        asteroid_text9 = font1.render("It  is  way  further  than  the  Kuiper  Belt,  it  is  approximately  50 000  -  100 000 AU  ",False,"White")
        asteroid_text10 = font1.render("from  the  sun.  1 AU  stands  for  the  distance  from  the  Earth  to  the  sun.  Comets  ",False,"White")
        asteroid_text11 = font1.render("come  from  the  Kuiper  Belt  and  Oort  Cloud.",False,"White")
        screen.blit(asteroid_title,(140,0))
        screen.blit(asteroid_text,(50,120))
        screen.blit(asteroid_text2,(50,150))
        screen.blit(asteroid_text3,(50,180))
        screen.blit(asteroid_text4,(50,210))  
        screen.blit(asteroid_text5,(50,240))  
        screen.blit(asteroid_text6,(50,270))  
        screen.blit(asteroid_text7,(50,300))  
        screen.blit(asteroid_text8,(50,330))  
        screen.blit(asteroid_text9,(50,360))  
        screen.blit(asteroid_text10,(50,390))  
        screen.blit(asteroid_text11,(50,420))

        asteroid_belt_back_button = screen.blit(back_button,(1200,580))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if asteroid_belt_back_button.collidepoint(mouse_pos):
                asteroid_belt_exit = True  

    if jupiter_mouse_pressed == True:
        screen.blit(galaxy,(0,0))
        jupiter_title = font.render("Jupiter",False,"White")
        jupiter_text = font1.render("Largest  planet  in  the  solar  system  and  has  the  greatest  mass  compared  to  all  ",False,"White")
        jupiter_text2 = font1.render("planets  in  the  solar  system.  Jupiter  has  coloured  bands  and  something  called  ",False,"White")
        jupiter_text3 = font1.render("the  Great  Red  Spot.  It  is  a  hurricane  with  very  high  wind  speeds.  Jupiter  ",False,"White")
        jupiter_text4 = font1.render("has  many  moons,  but  the  4  largest  are:  Europa,  Io,  Ganymede,  and  Callisto.",False,"White")
        screen.blit(jupiter_title,(450,0))
        screen.blit(jupiter_text,(40,120))
        screen.blit(jupiter_text2,(40,150))
        screen.blit(jupiter_text3,(40,180))
        screen.blit(jupiter_text4,(40,210))   

        jupiter_back_button = screen.blit(back_button,(1200,580))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if jupiter_back_button.collidepoint(mouse_pos):
                jupiter_exit = True  

    if saturn_mouse_pressed == True:
        screen.blit(galaxy,(0,0))
        saturn_title = font.render("Saturn",False,"White")
        saturn_text = font1.render("Saturn is  the  second  largest  planet  in  the  solar  system,  but  the  least  dense  of  ",False,"White")
        saturn_text2 = font1.render("all  the  planets  in  our  solar  system.  Saturn  has  a  quick  rotation  and  high  wind  ",False,"White")
        saturn_text3 = font1.render("speeds.  There  are  over  1000  rings  surrounding  Saturn.  They  may  have  been  formed  ",False,"White")
        saturn_text4 = font1.render("from  many  moons  or  other  objects  which  came  close  to  the  planet.  Saturn  has  the  ",False,"White")
        saturn_text5 = font1.render("most  known  moons  in  the  solar  system  and  has  the  2nd  largest  known  moon  in  the  ",False,"White")
        saturn_text6 = font1.render("solar  system  which  is  named  Titan.",False,"White")
        screen.blit(saturn_title,(430,0))
        screen.blit(saturn_text,(25,120))
        screen.blit(saturn_text2,(25,150))
        screen.blit(saturn_text3,(25,180))
        screen.blit(saturn_text4,(25,210))  
        screen.blit(saturn_text5,(25,240))
        screen.blit(saturn_text6,(25,270))

        saturn_back_button = screen.blit(back_button,(1200,580))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if saturn_back_button.collidepoint(mouse_pos):
                saturn_exit = True  

    if uranus_mouse_pressed == True:
        screen.blit(galaxy,(0,0))
        uranus_title = font.render("Uranus",False,"White")
        uranus_text = font1.render("Uranus  is  a  unique  planet  because  it  rotates  on  its  sides.  Uranus  has  rings  just  ",False,"White")
        uranus_text2 = font1.render("like  Saturn.  Its  atmosphere  is  made  mostly  of  hydrogen,  helium,  and  methane.  ",False,"White")
        screen.blit(uranus_title,(430,0))
        screen.blit(uranus_text,(25,120))
        screen.blit(uranus_text2,(25,150))

        uranus_back_button = screen.blit(back_button,(1200,580))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if uranus_back_button.collidepoint(mouse_pos):
                uranus_exit = True  

    if neptune_mouse_pressed == True:
        screen.blit(galaxy,(0,0))
        neptune_title = font.render("Neptune",False,"White")
        neptune_text = font1.render("Neptune  is  the  coldest  planet  in  our  solar  system,  Neptune  is  blue  and  has  ",False,"White")
        neptune_text2 = font1.render("white  clouds.  The Great  Dark  Spot  is  another  feature  of  Neptune  and  is  actually  ",False,"White")
        neptune_text3 = font1.render("the  centre  of  a  storm.  Neptune  just  like  Uranus  and  Saturn  has  rings,  but  they  ",False,"White")
        neptune_text4 = font1.render("are  very  thin.  Neptune  contains  lots  of  ice  and  icy  material",False,"White")
        screen.blit(neptune_title,(400,0))
        screen.blit(neptune_text,(25,120))
        screen.blit(neptune_text2,(25,150))
        screen.blit(neptune_text3,(25,180))
        screen.blit(neptune_text4,(25,210))  

        neptune_back_button = screen.blit(back_button,(1200,580))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if neptune_back_button.collidepoint(mouse_pos):
                neptune_exit = True  

# First level of the game, player has to collect fuel to procceed
def mercury_level():
    global main_venus    
    global astronaut_x_mercury
    global astronaut_y_mercury
    global astronaut_collide_mercury

    screen.blit(mercury_background,(0,0))        
    screen.blit(fuel,(100,430))

    astronaut_left_1 = False
    astronaut_right_1 = False

    keys = pygame.key.get_pressed() 
    if not event.type == pygame.KEYDOWN:
        screen.blit(astronaut_left,(astronaut_x_mercury,astronaut_y_mercury))

    if event.type == pygame.KEYDOWN and not keys[pygame.K_RIGHT]:
        screen.blit(astronaut_left,(astronaut_x_mercury,astronaut_y_mercury))

    if keys[pygame.K_LEFT]:
        astronaut_x_mercury-=5
        astronaut_right_1 = False        
        astronaut_left_1 = True

    if keys[pygame.K_RIGHT]:
        astronaut_x_mercury+=5
        astronaut_left_1 = False        
        astronaut_right_1 = True

    if astronaut_left_1 == True:
        astronaut_right_1 = False                
        screen.blit(astronaut_left,(astronaut_x_mercury,astronaut_y_mercury))

    if astronaut_right_1 == True:
        astronaut_left_1 = False     
        screen.blit(astronaut_right,(astronaut_x_mercury,astronaut_y_mercury))


    if astronaut_x_mercury > 1404:
        astronaut_x_mercury = -90 

    if astronaut_x_mercury < -90:
        astronaut_x_mercury = 1404 

    astronaut_button = invisible_button(80, 124, astronaut_x_mercury, astronaut_y_mercury)
    fuel_button1 = invisible_button(25, 91, 100 , 430)
    if (pygame.Rect.colliderect(astronaut_button, fuel_button1)):
        astronaut_collide_mercury = True 

    if astronaut_collide_mercury == True:
        venus_level()

# Second level of the game, player has to collect fuel, and avoid comets to procceed
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
    global main_venus

    screen.blit(venus_bg,(0,0))
    screen.blit(fuel,(fuel_x_venus, fuel_y_venus))

    astronaut_left_1 = False
    astronaut_right_1 = False

    keys = pygame.key.get_pressed() 
    if not event.type == pygame.KEYDOWN:
        screen.blit(astronaut_left,(astronaut_x_venus,astronaut_y_venus))

    if event.type == pygame.KEYDOWN and not keys[pygame.K_RIGHT]:
        screen.blit(astronaut_left,(astronaut_x_venus,astronaut_y_venus))

    if keys[pygame.K_LEFT]:
        astronaut_x_venus-=5
        astronaut_right_1 = False        
        astronaut_left_1 = True

    if keys[pygame.K_RIGHT]:
        astronaut_x_venus+=5
        astronaut_left_1 = False        
        astronaut_right_1 = True

    if astronaut_left_1 == True:
        astronaut_right_1 = False                
        screen.blit(astronaut_left,(astronaut_x_venus,astronaut_y_venus))

    if astronaut_right_1 == True:
        astronaut_left_1 = False     
        screen.blit(astronaut_right,(astronaut_x_venus,astronaut_y_venus))


    if astronaut_x_venus > 1404:
        astronaut_x_venus = -90 

    if astronaut_x_venus < -90:
        astronaut_x_venus = 1404 

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
        earth_level()
        fuel_x_venus = 1000
        fuel_y_venus = 1000
        comet1_x = 1000
        comet1_y = 1000
        comet2_x = 1000
        comet2_y = 1000
        comet3_x = 1000
        comet3_y = 1000
        comet4_x = 1000
        comet4_y = 1000   

    if comet_collide == True:
        comet1_y = 1000
        comet2_y = 1000
        comet3_y = 1000
        comet4_y = 1000           

    mouse_pos = pygame.mouse.get_pos()  

# Third level of the game, player has to collect fuel to procceed
def earth_level():
    global main_earth  
    global astronaut_x_earth
    global astronaut_y_earth
    global astronaut_collide_earth

    screen.blit(earth_bg,(0,0))        
    screen.blit(fuel,(100,440))

    astronaut_left_1 = False
    astronaut_right_1 = False

    keys = pygame.key.get_pressed() 
    if not event.type == pygame.KEYDOWN:
        screen.blit(astronaut_left,(astronaut_x_earth,astronaut_y_earth))

    if event.type == pygame.KEYDOWN and not keys[pygame.K_RIGHT]:
        screen.blit(astronaut_left,(astronaut_x_earth,astronaut_y_earth))

    if keys[pygame.K_LEFT]:
        astronaut_x_earth-=5
        astronaut_right_1 = False        
        astronaut_left_1 = True

    if keys[pygame.K_RIGHT]:
        astronaut_x_earth+=5
        astronaut_left_1 = False        
        astronaut_right_1 = True

    if astronaut_left_1 == True:
        astronaut_right_1 = False                
        screen.blit(astronaut_left,(astronaut_x_earth,astronaut_y_earth))

    if astronaut_right_1 == True:
        astronaut_left_1 = False     
        screen.blit(astronaut_right,(astronaut_x_earth,astronaut_y_earth))


    if astronaut_x_earth > 1404:
        astronaut_x_earth = -90 

    if astronaut_x_earth < -90:
        astronaut_x_earth = 1404 

    astronaut_button = invisible_button(80, 124, astronaut_x_earth, astronaut_y_earth)
    fuel_button1 = invisible_button(25, 91, 100 , 430)
    if (pygame.Rect.colliderect(astronaut_button, fuel_button1)):
        astronaut_collide_earth = True 

    if astronaut_collide_earth == True:
        mars_level()

# Fourth level of the game, player has to collect fuel to procceed
def mars_level():
    global main_mars  
    global astronaut_x_mars
    global astronaut_y_mars
    global astronaut_collide_mars

    screen.blit(mars_bg,(0,0))        
    screen.blit(fuel,(100,413))

    astronaut_left_1 = False
    astronaut_right_1 = False

    keys = pygame.key.get_pressed() 
    if not event.type == pygame.KEYDOWN:
        screen.blit(astronaut_left,(astronaut_x_mars,astronaut_y_mars))

    if event.type == pygame.KEYDOWN and not keys[pygame.K_RIGHT]:
        screen.blit(astronaut_left,(astronaut_x_mars,astronaut_y_mars))

    if keys[pygame.K_LEFT]:
        astronaut_x_mars-=5
        astronaut_right_1 = False        
        astronaut_left_1 = True

    if keys[pygame.K_RIGHT]:
        astronaut_x_mars+=5
        astronaut_left_1 = False        
        astronaut_right_1 = True

    if astronaut_left_1 == True:
        astronaut_right_1 = False                
        screen.blit(astronaut_left,(astronaut_x_mars,astronaut_y_mars))

    if astronaut_right_1 == True:
        astronaut_left_1 = False     
        screen.blit(astronaut_right,(astronaut_x_mars,astronaut_y_mars))


    if astronaut_x_mars > 1404:
        astronaut_x_mars = -90 

    if astronaut_x_mars < -90:
        astronaut_x_mars = 1404 

    astronaut_button = invisible_button(80, 124, astronaut_x_mars, astronaut_y_mars)
    fuel_button1 = invisible_button(25, 91, 100 , 430)
    if (pygame.Rect.colliderect(astronaut_button, fuel_button1)):
        astronaut_collide_mars = True 

    if astronaut_collide_mars == True:
        asteroid_belt_level()

# Creates moving background
def galaxy_background():
    screen.blit(galaxy,(galaxy_x_pos, 0))
    screen.blit(galaxy,(galaxy_x_pos + 1280, 0))

# Fifth level of the game, player has to collect fuel, and avoid asteroid to procceed
def asteroid_belt_level():
    global asteroid_x1
    global asteroid_y1
    global asteroid_x2
    global asteroid_y2    
    global asteroid_x3
    global asteroid_y3
    global asteroid_x4
    global asteroid_y4   
    global fuel_x_a
    global fuel_y_a
    global astro_x_a
    global astro_y_a
    global galaxy_x_pos
    global a_collide
    global astronaut_collide_a

    screen.fill("Black")
    galaxy_x_pos -= 2
    galaxy_background()
    if galaxy_x_pos <= -1280:
        galaxy_x_pos = 0    
    screen.blit(astro_fuel,(astro_x_a, astro_y_a))
    keys = pygame.key.get_pressed()    
    if keys[pygame.K_UP]:
        astro_y_a -=5
    if keys[pygame.K_DOWN]:
        astro_y_a+=5

    if astro_y_a > 820:
        astro_y_a = -80 

    if astro_y_a < -80:
        astro_y_a = 820 

    astronaut_button = invisible_button(80, 124, astro_x_a, astro_y_a)
    fuel_button = invisible_button(25, 91, fuel_x_a , fuel_y_a)
    asteroid_1_button = invisible_button(110, 95, asteroid_x1 , asteroid_y1) 
    asteroid_2_button  = invisible_button(110, 95, asteroid_x2 , asteroid_y2) 
    asteroid_3_button  = invisible_button(110, 95, asteroid_x3 , asteroid_y3) 
    asteroid_4_button  = invisible_button(110, 95, asteroid_x4 , asteroid_y4) 


    if (pygame.Rect.colliderect(astronaut_button, fuel_button)):
        astronaut_collide_a = True 
    if (pygame.Rect.colliderect(astronaut_button, asteroid_1_button)):
        a_collide = True 
    if (pygame.Rect.colliderect(astronaut_button, asteroid_2_button)):
        a_collide = True 
    if (pygame.Rect.colliderect(astronaut_button, asteroid_3_button)):
        a_collide = True 
    if (pygame.Rect.colliderect(astronaut_button, asteroid_4_button)):
        a_collide = True 

    fuel_x_a-= 7
    if fuel_x_a<-112.5:
        fuel_y_a = random.randint(1, 720)    
    if fuel_x_a<-112.5:
        fuel_x_a = random.randint(2000, 2100)    

    screen.blit(asteroid,(asteroid_x1,asteroid_y1))
    screen.blit(asteroid,(asteroid_x2,asteroid_y2))
    screen.blit(asteroid,(asteroid_x3,asteroid_y3))
    screen.blit(asteroid,(asteroid_x4,asteroid_y4))
    screen.blit(fuel, (fuel_x_a,fuel_y_a))

    asteroid_x1-= 7    
    if asteroid_x1<-112.5:
        asteroid_y1 = random.randint(1, 720)   
        asteroid_x1 = random.randint(1400, 1600)
    if asteroid_x1<-112.5:
        asteroid_x1 = 1280

    asteroid_x2-= 11
    if asteroid_x2<-112.5:
        asteroid_y2 = random.randint(1, 720)
        asteroid_x2 = random.randint(1400, 1600)
    if asteroid_x2<-112.5:
        asteroid_x2 = 1280   

    asteroid_x3-= 7
    if asteroid_x3==-112.5:
        asteroid_y3 = random.randint(1, 720)
        asteroid_x3 = random.randint(1400, 1600)
    if asteroid_x3==-112.5:
        asteroid_x3 = 1280  

    asteroid_x4-= 7
    if asteroid_x4==-112.5:
        asteroid_y4 = random.randint(1, 720)
        asteroid_x4 = random.randint(1400, 1600)
    if asteroid_x4==-112.5:    
        asteroid_x4 = 1280    

    if astronaut_collide_a == True:
        asteroid_x1 = 1500
        asteroid_y1 = 1500
        asteroid_x2 = 1500
        asteroid_y2 = 1500   
        asteroid_x3 = 1500
        asteroid_y3 = 1500
        asteroid_x4 = 1500
        asteroid_y4 = 1500    
        jupiter_level()

    if a_collide == True:
        asteroid_x1 = 1
        asteroid_x2 = 1
        asteroid_x3 = 1
        asteroid_x4 = 1

# Sixth level of the game, player has to collect fuel, and avoid asteroid to procceed
def jupiter_level():
    global jupiter_x1
    global jupiter_y1
    global jupiter_x2
    global jupiter_y2    
    global jupiter_x3
    global jupiter_y3
    global jupiter_x4
    global jupiter_y4   
    global fuel_x_j
    global fuel_y_j
    global astro_x_j
    global astro_y_j
    global j_collide
    global astronaut_collide_j

    screen.fill("Black")
    screen.blit(jupiter_bg,(0,0))
    screen.blit(astro_fuel,(astro_x_j, astro_y_j))
    keys = pygame.key.get_pressed()    
    if keys[pygame.K_UP]:
        astro_y_j -=5
    if keys[pygame.K_DOWN]:
        astro_y_j+=5

    if astro_y_j > 820:
        astro_y_j = -80 

    if astro_y_j < -80:
        astro_y_j = 820

    astronaut_button = invisible_button(80, 124, astro_x_j, astro_y_j)
    fuel_button = invisible_button(25, 91, fuel_x_j , fuel_y_j)
    jupiter_1_button = invisible_button(110, 95, jupiter_x1 , jupiter_y1) 
    jupiter_2_button  = invisible_button(110, 95, jupiter_x2 , jupiter_y2) 
    jupiter_3_button  = invisible_button(110, 95, jupiter_x3 , jupiter_y3) 
    jupiter_4_button  = invisible_button(110, 95, jupiter_x4 , jupiter_y4) 


    if (pygame.Rect.colliderect(astronaut_button, fuel_button)):
        astronaut_collide_j = True 
    if (pygame.Rect.colliderect(astronaut_button, jupiter_1_button)):
        j_collide = True 
    if (pygame.Rect.colliderect(astronaut_button, jupiter_2_button)):
        j_collide = True 
    if (pygame.Rect.colliderect(astronaut_button, jupiter_3_button)):
        j_collide = True 
    if (pygame.Rect.colliderect(astronaut_button, jupiter_4_button)):
        j_collide = True 

    fuel_x_j-= 7
    if fuel_x_j<-112.5:
        fuel_y_j = random.randint(1, 720)    
    if fuel_x_j<-112.5:
        fuel_x_j = random.randint(2000, 2100)    

    screen.blit(asteroid,(jupiter_x1,jupiter_y1))
    screen.blit(asteroid,(jupiter_x2,jupiter_y2))
    screen.blit(asteroid,(jupiter_x3,jupiter_y3))
    screen.blit(asteroid,(jupiter_x4,jupiter_y4))
    screen.blit(fuel, (fuel_x_j,fuel_y_j))

    jupiter_x1-= 7    
    if jupiter_x1<-112.5:
        jupiter_y1 = random.randint(1, 720)   
        jupiter_x1 = random.randint(1400, 1600)
    if jupiter_x1<-112.5:
        jupiter_x1 = 1280

    jupiter_x2-= 11
    if jupiter_x2<-112.5:
        jupiter_y2 = random.randint(1, 720)
        jupiter_x2 = random.randint(1400, 1600)
    if jupiter_x2<-112.5:
        jupiter_x2 = 1280   

    jupiter_x3-= 7
    if jupiter_x3==-112.5:
        jupiter_y3 = random.randint(1, 720)
        jupiter_x3 = random.randint(1400, 1600)
    if jupiter_x3==-112.5:
        jupiter_x3 = 1280  

    jupiter_x4-= 7
    if jupiter_x4==-112.5:
        jupiter_y4 = random.randint(1, 720)
        jupiter_x4 = random.randint(1400, 1600)
    if jupiter_x4==-112.5:    
        jupiter_x4 = 1280    

    if astronaut_collide_j == True:
        jupiter_x1 = 1500
        jupiter_y1 = 1500
        jupiter_x2 = 1500
        jupiter_y2 = 1500   
        jupiter_x3 = 1500
        jupiter_y3 = 1500
        jupiter_x4 = 1500
        jupiter_y4 = 1500
        saturn_level()

    if j_collide == True:
        jupiter_x1 = 1
        jupiter_x2 = 1
        jupiter_x3 = 1
        jupiter_x4 = 1

# Seventh level of the game, player has to collect fuel, and avoid asteroid to procceed
def saturn_level():
    global saturn_x1
    global saturn_y1
    global saturn_x2
    global saturn_y2    
    global saturn_x3
    global saturn_y3
    global saturn_x4
    global saturn_y4   
    global fuel_x_s
    global fuel_y_s
    global astro_x_s
    global astro_y_s
    global s_collide
    global astronaut_collide_s

    screen.fill("Black")
    screen.blit(saturn_bg,(0,0))
    screen.blit(astro_fuel,(astro_x_s, astro_y_s))
    keys = pygame.key.get_pressed()    
    if keys[pygame.K_UP]:
        astro_y_s -=5
    if keys[pygame.K_DOWN]:
        astro_y_s+=5

    if astro_y_s > 820:
        astro_y_s = -80 

    if astro_y_s < -80:
        astro_y_s = 820

    astronaut_button = invisible_button(80, 124, astro_x_s, astro_y_s)
    fuel_button = invisible_button(25, 91, fuel_x_s , fuel_y_s)
    saturn_1_button = invisible_button(110, 95, saturn_x1 , saturn_y1) 
    saturn_2_button  = invisible_button(110, 95, saturn_x2 , saturn_y2) 
    saturn_3_button  = invisible_button(110, 95, saturn_x3 , saturn_y3) 
    saturn_4_button  = invisible_button(110, 95, saturn_x4 , saturn_y4) 


    if (pygame.Rect.colliderect(astronaut_button, fuel_button)):
        astronaut_collide_s = True 
    if (pygame.Rect.colliderect(astronaut_button, saturn_1_button)):
        s_collide = True 
    if (pygame.Rect.colliderect(astronaut_button, saturn_2_button)):
        s_collide = True 
    if (pygame.Rect.colliderect(astronaut_button, saturn_3_button)):
        s_collide = True 
    if (pygame.Rect.colliderect(astronaut_button, saturn_4_button)):
        s_collide = True 

    fuel_x_s-= 7
    if fuel_x_s<-112.5:
        fuel_y_s = random.randint(1, 720)    
    if fuel_x_s<-112.5:
        fuel_x_s = random.randint(2000, 2100)    

    screen.blit(asteroid,(saturn_x1,saturn_y1))
    screen.blit(asteroid,(saturn_x2,saturn_y2))
    screen.blit(asteroid,(saturn_x3,saturn_y3))
    screen.blit(asteroid,(saturn_x4,saturn_y4))
    screen.blit(fuel, (fuel_x_s,fuel_y_s))

    saturn_x1-= 7    
    if saturn_x1<-112.5:
        saturn_y1 = random.randint(1, 720)   
        saturn_x1 = random.randint(1400, 1600)
    if saturn_x1<-112.5:
        saturn_x1 = 1280

    saturn_x2-= 11
    if saturn_x2<-112.5:
        saturn_y2 = random.randint(1, 720)
        saturn_x2 = random.randint(1400, 1600)
    if saturn_x2<-112.5:
        saturn_x2 = 1280   

    saturn_x3-= 7
    if saturn_x3==-112.5:
        saturn_y3 = random.randint(1, 720)
        saturn_x3 = random.randint(1400, 1600)
    if saturn_x3==-112.5:
        saturn_x3 = 1280  

    saturn_x4-= 7
    if saturn_x4==-112.5:
        saturn_y4 = random.randint(1, 720)
        saturn_x4 = random.randint(1400, 1600)
    if saturn_x4==-112.5:    
        saturn_x4 = 1280    

    if astronaut_collide_s == True:
        saturn_x1 = 1500
        saturn_y1 = 1500
        saturn_x2 = 1500
        saturn_y2 = 1500   
        saturn_x3 = 1500
        saturn_y3 = 1500
        saturn_x4 = 1500
        saturn_y4 = 1500 
        neptune_level()

    if s_collide == True:
        saturn_x1 = 1
        saturn_x2 = 1
        saturn_x3 = 1
        saturn_x4 = 1

# Eighth level of the game, player has to collect fuel to finish game, adn return back to main menu
def neptune_level():
    global main_neptune  
    global astronaut_x_neptune
    global astronaut_y_neptune
    global astronaut_collide_neptune
    global neptune_main

    screen.blit(neptune_bg,(0,0))        
    screen.blit(fuel,(100,430))

    astronaut_left_1 = False
    astronaut_right_1 = False

    keys = pygame.key.get_pressed() 
    if not event.type == pygame.KEYDOWN:
        screen.blit(astronaut_left,(astronaut_x_neptune,astronaut_y_neptune))

    if event.type == pygame.KEYDOWN and not keys[pygame.K_RIGHT]:
        screen.blit(astronaut_left,(astronaut_x_neptune,astronaut_y_neptune))

    if keys[pygame.K_LEFT]:
        astronaut_x_neptune-=5
        astronaut_right_1 = False        
        astronaut_left_1 = True

    if keys[pygame.K_RIGHT]:
        astronaut_x_neptune+=5
        astronaut_left_1 = False        
        astronaut_right_1 = True

    if astronaut_left_1 == True:
        astronaut_right_1 = False                
        screen.blit(astronaut_left,(astronaut_x_neptune,astronaut_y_neptune))

    if astronaut_right_1 == True:
        astronaut_left_1 = False     
        screen.blit(astronaut_right,(astronaut_x_neptune,astronaut_y_neptune))


    if astronaut_x_neptune > 1404:
        astronaut_x_neptune = -90 

    if astronaut_x_neptune < -90:
        astronaut_x_neptune = 1404 

    astronaut_button = invisible_button(80, 124, astronaut_x_neptune, astronaut_y_neptune)
    fuel_button1 = invisible_button(25, 91, 100 , 430)
    if (pygame.Rect.colliderect(astronaut_button, fuel_button1)):
        astronaut_collide_neptune = True 

    mouse_pos = pygame.mouse.get_pos()      
    if astronaut_collide_neptune == True:
        screen.blit(galaxy,(0,0))
        screen.blit(game_over,(400, 200))
        neptune_button = button(200, 100, 500, 400, "Light Grey")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if neptune_button.collidepoint(mouse_pos):
                neptune_main = True        
        screen.blit(main_menu_text,(533, 430))


# First question of quiz
def quiz():
    global mouse_correct
    global mouse_wrong
    global image_time
    global question_1
    mouse_pos = pygame.mouse.get_pos() 

    title = font1.render("What  is  left  after  a  planetary  nebula  occurs?",False,"White")
    top_left = small_font.render("White dwarf",False,"White")
    top_right = small_font.render("Black  hole",False,"White")
    bottom_left = small_font.render("Neutron  star",False,"White")
    bottom_right = small_font.render("Super  red  giant",False,"White")
    wrong_text = font.render("Incorrect  Answer!", False, "White")
    right_text = font.render("Correct  Answer!", False, "White")

    quiz_background = pygame.image.load("Quizbackground.jpg").convert()
    quiz_title = pygame.image.load("QuizTitle.jpg")
    quiz_button_top_left = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()
    quiz_button_top_right = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()
    quiz_button_bottom_left = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()
    quiz_button_bottom_right = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()

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
        question_1 = True
        if image_time>0:
            image_time-=1
            screen.blit(quiz_background,(0,0))
            screen.blit(right_text,(130,300))
        if image_time<=0:
            pygame.MOUSEBUTTONDOWN == False
            mouse_correct == False
            question2()

mouse_wrong2=bool(False)
mouse_correct2=bool(False)
image_time2=30

# Second question of quiz
def question2():
    global question_2
    global mouse_correct2
    global mouse_wrong2
    global image_time2
    mouse_pos = pygame.mouse.get_pos()    

    title2 = font1.render("Where  in  the  solar  system  is  the  asteroid  belt  located?",False,"White")
    top_left2 = small_font.render("Between  Jupiter  and  Saturn",False,"White")
    top_right2 = small_font.render("Between  Mars  and  Jupiter",False,"White")
    bottom_left2 = small_font.render("Between  Mercury  and  Venus",False,"White")
    bottom_right2 = small_font.render("Between  Earth  and  Mars",False,"White")
    wrong_text2 = font.render("Incorrect  Answer!", False, "White")
    right_text2 = font.render("Correct  Answer!", False, "White")

    quiz_background2 = pygame.image.load("Quizbackground.jpg").convert()
    quiz_title2 = pygame.image.load("QuizTitle.jpg").convert_alpha()
    quiz_button_top_left2 = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()
    quiz_button_top_right2 = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()
    quiz_button_bottom_left2 = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()
    quiz_button_bottom_right2 = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()

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
        question_2 = True
        if image_time2>0:
            image_time2-=1
            screen.blit(quiz_background2,(0,0))
            screen.blit(right_text2,(130,300))
            if image_time2<=0:
                pygame.MOUSEBUTTONDOWN == False
                mouse_correct2 == False
                question3()

mouse_wrong3=bool(False)
mouse_correct3=bool(False)
image_time3=30

# Third question of quiz
def question3():
    global question_3
    global mouse_correct3
    global mouse_wrong3
    global image_time3
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

    quiz_background3 = pygame.image.load("Quizbackground.jpg").convert()
    quiz_title3 = pygame.image.load("QuizTitle.jpg")
    quiz_button_top_left3 = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()
    quiz_button_top_right3 = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()
    quiz_button_bottom_left3 = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()
    quiz_button_bottom_right3 = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()

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
        question_3 = 20
        if image_time3>0:
            image_time3-=1
            screen.blit(quiz_background3,(0,0))
            screen.blit(right_text3,(130,300))
        if image_time3<=0:
            pygame.MOUSEBUTTONDOWN == False
            mouse_correct3 == False
            question4()

mouse_wrong4=bool(False)
mouse_correct4=bool(False)
image_time4=30

# Fourth question of quiz
def question4():
    global question_4
    global mouse_correct4
    global mouse_wrong4
    global image_time4
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

    quiz_background4 = pygame.image.load("Quizbackground.jpg").convert()
    quiz_title4 = pygame.image.load("QuizTitle.jpg").convert_alpha()
    quiz_button_top_left4 = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()
    quiz_button_top_right4 = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()
    quiz_button_bottom_left4 = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()
    quiz_button_bottom_right4 = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()

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
        question_4 = True
        if image_time4>0:
            image_time4-=1
            screen.blit(quiz_background4,(0,0))
            screen.blit(right_text4,(130,300))
        if image_time4<=0:
            pygame.MOUSEBUTTONDOWN == False
            mouse_correct4 == False
            question5()

mouse_wrong5=bool(False)
mouse_correct5=bool(False)
image_time5=30

# Fifth question of quiz
def question5():
    global question_5
    global mouse_correct5
    global mouse_wrong5
    global image_time5
    mouse_pos = pygame.mouse.get_pos()    

    title5 = font1.render("Where  do  comets  come  from?",False,"White")
    left5 = small_font.render("The  asteroid  belt",False,"White")
    right5 = small_font.render("Oort  Cloud  and  Kuiper  Belt",False,"White")
    wrong_text5 = font.render("Incorrect  Answer!", False, "White")
    right_text5 = font.render("Correct  Answer!", False, "White")

    quiz_background5 = pygame.image.load("Quizbackground.jpg").convert()
    quiz_title5 = pygame.image.load("QuizTitle.jpg").convert_alpha()
    quiz_button_left5 = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()
    quiz_button_right5 = pygame.image.load("QuizFunctionButton.jpg").convert_alpha()

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
        question_5 = True
        if image_time5>0:
            image_time5-=1
            screen.blit(quiz_background5,(0,0))
            screen.blit(right_text5,(130,300))
        if image_time5<=0:
            pygame.MOUSEBUTTONDOWN == False
            mouse_correct5 == False
            quiz_end()

# End screen
def quiz_end():
    global quiz_exit
    mouse_pos = pygame.mouse.get_pos()
    quiz_end_background = pygame.image.load("Quizbackground.jpg").convert()
    ending_message = font1.render("Congratulations,  you  have  finished  the  quiz!",False,"White")
    screen.blit(quiz_end_background,(0,0))
    screen.blit(ending_message,(300,300))

    #Back button for the end of the quiz, to return them to main menu
    quiz_back_button = screen.blit(back_button,(0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if quiz_back_button.collidepoint(mouse_pos):
            quiz_exit = True  

# Displays instrcutions for our game, the objective, and how to use lesson page
def instruction():
    global instruction_exit
    mouse_pos = pygame.mouse.get_pos()
    instruction_background = pygame.image.load("instruction.jpg").convert()
    screen.blit(instruction_background, (0,0))

    # Text for instruction
    instruction_title = font.render("Instructions", False, "White")

    instruction_function_text = small_font.render("In  our  pygame  project  the  objective  of  the game  is  for  the  user  to  play  as  an  extraterrestrial  ", False, "White") 

    instruction_function_text_2 = small_font.render("being  in  a  ship  attempting  to  return  home.  There  are  many  obstacles,  some  being:  the asteroids.", False, "White") 

    instruction_function_text_5 = small_font.render("If you collide with any of the obstacles, its gameover, but you can continue from where you died.    ", False, "White")

    instruction_function_text_6 = small_font.render("There  will be  planet levels you have to complete  in  order  to  collect  fuel.  Each  planet  has  fuel  ", False, "White")

    instruction_function_text_7 = small_font.render("because  you  left  behind  a  little  fuel  in  each  of  the  planets  accidentally.  In  order  to  collect  fuel  all    ", False, "White")

    instruction_function_text_8 = small_font.render("you  have  to  do  is  collide  into  it  with  your character.  You  have  to  collect  fuel  from  each  ", False, "White") 

    instruction_function_text_9 = small_font.render(" planet  in  order  to  move  on.  The  controls  in  order to  move  will  be  the  arrow  keys,  the  top   ", False, "White") 

    instruction_function_text_10 = small_font.render("arrow  key  will  be  used  to  move  up,  the  bottom  arrow  key  will  be  used  to  move downwards,   ", False, "White")
    
    instruction_function_text_11 = small_font.render("left  arrow  key  left,  and  the  right  arrow  key  will  be  used  to  move  to  the  right.", False, "White")

    instruction_function_text_12 = small_font.render("Click on planets, or asteroid belt in lesson for further information about the planet, or asteroid belt.", False, "White")

    # Blitting text for instructions
    screen.blit(instruction_title, (275,135))
    screen.blit(instruction_function_text,(210,280))
    screen.blit(instruction_function_text_2,(210,295))
    screen.blit(instruction_function_text_5,(210,310))
    screen.blit(instruction_function_text_6,(210,325))
    screen.blit(instruction_function_text_7,(210,340))
    screen.blit(instruction_function_text_8,(210,355))
    screen.blit(instruction_function_text_9,(210,370))
    screen.blit(instruction_function_text_10,(210,385))
    screen.blit(instruction_function_text_11,(210,400))
    screen.blit(instruction_function_text_12,(210,415))


    # Back button to return to main menu for instructions
    instruction_back_button = screen.blit(back_button,(0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if instruction_back_button.collidepoint(mouse_pos):
            instruction_exit = True 

# Displays the results of your quiz
def result():
    global result_exit
    question_1_score = int()
    question_2_score = int()
    question_3_score = int()
    question_4_score = int()
    question_5_score = int()

    result_background = pygame.image.load("SpacePixelArt.jpg").convert()
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(result_background,(0,0))
    if question_1:
        question_1_score = 20
    if  question_2:
        question_2_score = 20
    if question_3:
        question_3_score = 20
    if question_4:
        question_4_score = 20
    if question_5:
        question_5_score = 20
    score = (question_1_score+question_2_score+question_3_score+question_4_score+question_5_score)
    result_text = font.render("Your  Score  is",False,"White")
    result_text2 = font.render(str(score),False,"White")
    result_text3 = font.render("Percent",False,"White")
    screen.blit(result_text,(200,200))
    screen.blit(result_text2,(1000,200))
    screen.blit(result_text3,(400,300))   

    # Back button code to return to main menu from results page
    result_back_button = screen.blit(back_button,(0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if result_back_button.collidepoint(mouse_pos):
            result_exit = True    

# Creates a button, with parametres that includes: width, heigh, location,
#  and colour. It returns a surface of the button
def button(width, height, x_surface, y_surface, colour):
    button = pygame.Surface((width, height))
    button.fill(colour)
    mouse_pos = pygame.mouse.get_pos()        
    button_surface = screen.blit(button, (x_surface, y_surface))
    return button_surface

# Invisible button to create player hitboxes, 
# or to make invisible clickable areas
def invisible_button(width, height, x_surface, y_surface):
    button = pygame.Surface((width, height))
    button.set_alpha(0)
    mouse_pos = pygame.mouse.get_pos()        
    button_surface = screen.blit(button, (x_surface, y_surface))
    return button_surface




# Initialization of pygame
pygame.init()
# Setting window size and caption
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Solar Escape Game")
clock = pygame.time.Clock()
font = pygame.font.Font("Pixel_Font.ttf", 75)
font1 = pygame.font.Font("Pixel_Font.ttf", 20)

# Importing all the nessecary files into pygame
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
asteroid = pygame.transform.scale(asteroid, (138.5, 112.5))
fuel = pygame.image.load("fuel.png").convert_alpha()
fuel = pygame.transform.scale(fuel, (25, 93))
venus_bg = pygame.image.load("venus_bg.jpg").convert()
comet = pygame.image.load("comet.png").convert_alpha()
comet = pygame.transform.scale(comet, (101.25, 241.5))
astro_fuel = pygame.image.load("Astronaut_Fuel.png").convert_alpha()
earth_bg = pygame.image.load("earth_bg.jpg").convert()
mars_bg = pygame.image.load("mars_background.jpg").convert()
jupiter_bg = pygame.image.load("jupiter_bg.jpg").convert()
saturn_bg = pygame.image.load("saturn_bg.jpg").convert()
neptune_bg = pygame.image.load("neptune_bg.jpg").convert()
back_button = pygame.image.load("back_button.png")
citations = pygame.image.load("Citation.png").convert()

# Creating all text blits
text1 = font.render("Solar  Escape",False, "White")
text2 = font1.render("Press  any  key  to  start",False, "White")
game_over = font.render("Finished!",False, "White")
main_menu_text = font1.render("Main Menu", False, "Black")
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

# Variables for game

astronaut_x_mercury = 1024
astronaut_y_mercury = 399
astronaut_x_venus = 640
astronaut_y_venus = 400

astronaut_x_earth = 1024
astronaut_y_earth = 413

astronaut_x_mars = 1024
astronaut_y_mars = 383

astronaut_x_neptune = 700
astronaut_y_neptune = 400
astronaut_collide_neptune = False

fuel_x_venus = random.randint(1,1280)
fuel_y_venus = random.randint(-1500, -1200)

fuel_x_a = random.randint(-1500, -1200)
fuel_y_a = random.randint(1, 720)

fuel_x_j = random.randint(-1500, -1200)
fuel_y_j = random.randint(1, 720)

fuel_x_s = random.randint(-1500, -1200)
fuel_y_s = random.randint(1, 720)

comet1_x= random.randint(1,1280)
comet1_y= -200
comet2_x= random.randint(1,1280)
comet2_y= -500
comet3_x= random.randint(1,1280)
comet3_y=-300
comet4_x= random.randint(1,1280)
comet4_y=-50

asteroid_x1 = -200
asteroid_y1 = random.randint(1, 720)
asteroid_x2 = -500
asteroid_y2 = random.randint(1, 720)
asteroid_x3 = -300
asteroid_y3 = random.randint(1, 720)
asteroid_x4 = -50
asteroid_y4 = random.randint(1, 720)

jupiter_x1 = -200
jupiter_y1 = random.randint(1, 720)
jupiter_x2 = -500
jupiter_y2 = random.randint(1, 720)
jupiter_x3 = -300
jupiter_y3 = random.randint(1, 720)
jupiter_x4 = -50
jupiter_y4 = random.randint(1, 720)

saturn_x1 = -200
saturn_y1 = random.randint(1, 720)
saturn_x2 = -500
saturn_y2 = random.randint(1, 720)
saturn_x3 = -300
saturn_y3 = random.randint(1, 720)
saturn_x4 = -50
saturn_y4 = random.randint(1, 720)

astro_x_a = 200
astro_y_a = 150

astro_x_j = 200
astro_y_j = 150

astro_x_s = 200
astro_y_s = 150


jupiter_x_pos = 0

saturn_x_pos = 0

galaxy_x_pos = 0

# Setting variables to false for buttons,
# or if a player loses in the game
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
main_venus = False
main_end = False
a_collide = False
astronaut_collide_earth = False 
astronaut_collide_a = False
astronaut_collide_mars = False 
j_collide = False 
astronaut_collide_j = False
s_collide = False 
astronaut_collide_s = False

lesson_exit = False
sun_exit = False
mercury_exit = False
venus_exit = False
earth_exit = False
mars_exit = False
instruction_exit = False
quiz_exit = False
result_exit = False
asteroid_belt_exit = False
jupiter_exit = False
saturn_exit = False
uranus_exit = False
neptune_exit = False
instruction_exit = False
quiz_exit = False
result_exit = False
neptune_main = False
pygame_exit_time = 60


mouse_wrong=bool(False)
mouse_correct=bool(False)
image_time=30
question_1 = False
question_2 = False
question_3 = False
question_4 = False
question_5 = False


# Main game loop
while True:
    # Quitting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mouse_pressed_quit = True


    # Title page, and calling the main 
    # menu function if a button is clicked
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

    # Updating the display, and refresh rate for the game
    pygame.display.update()    
    clock.tick(60)