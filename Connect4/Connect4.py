import numpy as np
from enum import Enum

class Color( Enum ):
    EMPTY = 0
    BLACK = 1
    WHITER = 2

class Board:
    def __init__( self ):
        self.board = np.zeros( [ 6, 7 ] ).astype(int)

    def __str__( self ):
        return self.board[::-1].__str__()

    def _getRow( self, rowNum ):
        return self.board[ rowNum, : ]

    def _getCol( self, colNum ):
        return self.board[ :, colNum ]

    def _getHeight( self, colNum ):
        ''' return the lowest empty slot '''
        col = self._getCol( colNum )
        isEmpty = ( col == 0 )

        ## column is completely empty
        if True == isEmpty.min():
            return 0

        ## column is completely full
        if False == isEmpty.max():
            return 6

        ## returns the first index which is True
        return np.argmax( isEmpty )

    def add( self, color, colNum ):
        height = self._getHeight( colNum )
        if  height == 6:
            return -1
        self.board[ height, colNum ] = color
        return 0


        






def main():
    b = Board()
    for x in range(10):
        column = int( input('enter column') )
        color = int( input('enter color') )
        b.add( color, column )
        print (b)














main()