from agentInterface import AgentInterface
import numpy as np
from keras import Sequential
from keras.layers import InputLayer, Dense
from keras.optimizers import adam
from board import Board

class RLAgent( AgentInterface ):
    """description of class"""

    def __init__(   self, 
                    actionSelector,
                    weightsFile = None,
                    discountFactor = 0.95 ):

        self.discountFactor = discountFactor
        self.model          = Sequential()

        self.model.add( Dense( 100, input_shape = (42,), activation = 'relu', kernel_initializer='zeros' ) )
        self.model.add( Dense( 100, activation = 'relu', kernel_initializer='zeros' ) )
        self.model.add( Dense( 100, activation = 'relu', kernel_initializer='zeros' ) )
        self.model.add( Dense( 100, activation = 'relu', kernel_initializer='zeros' ) )
        self.model.add( Dense( 7, kernel_initializer='zeros' ) )
        #self.model.compile( sgd(lr=.02),'mse')
        self.model.compile( loss = 'mse', optimizer = 'adam' )

        if weightsFile:
            self.model.load_weights( weightsFile )
        self.reset()

        
        self.actionSelector = actionSelector
        

    def getAction( self ):
        action          = self.actionSelector.getAction( self.model.predict( self.board.asVector() ) )
        self.lastAction = action
        return action


    def update( self, nextState, reward ):
        if not self.lastAction:
            self.board = nextState.make_copy()
            return

        if reward == 0: ## if there's a non zero reward, that's the last move of the game and there's no discounting of future rewards
            target                    = self.discountFactor * np.max( self.model.predict( nextState.asVector() ) )
        else:
            target                    = reward
        target_vec                    = self.model.predict( self.board.asVector() )[ 0 ]
        target_vec[ self.lastAction ] = target
        target_vec                    = target_vec.reshape( -1, 7 )

        self.model.fit( self.board.asVector(), target_vec, epochs = 1, verbose = 0 )

        if reward == 0:
            self.board = nextState.make_copy()

    def reset( self ):
        self.board          = Board()
        self.lastAction     = None