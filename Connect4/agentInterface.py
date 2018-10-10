import abc

class AgentInterface:
    ''' defines the interface that each agent has to implement '''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def description( self ):
        raise NotImplementedError()

    @abc.abstractmethod
    def getAction( self ):
        raise NotImplementedError()

    @abc.abstractmethod
    def update( self, nextState, reward ):
        raise NotImplementedError()

    @abc.abstractmethod
    def setState( self, state ):
        raise NotImplementedError()

    @abc.abstractmethod
    def getState( self ):
        raise NotImplementedError()


