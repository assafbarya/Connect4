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

    def _getSubRow( self, rowIdx, colIdx ):
        return self.board[ rowIdx, colIdx : ( colIdx + 4 ) ]

    def _getSubCol( self, rowIdx, colIdx ):
        return self.board[ rowIdx : ( rowIdx + 4 ), colIdx ]

    def _getSubDiag1( self, rowIdx, colIdx ):
        return np.diag( self.board[ rowIdx : ( rowIdx + 4 ), colIdx : ( colIdx + 4 ) ] )

    def _getSubDiag2( self, rowIdx, colIdx ):
        return np.diag( np.fliplr( self.board[ rowIdx : ( rowIdx + 4 ), colIdx : ( colIdx + 4 ) ] ) )

    def _rowSubColGenerator( self ):
        for rowIdx in range( 6 ):
            for colIdx in range( 4 ):
                yield self._getSubRow( rowIdx, colIdx )

    def _colSubColGenerator( self ):
        for rowIdx in range( 3 ):
            for colIdx in range( 7 ):
                yield self._getSubCol( rowIdx, colIdx )

    def _diag1SubColGenerator( self ):
        for rowIdx in range( 3 ):
            for colIdx in range( 4 ):
                yield self._getSubDiag1( rowIdx, colIdx )

    def _diag2SubColGenerator( self ):
        for rowIdx in range( 3 ):
            for colIdx in range( 4 ):
                yield self._getSubDiag2( rowIdx, colIdx )

    def _subColGenerator( self ):
        for row in self._rowSubColGenerator():
            yield row

        for col in self._colSubColGenerator():
            yield col

        for diag1 in self._diag1SubColGenerator():
            yield diag1

        for diag2 in self._diag1SubColGenerator():
            yield diag2



        






def main():
    b = Board()
    for i in range (6):
        for j in range(7):
            b.board[i,j] = i*7+j

    for c in b._subColGenerator():
        print (c)

    print (b)

    #for x in range(10):
    #    column = int( input('enter column') )
    #    color = int( input('enter color') )
    #    b.add( color, column )
    #    print (b)














main()