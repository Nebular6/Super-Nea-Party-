import pygame
import random
pygame.init()
clock = pygame.time.Clock()
main_loop = True
current_frame = 0




def quitting_script():
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                pygame.display.quit()
                return False
        return True


def set_setbackground_image(rel_path):
    pygame.display.quit()
    screen = pygame.display.set_mode()
    pygame.display.set_caption("Super Nea Party")
    backing_image = pygame.image.load(rel_path)
    screen_width, screen_height = backing_image.get_width(), backing_image.get_height()
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.blit(backing_image)
    util = [screen, backing_image]
    return util


def check_if_win(screen_slots,new_screen_height,new_screen_width,symbols):
    if symbols[0] == symbols[1] == symbols[2]:
        return False
    else:
        return True


def draw_symbols(symbol_list,symbols,screen_slots,x_pos_slot_symbols):
    symboll_list_usable = []
    for i in range(3):
        used_symbol = symbol_list[random.randint(0,2)]
        symbols.append(pygame.image.load("Assets/Slot Symbols/" + used_symbol))
        symboll_list_usable.append(used_symbol)
    for item in symbols:  
        screen_slots.blit(item,(x_pos_slot_symbols,250))
        x_pos_slot_symbols += 62.5
    return symboll_list_usable


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
    won = True
    player = 0
    while gambling and won:
            current_frame += 1
            events = pygame.key.get_just_pressed()
            gambling = quitting_script()
            pygame.display.flip()
            if events[pygame.K_h]:
                player += 1
                symbols = []
                x_pos_slot_symbols = 220
                pygame.display.flip()
                screen_slots.blit(slot_machine)
                win_condition = draw_symbols(symbol_list,symbols,screen_slots,x_pos_slot_symbols)
                won = check_if_win(screen_slots,new_screen_height, new_screen_width,win_condition)
    pygame.display.quit()
    winner_screen = pygame.image.load("Assets\Slot Symbols\Winner!.jpg")
    winner_screen_width, winner_screen_height = winner_screen.get_width(), winner_screen.get_height()
    winner_screen_display = pygame.display.set_mode((winner_screen_width,winner_screen_height))
    winner_screen_display.blit(winner_screen)
    pygame.display.flip()
    waiting_for_input = True
    while waiting_for_input:
        if events[pygame.K_SPACE]:
            return player
        
    
        

def game_current(game_current):
    if game_current == 1:
        return slots()
    if game_current == 2:
        pass
    

display = set_setbackground_image("Assets/Untitled.png")
display[0].blit(display[1])
while main_loop:
    current_frame += 1
    main_loop = quitting_script()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] == True: #general way to get a keyto have an effect
        current_selected_game = random.randint(1,2) #selects a random integer correlating to one of the games 
        playerwin = game_current(current_selected_game)
    pygame.display.flip() #updates the screen
    clock.tick(60)        #sets the framerate 

