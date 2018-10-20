from agentInterface import AgentInterface
import numpy as np

class RuleAbidingAgent( AgentInterface ):
    def __init__( self ):
        self.board = None

    def description( self ):
        return 'Rule Abiding Agent'

    def getAction( self ):
        if not self.board:
            return np.random.randint( 7 )
        else:
            legalMoves  = []
            for move in range( 7 ):
                if self.board.getHeight( move ) < 6:
                    legalMoves.append( move )
            moveIdx = np.random.randint( len( legalMoves ) )
            return legalMoves[ moveIdx ]

    def update( self, nextState, _reward ):
        self.board = nextState


