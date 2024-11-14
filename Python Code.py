import pygame
import random
pygame.init()
screen = pygame.display.set_mode()
pygame.display.set_caption("Super Nea Party")
Screen_size = pygame.display.get_window_size()
clock = pygame.time.Clock()
main_loop = True
current_frame = 0


def quitting_script():
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                return False
        return True

def centering(image_path, desired_x, desired_y):
    currentimage = pygame.image.load(image_path)
    currentimageheight, currentimagewidth = currentimage.height, currentimage.width
    # works out current image dimensions
    actual_x = desired_x - currentimagewidth/2
    actual_y = desired_y - currentimageheight/2  
    return actual_x, actual_y



def check_if_win(screen_slots,new_screen_height,new_screen_width,symbols):
    if symbols[0] == symbols[1] == symbols[2]:
        screen_slots.blit(pygame.image.load("Assets\Slot Symbols\Winner!.jpg"),(0,0))
        return False
    else:
        return True


def draw_symbols(symbol_list,symbols,screen_slots,x_pos_slot_symbols):
    for i in range(3):
        symbols.append(pygame.image.load("Assets/Slot Symbols/" + symbol_list[random.randint(0,2)]))
    for item in symbols:  
        screen_slots.blit(item,(x_pos_slot_symbols,250))
        x_pos_slot_symbols += 62.5



def slots():
    global current_frame
    current_frame += 1
    pygame.display.quit()
    slot_machine = pygame.image.load("Assets/SlotMachine.png")
    new_screen_width = slot_machine.get_width()
    new_screen_height = slot_machine.get_height() 
    screen_slots = pygame.display.set_mode((new_screen_width, new_screen_height))
    symbol_list = ["Seven.png","Melon.png","Diamond.png"]
    gambling = True
    while gambling:
        symbols = []
        x_pos_slot_symbols = 220
        pygame.display.flip()
        screen_slots.blit(slot_machine)
        draw_symbols(symbol_list,symbols,screen_slots,x_pos_slot_symbols)
        gambling = check_if_win(screen_slots,new_screen_height, new_screen_width,symbols)
        gambling = quitting_script()

        

def game_current(game_current):
    if game_current == 1:
        slots()
    if game_current == 2:
        pass
    

while main_loop:
    current_frame += 1
    main_loop = quitting_script()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] == True: #general way to get a keyto have an effect
        current_selected_game = random.randint(1,2) #selects a random integer correlating to one of the games 
        game_current(current_selected_game)
    #game_current(1)


    pygame.display.flip() #updates the screen
    clock.tick(60)        #sets the framerate 


