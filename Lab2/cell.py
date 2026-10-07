"""
Author: Prof. Alyssa
Represents a single Cell on the Board.
You do NOT need to modify this file.
"""

from enum import Enum 

from preferences import Preferences

class Cell:    
    def __init__(self, row, col):
        # The row of this cell on the board
        self.__row = row            
        # The column of this cell on the board
        self.__col = col 
        # The current contents of this cell
        self.__cell_type = self.CellType.EMPTY 

    ###########################################
    # Access basic information about the cell #
    ###########################################

    def get_row(self) -> int:
        """ Get the row of this cell """
        return self.__row 
    
    def get_col(self) -> int:
        """ Get the column of this cell """
        return self.__col 
    
    def is_player(self) -> bool:
        """ Return whether or not this cell has the player """
        return self.__cell_type == self.CellType.PLAYER
    
    def is_empty(self) -> bool:
        """ Return whether or not this cell is empty """
        return self.__cell_type == self.CellType.EMPTY
    
    def is_food(self) -> bool:
        """ Return whether or not this cell is food """
        return self.__cell_type == self.CellType.FOOD
    
    def is_enemy(self) -> bool:
        """ Return whether or not this cell is an enemy """
        return self.__cell_type == self.CellType.ENEMY
    
    def get_color(self):
        """ Return the color associated with this type of cell """
        return {
            self.CellType.PLAYER : Preferences.COLOR_PLAYER,
            self.CellType.FOOD : Preferences.COLOR_FOOD,
            self.CellType.EMPTY : Preferences.COLOR_BACKGROUND,
            self.CellType.ENEMY : Preferences.COLOR_ENEMY
        }.get(self.__cell_type)
    
    ###########################################
    # Modify basic information about the cell #
    ###########################################
    
    def become_player(self) -> None:
        """ Change this cell type to the player """
        self.__cell_type = self.CellType.PLAYER
    
    def become_food(self) -> None:
        """ Change this cell type to food """
        self.__cell_type = self.CellType.FOOD

    def become_empty(self) -> None:
        """ Change this cell type to empty """
        self.__cell_type = self.CellType.EMPTY 

    def become_enemy(self) -> None:
        """ Change this cell type to an enemy """
        self.__cell_type = self.CellType.ENEMY

    
    ##############################
    # Helper methods for testing #
    ##############################

    def __str__(self):
        """ Specify the string representation of the cell.
            Formats as '[row, col, CellType]' """
        return "[{}, {}, {}]".format(self.__row, self.__col, self.__cell_type.value)

    class CellType(Enum):
        """ An enumeration (enum) representing the possible types of cells
            and their string representations. Using an enum ensures that we 
            do not accidentally assign an invalid type to a cell.
        """
        PLAYER = 'P'
        EMPTY = ' '
        FOOD = 'o'
        ENEMY = 'x'