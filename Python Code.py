import pygame
import time
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
    pygame.display.flip()
    time.sleep(1)
    pygame.display.quit()
    winner_screen = pygame.image.load("Assets/Slot Symbols/Winner!.jpg")
    winner_screen_width, winner_screen_height = winner_screen.get_width(), winner_screen.get_height()
    winner_screen_display = pygame.display.set_mode((winner_screen_width,winner_screen_height))
    winner_screen_display.blit(winner_screen)
    print(type(winner_screen_display))
    pygame.display.flip()
    time.sleep(3)
    return player



    



class Sprite():
    def __init__(self, imagefilepath, position,screen):
        self.image = pygame.image.load(imagefilepath)
        self.position = position
        self.screen = screen
    def blit(self):
        self.screen.blit(self.image,self.position)
    def updatePosition():
        pass
class Ship(Sprite):
    def __init__(self, imagefilepath, screen):
        super().__init__(imagefilepath, screen)
        self.currentAngle = 0
        self.position = (screen.get_width()/2-self.image.get_width()/2,screen.get_height()/2-self.image.getwidth())
    def shoot():
        pass
    def gameover():
        pass

class Projectile(Sprite):
    def __init__(self, imagefilepath, position, screen):
        super().__init__(imagefilepath, position, screen)
        self.speed_x = 10
        self.speed_y = 10

class Asteroid(Projectile):
    def __init__(self, imagefilepath,screen):
        
        # easy way to get an asteroid at atleast 1 maximum and randomised position so anywhere on outside of screen
        if random.randint(1,2) == 2:
            if random.randint(1,2) == 2:
                self.position = (screen.get_width(),random.randint(0,screen.get_height()))
            else:
                self.position = (0,random.randint(0,screen.get_height()))
        else:
            if random.randint(1,2) == 1:
                self.position = (random.randint(0,screen.get_width()),screen.get_height())
            else:
                self.position = (random.randint(0,screen.get_width()),0)
        super().__init__(imagefilepath, self.position ,screen)
        self.speed = 5 #random.randint(250,500)
    
    def towardsCenter(self,screen,asteroids):
        try:
            self.x_difference = screen.get_width() / 2 - self.position[0]
            self.y_difference = screen.get_height() / 2 - self.position[1]
            ratiomultiplier = (self.x_difference ** 2 + self.y_difference **2 ) **0.5
            self.x_difference /= ratiomultiplier
            self.y_difference /= ratiomultiplier
            self.x_difference *= self.speed
            self.x_difference *= self.speed
            self.position = (int(round(self.position[0]+self.x_difference)), int(round(self.position[1]+self.y_difference)))
        except:
            return asteroids.remove(self)
    
def asteroid_shooter():
    pygame.display.quit()
    screen = pygame.display.set_mode()
    clock.tick(60)
    asteroids = []
    ship = Ship("Assets/Asteroid/SpaceShip.png",screen)
    ship.blit()
    while True:
        if random.randint(1,1) == 1:
            asteroids.append(Asteroid("Assets/Asteroid/Asterod.png",screen))
        quitting_script()
        screen.fill(1)
        screen.blit(screen)
        for ass in asteroids:
            ass.towardsCenter(screen,asteroids)
            ass.blit()
        pygame.display.flip()


    

    

























def game_current(game_current):
    game_current = 2
    if game_current == 1:
        return slots()
    if game_current == 2:
        return asteroid_shooter()
    

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
