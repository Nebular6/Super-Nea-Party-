import pygame
import random
pygame.init()
screen = pygame.display.set_mode()
pygame.display.set_caption("Super Nea Party")
Screen_size = pygame.display.get_window_size()
clock = pygame.time.Clock()
main_loop = True
current_selected_game = 2

def slots():
    pygame.display.quit()
    print("hai")
    slot_machine = pygame.image.load("Assets/SlotMachine.png")
    new_screen_width = slot_machine.get_width()
    new_screen_height = slot_machine.get_height() 
    screen_slots = pygame.display.set_mode((new_screen_width, new_screen_height))
    screen_slots.blit(slot_machine)
    symbol_list = ["Seven.png","Melon.png","Diamond.png"]
    symbols = []
    keys = pygame.key.get_pressed()
    if keys[pygame.K_e] == True:
        for i in range(3):
            symbols.append(pygame.image.load("Assets/Slot Symbols/" + symbol_list[random.randint(0,2)]))
    x_pos_slot_symbols = 220
    for item in symbols:
        screen_slots.blit(item,(x_pos_slot_symbols,250))
        x_pos_slot_symbols += 62.5
    pygame.display.flip()


def game_current(game_current):
    if game_current == 1:
        slots()
    if game_current == 2:
        pass
    

while main_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] == True: #general way to get a keyto have an effect
        current_selected_game = random.randint(1,2) #selects a random integer correlating to one of the games 
    game_current(current_selected_game)


    pygame.display.flip() #updates the screen
    clock.tick(60)        #sets the framerate 