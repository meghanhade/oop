import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys


#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 6
GAME_HEIGHT = 6

#### Put class definitions here ####
class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False

    def interact(self,player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just won back a gem! You have %d items!" % (len(player.inventory)))

class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = False

    # def interact(self, player):
    #     player.IMAGE = "Invisible"

class Character(GameElement):
    IMAGE = "Dirt"
    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return(self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        else:
            return None
    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

    def interact (self,Rock):
        IMAGE = "Heart"
        return IMAGE




####   End class definitions    ####

def keyboard_handler():
    direction = None
    if KEYBOARD[key.UP]:
        direction = "up"
        
        
    elif KEYBOARD[key.DOWN]:
        direction = "down"
        
        
    elif KEYBOARD[key.LEFT]:
        direction = "left"
        
        
    elif KEYBOARD[key.RIGHT]:
        direction = "right"
        
        
    

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        if next_location[0] in range(0,GAME_WIDTH) and next_location[1] in range(0, GAME_HEIGHT):
            existing_el = GAME_BOARD.get_el(next_x, next_y)

            if existing_el:
                existing_el.interact(PLAYER)

            #if existing_el is not existing_el.SOLID:
            if existing_el is not None:
                PLAYER.IMAGE = existing_el.IMAGE
                GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
                #GAME_BOARD.set_el(next_x, next_y, PLAYER)
                GAME_BOARD.set_el(next_x, next_y, PLAYER)
                #setup_images()
                print PLAYER.IMAGE
            else:
                GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
                GAME_BOARD.set_el(next_x, next_y, PLAYER)
        # else:
        #     GAME_BOARD.draw_msg("Cannot go off board")

def initialize():
    
    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2, 2, PLAYER)
    print PLAYER

    rock_positions = [
            (2,1),
            (1,2),
            (3,2),
            (2,3),
            (1,1),
            (1,3),
            (1,4),
            (0,0)
        ]

    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    # rocks[-5].SOLID = False

    for rock in rocks:
        print rock

    GAME_BOARD.draw_msg("YOU MUST WIN IT BACK")
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3,1, gem)

    keyboard_handler()