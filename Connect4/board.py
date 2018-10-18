import numpy as np

class Board(object):
    """description of class"""
    def __init__( self ):
        self.board = np.zeros( [ 6, 7 ] ).astype(int)

    def __str__( self ):
        return '\n' + self.board[::-1].__str__()

    def _getRow( self, rowNum ):
        return self.board[ rowNum, : ]

    def _getCol( self, colNum ):
        return self.board[ :, colNum ]

    def getHeight( self, colNum ):
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
        if colNum < 0 or colNum > 6:
            return -1
        height = self.getHeight( colNum )
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

    def _rowSubVecGenerator( self ):
        for rowIdx in range( 6 ):
            for colIdx in range( 4 ):
                yield self._getSubRow( rowIdx, colIdx )

    def _colSubVecGenerator( self ):
        for rowIdx in range( 3 ):
            for colIdx in range( 7 ):
                yield self._getSubCol( rowIdx, colIdx )

    def _diag1SubVecGenerator( self ):
        for rowIdx in range( 3 ):
            for colIdx in range( 4 ):
                yield self._getSubDiag1( rowIdx, colIdx )

    def _diag2SubVecGenerator( self ):
        for rowIdx in range( 3 ):
            for colIdx in range( 4 ):
                yield self._getSubDiag2( rowIdx, colIdx )

    def _subVecGenerator( self ):
        for row in self._rowSubVecGenerator():
            yield row

        for col in self._colSubVecGenerator():
            yield col

        for diag1 in self._diag1SubVecGenerator():
            yield diag1

        for diag2 in self._diag2SubVecGenerator():
            yield diag2

    @staticmethod
    def _checkSubVec( subVec ):
        for val in [ 1, 2 ]:
            if subVec.max() == val and subVec.min() == val:
                return val
        return 0

    def check( self ):
        for subVec in self._subVecGenerator():
            r = self._checkSubVec( subVec )
            if r in [ 1, 2 ]:
                return r
        return 0

    def isFull( self ):
        for colNum in range( 7 ):
            if not ( self.getHeight( colNum ) == 6 ):
                return False
        return True


