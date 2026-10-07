"""
Author: Prof. Alyssa
Creates and displays the graphics
based on the current state of the board.
You do NOT need to modify this file.
"""

import pygame

from preferences import Preferences
from gameData import GameData
from cell import Cell

class BoardDisplay:
    def __init__(self):
        # The background window where everything will be drawn
        self.screen = pygame.display.set_mode((Preferences.BOARD_WIDTH, 
                                              Preferences.BOARD_HEIGHT))
        self.player_img = None 
        self.food_img = None
        self.enemy_img = None
        # Load the images 
        self.load_images()

    def load_images(self) -> None:
        """ Try loading the images specified in the preferences file, 
            or indicate to the user that the images failed to load. """
        
        try:
            self.player_img = pygame.image.load(Preferences.PLAYER_IMAGE)
            self.food_img = pygame.image.load(Preferences.FOOD_IMAGE)
            self.enemy_img = pygame.image.load(Preferences.ENEMY_IMAGE)
        except:
            print("Failed to load image(s)")
        
    def draw_board(self, game_data: GameData) -> None:
        """ Re-draws the board and all cards based 
            on the current state of the board """
        
        # Reset the board
        self.clear_board()

        # Fill in each cell with the appropriate image
        for row in range(Preferences.NUM_ROWS):
            for col in range(Preferences.NUM_COLS):
                cell = game_data.board[row][col]
                self.draw_cell(cell)
        
        # Add the score
        self.draw_score(game_data.score)

        # Draw the game over message if applicable
        if game_data.gameover:
            self.display_gameover()

        # Update the display
        pygame.display.update()

    def draw_cell(self, cell: Cell) -> None:
        """ Draws a cell-sized square at the appropriate location """

        row = cell.get_row()
        col = cell.get_col()

        if cell.is_player() and self.player_img:
            self.draw_image(self.player_img, row, col)
                
        elif cell.is_food() and self.food_img:
            self.draw_image(self.food_img, row, col)

        elif cell.is_enemy() and self.enemy_img:
            self.draw_image(self.enemy_img, row, col)

        # If the images were not loaded properly, 
        # fill in the square with the appropriate color
        elif not cell.is_empty():
            self.draw_square(cell.get_color(), row, col)

        # Do nothing if the cell is empty
        
    def draw_image(self, image: pygame.Surface, 
                        row: int, col: int) -> None:
        """ Displays the given image at the given cell location """

        # First, convert the image to a Surface type
        image = image.convert_alpha()
        # Scale the image to fit within a cell
        image = pygame.transform.scale(image,
                                (Preferences.CELL_WIDTH, Preferences.CELL_HEIGHT))
        # Get the dimensions of the image
        image_rect = image.get_rect()
        # Position the image in the center of the cell
        image_rect.center = ((col*Preferences.CELL_WIDTH) + (Preferences.CELL_WIDTH / 2),
                        (row*Preferences.CELL_HEIGHT) + (Preferences.CELL_HEIGHT / 2))
        # Place the image on the screen
        self.screen.blit(image, image_rect)

    def draw_square(self, color: pygame.Color, 
                        row: int, col: int) -> None:
        """ Draw a cell-sized square at the given location """
        pygame.draw.rect(self.screen, # The surface to draw on
                        color, # What color to draw the cell
                        [col*Preferences.CELL_WIDTH,  # Top left corner x position
                         row*Preferences.CELL_HEIGHT, # Top left corner y position
                         Preferences.CELL_WIDTH,      # Cell width
                         Preferences.CELL_HEIGHT])    # Cell height

    def clear_board(self) -> None:
        """ Reset the background of the screen """
        self.screen.fill(Preferences.COLOR_BACKGROUND)
        
    def draw_score(self, score: int) -> None:
        """ Display the score on the screen """

        # Get the font
        font = Preferences.SCORE_FONT
        # Create the text
        text = font.render(Preferences.SCORE_TEXT.format(score), 
                           True, Preferences.SCORE_FONT_COLOR)
        # Get the dimensions of the text box
        text_rect = text.get_rect()
        # Position the text at the bottom left of the screen
        text_rect.topleft = (0, Preferences.NUM_ROWS * Preferences.CELL_HEIGHT)
        # Place the text on the screen
        self.screen.blit(text, text_rect)
       
    def display_gameover(self) -> None:
        """ Displays the game over message on the screen """

        # Get the font
        font = Preferences.GAMEOVER_FONT
        # Create the text 
        text = font.render(Preferences.GAMEOVER_TEXT, 
                           True, Preferences.GAMEOVER_FONT_COLOR)
        # Get the dimensions of the text box
        text_rect = text.get_rect()
        # Position the text in the middle of the screen
        text_rect.center = (Preferences.BOARD_WIDTH / 2, Preferences.BOARD_HEIGHT / 2)
        # Place the text on the screen
        self.screen.blit(text, text_rect)