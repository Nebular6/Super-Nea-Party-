import pygame
import time
import math
import random
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
main_loop = True
current_frame = 0






def quitting_script():
        """ subroutine to be called every game frame to allow users to quit whenever """
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                pygame.display.quit()
                return False
        return True


def set_setbackground_image(rel_path):
    """ i set windows with a background image, since i want to create multiple games i can utilise this subroutine to 
        set one easily just using the relitive path to the image """
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
    """ Simple Subroutine to return if the game state is currently "WON" or not """
    if symbols[0] == symbols[1] == symbols[2]:
        return False
    else:
        return True


def draw_symbols(symbol_list,symbols,screen_slots,x_pos_slot_symbols):
    """ Subroutine to create the different symbols whenever a new "spin" is played """
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
    """ Main game loop for slots """
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
            if events[pygame.K_SPACE]:
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
    """ Main Sprite superclass to build other classes off of, has a screen image and position values """
    
    def __init__(self, imagefilepath, position,screen):
        self.image = pygame.image.load(imagefilepath)
        self.position = position
        self.screen = screen

    def updateimage(self):
        """ I gave the sprite class this subroutine so each subsequent class can update their position easily """
        self.screen.blit(self.image,self.position)
    

class Ship(Sprite):
    """ The ship class, subclass of sprite allows the additional attirubtes of 
        its imagefilepath mainly to display the ship furthermore it has an angle 
        of rotation  """
    
    def __init__(self, imagefilepath, screen):
        position = 0
        super().__init__(imagefilepath, position ,screen)
        self.current_angle = 0
        self.position = (screen.get_width()/2-self.image.get_width()/2,screen.get_height()/2-self.image.get_width())
        self.rotatedimage = self.image
        self.time_of_movement = time.time()
        self.timeofshoot = time.time()

    def position(self):
        """ yep """
        return self.position
    
    def current_angle(self):
        """ yep.2 """
        return self.current_angle

    def ship_direction(self,keys):
        """ Subroutine to allow the ship to rotate and updates its image as such using a and d  """
        req = self.time_of_movement - time.time()
        if req > -0.01:
            return
        else:
            rotate_angle = self.current_angle
            if keys[pygame.K_a]:
                rotate_angle = self.current_angle + 5
            if keys[pygame.K_d]:

                rotate_angle = self.current_angle - 5
            self.current_angle = self.current_angle % 360
            self.current_angle = rotate_angle
            self.rotatedimage = pygame.transform.rotate(self.image,self.current_angle)
            self.time_of_movement = time.time()

    def Shoot(self,screen):
        """ adds a Projectile to the game in bullet list when shot to be updated ect """
        pygame.mixer.music.load("Assets\Sounds\laser-shot-ingame-230500.mp3")
        pygame.mixer.music.play()
        return Projectile("Assets/Asteroid/bullet.png",(0,0),screen,self)


class Projectile(Sprite):
    """ Class for bullets shot by script """
    def __init__(self, imagefilepath, position, screen, ship):
        super().__init__(imagefilepath, position, screen)
        """ code to translate the current rotation of the ship into the direction of travel the bullet needs to go """
        self.position = (screen.get_width()/2-self.image.get_width()+50/2,screen.get_height()/2-self.image.get_width()+50)
        self.ship = ship
        self.angleoftravel = self.ship.current_angle + 90
        self.xmove = 10 * math.cos((-self.angleoftravel * (0.01745329)))  
        self.ymove = 10 * math.sin((-self.angleoftravel * (0.01745329)))  

    def updatepos(self):
        """ moves the bullet in the direction of travel & updates its image """
        self.position = self.position[0]+self.xmove,self.position[1]+self.ymove
        self.updateimage()


class Asteroid(Sprite):
    def __init__(self, imagefilepath,screen):
        """ initiates the asterioid in one of the random 4 corners  """
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
        super().__init__(imagefilepath,self.position,screen)
        self.speed = random.randint(1,5)  #random.randint(250,500)
    
    def towardsCenter(self,screen,asteroids):
        """ Moves all asteroids towards the middle of the screen; Ship  """
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
            print("brain please ")
            return asteroids.remove(self) # gameover
            

    def checkcollision(self, bullet,asteroids):
        """ checks collision between all currently living asteroids for bullets """
        if self.position[0] < bullet.position[0] < self.position[0] + self.image.get_width():
            if self.position[1] < bullet.position[1]<self.position[1] + self.image.get_height():
                asteroids.remove(self)
            pass
        pass    


def asteroid_shooter():
    pygame.display.quit()
    screen = pygame.display.set_mode()
    clock.tick(60)
    asteroids = []
    bullets = []
    ship = Ship("Assets\Asteroid\SpaceShip.png", screen)
    framecountlocal = 0
    ship.image = pygame.transform.scale(ship.image,(100,100))
    ship.updateimage()
    while True:
        keys = pygame.key.get_pressed()
        if random.randint(1,200) == 100:
            asteroids.append(Asteroid("Assets\Asteroid\Asterod.png",screen))    
        quitting_script()
        screen.fill(1)
        screen.blit(screen)
        ship.ship_direction(keys)
        framecountlocal += 1
        if  framecountlocal % 20 == 1:
            bullets.append(ship.Shoot(screen))
        for item in bullets:
            Projectile.updatepos(item)
        screen.blit(ship.rotatedimage,(ship.position))
        for ass in asteroids:
            ass.towardsCenter(screen,asteroids)
            ass.updateimage()
            for item in bullets:
                ass.checkcollision(item,asteroids)
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
