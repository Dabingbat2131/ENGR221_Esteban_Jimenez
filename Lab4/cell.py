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

        # Whether this cell has been added to the search list
        self.added_to_search_list = False 

        # Where this cell came from when searching
        self.search_parent = None 


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
    
    def is_body(self) -> bool:
        """ Return whether or not this cell is part of the body """
        return self.__cell_type == self.CellType.BODY
    
    def is_empty(self) -> bool:
        """ Return whether or not this cell is empty """
        return self.__cell_type == self.CellType.EMPTY
    
    def is_food(self) -> bool:
        """ Return whether or not this cell is food """
        return self.__cell_type == self.CellType.FOOD
    
    def get_color(self):
        """ Return the color associated with this type of cell """
        return {
            self.CellType.PLAYER : Preferences.COLOR_PLAYER,
            self.CellType.BODY : Preferences.COLOR_BODY,
            self.CellType.FOOD : Preferences.COLOR_FOOD,
            self.CellType.EMPTY : Preferences.COLOR_BACKGROUND,
        }.get(self.__cell_type)
    

    ###########################################
    # Modify basic information about the cell #
    ###########################################
    
    def become_player(self) -> None:
        """ Change this cell type to the player """
        self.__cell_type = self.CellType.PLAYER

    def become_body(self) -> None:
        """ changes this cell type to the body """
        self.__cell_type = self.CellType.BODY
    
    def become_food(self) -> None:
        """ Change this cell type to food """
        self.__cell_type = self.CellType.FOOD

    def become_empty(self) -> None:
        """ Change this cell type to empty """
        self.__cell_type = self.CellType.EMPTY 


    ######################
    # Methods for search #
    ######################
    
    def set_added_to_search_list(self) -> None:
        """ Indicate that this cell has been added to the search list """
        self.added_to_search_list = True 

    def on_search_list(self) -> bool:
        """ Return whether or not this cell is on the search list """
        return self.added_to_search_list
    
    def set_search_parent(self, parent) -> None:
        """ Set the parent of this cell """
        self.search_parent = parent 

    def get_search_parent(self) -> None:
        """ Return the parent of this cell """
        return self.search_parent
    
    def clear_search_info(self) -> None:
        """ Reset the search attributes """
        self.added_to_search_list = False
        self.search_parent = None


    ##############################
    # Helper methods for testing #
    ##############################

    def __str__(self):
        """ Specify the string representation of the cell.
            Formats as 'CellType' """
        return self.__cell_type.value
    
    def parent_string(self):
        """ Format the parent of this cell, as a string """
        if self.__parent:
            return "[{}, {}]".format(self.search_parent.get_row(), 
                                     self.search_parent.get_col())


    class CellType(Enum):
        """ An enumeration (enum) representing the possible types of cells
            and their string representations. Using an enum ensures that we 
            do not accidentally assign an invalid type to a cell.
        """
        PLAYER = 'P'
        EMPTY = ' '
        FOOD = 'o'
        BODY = 'p'
