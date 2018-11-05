from actionSelectorInterface import ActionSelectorInterface
import numpy as np

class EpsGreedySelector( ActionSelectorInterface ):
    """description of class"""

    def __init__( self, eps = 0.9, decay = 1 ):
        self.eps   = eps  ## epsilon greedy coefficient
        self.decay = decay ## decay of the epsilon greedy

    def getAction( self, actionValues ):
        beGreedy                      = ( np.random.rand() > self.eps ) and ( actionValues.var() > 0 )
        self.eps                     *= self.decay
        if beGreedy: 
            action                    = actionValues.argmax()
        else: 
            action                    = np.random.randint( actionValues.size )

        return action



