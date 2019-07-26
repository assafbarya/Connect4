from agentInterface import AgentInterface
import numpy as np
from keras import Sequential
from keras.layers import InputLayer, Dense
from keras.optimizers import adam, sgd
from board import Board
from datetime import datetime
import pickle

class RLAgent( AgentInterface ):
    """description of class"""

    def __init__(   self, 
                    actionSelector,
                    memoryFileName = None,
                    discountFactor = 0.95 ):

        self.discountFactor = discountFactor
        self.model          = Sequential()

        self.model.add( Dense( 100, input_shape = (42,), activation = 'relu', kernel_initializer='zeros' ) )
        self.model.add( Dense( 100, activation = 'relu', kernel_initializer='zeros' ) )
        self.model.add( Dense( 100, activation = 'relu', kernel_initializer='zeros' ) )
        self.model.add( Dense( 100, activation = 'relu', kernel_initializer='zeros' ) )
        self.model.add( Dense( 7, kernel_initializer='zeros' ) )
        self.model.compile( sgd(lr=.2),'mse')
        #self.model.compile( loss = 'mse', optimizer = 'adam', metrics = [ 'mae' ] )

        if memoryFileName:
            inputs, targets = self._prepare_memory( memoryFileName )
            self.model.train_on_batch( inputs, targets )

        self.reset()
        
        self.actionSelector = actionSelector
        self.memory = []

    @staticmethod
    def _prepare_memory( memoryFileName ):
        memory = pickle.load( open( memoryFileName, 'rb' ) )
        memory_size = len( memory )
        inputs = np.zeros( ( memory_size, 42 ) )
        targets = np.zeros( ( memory_size, 7 ) )
        for i in range( memory_size ):
            state, action, reward = memory[ i ]
            inputs[ i ] = state.board.reshape( 1, -1 )
            targets[ i, action ] = reward 
        return inputs, targets

    def __del__( self ):
        #self.save()
        pass

    def getAction( self ):
        action          = self.actionSelector.getAction( self.model.predict( self.board.asVector() ) )
        self.lastAction = action
        return action

    def _remember( self, state, action, reward ):
        self.memory.append( ( state, action, reward ) )

    def save( self ):
        t = datetime.now()
        file = open( 'c:\\work\\memories_{}_{}.pkl'.format( t.date(), t.time().microsecond ), 'wb' )
        pickle.dump( self.memory, file )

    def update( self, nextState, reward ):
        return
        if self.lastAction is None:
            self.board = nextState.make_copy()
            return

        if reward == 0: ## if there's a non zero reward, that's the last move of the game and there's no discounting of future rewards
            #target                    = self.discountFactor * np.max( self.model.predict( nextState.asVector() ) )
            self.board = nextState.make_copy()
            return
        else:
            self._remember( self.board, self.lastAction, reward )

        #    target                    = reward
        #target_vec                    = self.model.predict( self.board.asVector() )[ 0 ]
        #target_vec[ self.lastAction ] = target
        #target_vec                    = target_vec.reshape( -1, 7 )

        #self.model.fit( self.board.asVector(), target_vec, epochs = 1, verbose = 0 )
        #return
        #if reward == 0:
        #    self.board = nextState.make_copy()

    def reset( self ):
        self.board          = Board()
        self.lastAction     = None