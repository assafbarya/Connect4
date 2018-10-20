from board import Board
import logging

class Env( object ):
    """connect4 environment"""
    def _createLogger( self, level ):
        self.logger = logging.getLogger( 'Connect4' )
        self.logger.setLevel( level )
        self.ch = logging.StreamHandler()
        self.ch.setLevel( level )
        formatter = logging.Formatter( '%(asctime)s - %(name)s - %(levelname)s - %(message)s' )
        self.ch.setFormatter( formatter )
        self.logger.addHandler( self.ch )

    def __init__( self, agent1, agent2, loggingLevel ):
        self.agents = [ agent1, agent2 ]
        self.board  = Board()
        self._createLogger( loggingLevel )

    def __del__( self ):
        self.logger.removeHandler( self.ch )

    @staticmethod
    def _nextTurn( agentIdx ):
        return ( agentIdx + 1 ) % 2 

    @staticmethod
    def _idxToNum( agentIdx ):
        return agentIdx + 1

    def play( self ):
        finished = False
        agentIdx = 0
        while not finished:
            if self.board.isFull():
                self.logger.info( 'game ended in draw' )
                break
            action = self.agents[ agentIdx ].getAction()
            self.logger.debug( 'player {} chose action {}'.format( agentIdx, action ) )
            res = self.board.add( self._idxToNum( agentIdx ), action )
            self.logger.debug( self.board.__str__() )
            if res == -1: ## agent made an illegal action
                self.agents[ agentIdx ].update( self.board, -1 )
                self.logger.info( 'player {} made an illegal move'.format( agentIdx ) )
                break
            didWin = self.board.check()
            if 0 != didWin: ## only the agent that did the last move can win
                self.agents[ agentIdx ].update( self.board, 1 )
                self.agents[ self._nextTurn( agentIdx ) ].update( self.board, -1 )
                self.logger.info( 'player {} won'.format( agentIdx ) )
                break

            for agent in self.agents:
                agent.update( self.board, 0 )

            agentIdx = self._nextTurn( agentIdx )



