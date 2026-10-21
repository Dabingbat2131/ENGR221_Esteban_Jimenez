"""
Author: Prof. Alyssa
Defines constants to be used for the program.
You do NOT need to modify this file.
"""

import pygame
import os 

class Preferences:
    """ Defines values for constant variables.
        This is good practice to avoid "magic numbers" """
    
    pygame.init()
    
    ########
    # TEXT #
    ########

    SCORE_FONT_SIZE = 25
    SCORE_FONT = pygame.font.SysFont(None, SCORE_FONT_SIZE)
    SCORE_FONT_COLOR = pygame.Color('black')
    SCORE_TEXT = "Ducks collected: {}"

    GAMEOVER_FONT_SIZE = 50
    GAMEOVER_FONT = pygame.font.SysFont(None, GAMEOVER_FONT_SIZE)
    GAMEOVER_FONT_COLOR = pygame.Color('red')
    GAMEOVER_TEXT = "You stepped on a duck!\nPress any key to exit."


    ##########
    # SIZING #
    ##########

    CELL_WIDTH = 40           # In pixels
    CELL_HEIGHT = CELL_WIDTH  # In pixels

    NUM_ROWS = 15   # Number of rows in the board
    NUM_COLS = 20   # Number of columns in the board

    # Total number of cells on the board
    NUM_CELLS = NUM_ROWS * NUM_COLS  

    # Calculate board size
    BOARD_WIDTH = CELL_WIDTH * NUM_COLS
    BOARD_HEIGHT = CELL_HEIGHT * NUM_ROWS + SCORE_FONT_SIZE


    ###############
    # CELL COLORS #
    ###############

    COLOR_BACKGROUND = pygame.Color('white')
    COLOR_PLAYER = pygame.Color('blue')
    COLOR_BODY = pygame.Color('green')
    COLOR_FOOD = pygame.Color('red')


    ##########
    # TIMING #
    ##########

    # How long to sleep between updates (ms)
    SLEEP_TIME = 50
    # How frequently to add food to the board (cycles)
    FOOD_ADD_RATE = 100
    # How frequently to move the player
    REFRESH_RATE = 5


    ############
    # GRAPHICS #
    ############

    # Directory containing the images
    IMG_DIR = os.path.join(os.path.dirname(
                            os.path.realpath(__file__)), 
                            'images')

    # Image to display as the player
    PLAYER_IMAGE = os.path.join(IMG_DIR, "horse.png")
    # Image to display as the body
    BODY_IMAGE = os.path.join(IMG_DIR, 'duck.png')
    # Image to display as food
    FOOD_IMAGE = os.path.join(IMG_DIR, "duck_food.png")


    #######################
    # CELL CONFIGURATIONS #
    #######################

    # Only allow 20% of the board to be food at once
    MAX_FOOD = NUM_CELLS // 5 