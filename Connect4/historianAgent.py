
from agentInterface import AgentInterface
import numpy as np
from board import Board
from datetime import datetime
import pickle

class HistorianAgent(object):
    """description of class"""

    def __init__(   self ):

        self.reset()
        self.memory = []

    def __del__( self ):
        self.save()

    def getAction( self ):
        action          = np.random.randint( 7 )
        self.lastAction = action
        return action

    def _remember( self, state, action, reward ):
        self.memory.append( ( state, action, reward ) )

    def save( self ):
        t = datetime.now()
        file = open( 'c:\\work\\memories_{}_{}.pkl'.format( t.date(), t.time().microsecond ), 'wb' )
        pickle.dump( self.memory, file )

    def update( self, nextState, reward ):
        if ( self.lastAction is None ) or ( reward == 0 ):
            self.board = nextState.make_copy()
            return

        self._remember( self.board, self.lastAction, reward )

    def reset( self ):
        self.board          = Board()
        self.lastAction     = None
