from agentInterface import AgentInterface
import numpy as np
from keras import Sequential
from keras.layers import InputLayer, Dense

class RLAgent( AgentInterface ):
    """description of class"""

    def __init__(   self, 
                    actionSelector,
                    discountFactor = 0.95 ):

        self.discountFactor = discountFactor
        self.model          = Sequential()

        self.model.add( InputLayer( batch_input_shape = ( 6, 7 ) ) )
        self.model.add( Dense( 100, activation = 'sigmoid' ) )
        self.model.add( Dense( 100, activation = 'sigmoid' ) )
        self.model.add( Dense( 7, activation = 'linear' ) )
        self.model.compile( loss = 'mse', optimizer = 'adam', metrics = [ 'mae' ] )

        self.board          = np.zeros( [ 6, 7 ] ).astype(int)
        self.actionSelector = actionSelector
        
    def getAction( self ):
        action          = self.actionSelector.getAction( self.model.predict( self.board ) )
        self.lastAction = action
        return action


    def update( self, nextState, reward ):
        target                        = reward + self.discountFactor * np.max( self.model.predict( nextState ) )
        target_vec                    = self.model.predict( self.board )[ 0 ]
        target_vec[ self.lastAction ] = target
        target_vec                    = target_vec.reshape( -1, 7 )

        self.model.fit( self.board, target_vec, epochs = 1, verbose = 0 )
        self.board = nextState

