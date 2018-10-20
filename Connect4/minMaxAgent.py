from agentInterface import AgentInterface
import pandas as pd
import numpy as np
import random

class MinMaxAgent( AgentInterface ):
    """minMax agent"""

    @staticmethod
    def _otherColor( color ):
        return ( ( color % 2 ) + 1 )

    @classmethod
    def _getActionScores( cls, board, myNum, isMyTurn, depthLeft ):
        legalMoves  = cls._getLegalMoves( board )
        movesScores = pd.Series( index = legalMoves )
        for move in legalMoves:
            newBoard            = board.make_copy()
            num                 = myNum if isMyTurn else cls._otherColor( myNum  )
            newBoard.add( num, move )
            turn                = not isMyTurn
            depth               = depthLeft - 1
            movesScores[ move ] = cls._evalBoard( newBoard, myNum, turn, depth )
        return movesScores
     
    @classmethod
    def _evalBoard( cls, board, myNum, isMyTurn, depthLeft ):
        res = board.check()
        if res == myNum:
            return 1
        if res == cls._otherColor( myNum ):
            return -1
        if depthLeft == 0:
            return 0

        if board.isFull():
            return 0

        movesScores = cls._getActionScores( board, myNum, isMyTurn, depthLeft )
        func = max if isMyTurn else min
        return func( movesScores )
 
    def __init__( self, number, depth ):
        self.board = None
        self.number = number
        self.depth = depth

    def description( self ):
        return 'MinMax Agent'

    @staticmethod
    def _getLegalMoves( board ):
        legalMoves  = []
        for move in range( 7 ):
            if board.getHeight( move ) < 6:
                legalMoves.append( move )
        return legalMoves

    def getAction( self ):
        if not self.board:
            return np.random.randint( 7 )

        isMyTurn = True
        movesScores = self._getActionScores( self.board, self.number, isMyTurn, self.depth )
        
        if movesScores.std() == 0.:
            return random.choice( movesScores.index )
        
        return movesScores.idxmax()

    def update( self, nextState, _reward ):
        self.board = nextState



