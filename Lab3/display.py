"""
Author: Prof. Alyssa
Creates and displays the graphics.
You do NOT need to modify this file.
"""

import pygame 

from preferences import Preferences 

class Display:
    def __init__(self):
        # The background window where everything will be drawn
        self.screen = pygame.display.set_mode((
            Preferences.WIDTH, Preferences.HEIGHT
        ))
        pygame.display.set_caption("Sorting Algorithm Visualizer")

        # Text to be displayed
        self.text = "S: Selection Sort | I: Insertion Sort | B: Bubble Sort | R: Reset\n" \
                    "Right: Advance one step | Space: Advance continuously"

        self.default_img = None
        self.inner_img = None 
        self.outer_img = None
        self.load_images()

    def load_images(self) -> None:
        """ Try loading the images specified in the preferences file, 
            or indicate to the user that the images failed to load. """
        
        try:
            self.default_img = pygame.image.load(Preferences.BAR_IMAGE)
            self.inner_img = pygame.image.load(Preferences.BAR_INNER_IMAGE)
            self.outer_img = pygame.image.load(Preferences.BAR_OUTER_IMAGE)
        except:
            print("Failed to load image(s)")
        

    def draw_text(self):
        """ Display the text on the screen """

        # Create the text
        text = Preferences.FONT.render(
            self.text,
            True,
            Preferences.FONT_COLOR
        )
        # Get the dimensions of the text box
        text_rect = text.get_rect()
        # Position the text at the top center of the screen
        text_rect.center = (Preferences.WIDTH / 2, Preferences.FONT_SIZE)
        # Place the text on the screen
        self.screen.blit(text, text_rect)


    def draw(self, array, outer_idx=-1, inner_idx=-1):
        """ Draw the state of the array """

        self.clear_screen()
        self.draw_text()

        for i, val in enumerate(array):
            bar_x = i * Preferences.BAR_WIDTH
            bar_y = Preferences.HEIGHT - (val * Preferences.UNIT_HEIGHT)

            color = Preferences.BAR_COLOR
            img = self.default_img
            if i == outer_idx:
                color = Preferences.BAR_OUTER_COLOR
                img = self.outer_img
            elif i == inner_idx:
                color = Preferences.BAR_INNER_COLOR
                img = self.inner_img

            if self.default_img:
                bar_rect = self.draw_image(img, val, bar_x, bar_y)
            else:
                bar_rect = pygame.draw.rect(self.screen, # The surface to draw on
                             color, # The color to draw the cell
                             (bar_x, bar_y, # Top left corner x and y
                              Preferences.BAR_WIDTH-1, # Width
                              val * Preferences.UNIT_HEIGHT)) # Height
            

            
            # Show the value on the bar
            val_text = Preferences.FONT.render(str(val), True, Preferences.FONT_COLOR)
            val_rect = val_text.get_rect(center=(bar_rect.centerx, bar_y-Preferences.FONT_SIZE/2))
            self.screen.blit(val_text, val_rect)
            
        pygame.display.update()

    def draw_image(self, image: pygame.Surface, val: int,
                        bar_x: int, bar_y: int) -> None:
        """ Displays the given image at the given location """

        # First, convert the image to a Surface type
        image = image.convert_alpha()
        # Scale the image to fit within a cell
        image = pygame.transform.scale(image,
                                (Preferences.BAR_WIDTH, val * Preferences.UNIT_HEIGHT))
        # Get the dimensions of the image
        image_rect = image.get_rect(topleft=(bar_x, bar_y))
        # Place the image on the screen
        self.screen.blit(image, image_rect)

        return image_rect

    def clear_screen(self) -> None:
        """ Reset the background of the screen """
        self.screen.fill(Preferences.BACKGROUND_COLOR)