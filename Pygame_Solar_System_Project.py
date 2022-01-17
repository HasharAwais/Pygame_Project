import pygame
import sys
import random
import time

quiz_mouse_pressed=bool(False)
instruction_mouse_pressed=bool(False)
mouse_pressed=bool(False)
mouse_pressed_result=bool(False)

def main_menu():
  global mouse_pressed
  global mouse_pressed_quit  
  global mouse_pressed_lesson 
  global quiz_mouse_pressed
  global instruction_mouse_pressed
  global mouse_pressed_result

  screen.blit(galaxy,(0,0))
  main_menu_text = font.render("Main Menu", False, "White")   
  instruction_text = average_font.render("Instructions", False, "Black")
  lesson_text = average_font.render("Lesson", False, "Black") 
  game_text = average_font.render("Game", False, "Black")
  quiz_text = average_font.render("Quiz", False, "Black") 
  result_text = average_font.render("Results", False, "Black") 
  quit_text = average_font.render("Quit", False, "Black") 

  lesson_button = menu_button
  instruction_button = menu_button
  game_button = menu_button
  quiz_button = menu_button
  result_button = menu_button
  quit_button = menu_button
  
  lesson_surface = screen.blit(lesson_button,(30, 500))
  instruction_surface = screen.blit(instruction_button,(240, 500))
  game_surface = screen.blit(game_button,(450, 500))
  quiz_surface = screen.blit(quiz_button,(660, 500))
  result_surface = screen.blit(result_button, (870, 500))
  quit_surface = screen.blit(quit_button,(1080, 500))  
    
  screen.blit(lesson_text, (75, 520))
  screen.blit(instruction_text, (255, 520))
  screen.blit(game_text, (500, 520))  
  screen.blit(quiz_text, (715, 520))    
  screen.blit(result_text, (915, 520))  
  screen.blit(quit_text, (1135, 520))           
  screen.blit(main_menu_text,(460,300))
       
  mouse_pos = pygame.mouse.get_pos() 

  if event.type == pygame.MOUSEBUTTONDOWN:
    if lesson_surface.collidepoint(mouse_pos):
      mouse_pressed = True
  if event.type == pygame.MOUSEBUTTONDOWN:
    if instruction_surface.collidepoint(mouse_pos):
      instruction_mouse_pressed = True
  if event.type == pygame.MOUSEBUTTONDOWN:
    if game_surface.collidepoint(mouse_pos):
      mouse_pressed = True
  if event.type == pygame.MOUSEBUTTONDOWN:
    if quiz_surface.collidepoint(mouse_pos):
      quiz_mouse_pressed = True
  if event.type == pygame.MOUSEBUTTONDOWN:
    if result_surface.collidepoint(mouse_pos):
      mouse_pressed_result = True
  if event.type == pygame.MOUSEBUTTONDOWN:
    if quit_surface.collidepoint(mouse_pos):
      mouse_pressed_quit = True
        
  if mouse_pressed == True:
    screen.blit(galaxy,(0,0))
  if instruction_mouse_pressed:
    instruction()
  if mouse_pressed_quit == True:
    pygame.quit()
    sys.exit()
  if quiz_mouse_pressed == True:
    quiz()
  if mouse_pressed_result == True:
    result()


quiz_counter=int(0)
mouse_wrong=bool(False)
mouse_correct=bool(False)
image_time=30

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
date_text=small_font.render("January  17,  2022", False, "White")
name_text=average_font.render("By:  Awais  and  Zubair", False, "White")
teacher_text=average_font.render("Instructor:  Ms.  Keras", False, "White")
class_code_text=average_font.render("Class:  ICS207", False, "White")
menu_button = pygame.image.load("button.jpg")

pygame.mixer.music.load("title.wav")
pygame.mixer.music.play(-1)


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