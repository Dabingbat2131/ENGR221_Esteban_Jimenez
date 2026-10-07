"""
Author: Prof. Alyssa
Defines constants to be used for the program.
You do NOT need to modify this file.
"""

import pygame
import os

class Preferences:
    """ Defines values for constant values.
        This is good practice to avoid "magic numbers" """
    
    pygame.init()

    ########
    # TEXT #
    ########

    FONT_SIZE = 28
    FONT = pygame.font.SysFont(None, FONT_SIZE)
    FONT_COLOR = pygame.Color('black')

    ##########
    # SIZING #
    ##########

    NUM_ELEMENTS = 20 # Number of bars
    BAR_WIDTH = 30    # Width of bars in pixels
    UNIT_HEIGHT = 10  # Height of "1" unit in pixels

    WIDTH = BAR_WIDTH * NUM_ELEMENTS  # Width of the window 
    HEIGHT = 500 # Height of the window

    MAX_VAL = (HEIGHT - 100) // UNIT_HEIGHT

    ##########
    # COLORS #
    ##########

    BACKGROUND_COLOR = pygame.Color('white')
    BAR_COLOR = pygame.Color('gray')
    BAR_INNER_COLOR = pygame.Color('red')
    BAR_OUTER_COLOR = pygame.Color('blue')

    ##########
    # TIMING #
    ##########
    
    # How long to sleep between updates (ms)
    SLEEP_TIME = 50


    ############
    # GRAPHICS #
    ############

    # Directory containing the images
    IMG_DIR = os.path.join(os.path.dirname(
                            os.path.realpath(__file__)),
                            "images")

    # Image to display as the player
    BAR_IMAGE = os.path.join(IMG_DIR, "carrot.png")
    BAR_INNER_IMAGE = os.path.join(IMG_DIR, "carrot_inner.png")
    BAR_OUTER_IMAGE = os.path.join(IMG_DIR, "carrot_outer.png")