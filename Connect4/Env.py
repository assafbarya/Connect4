from board import Board

class Env( object ):
    """description of class"""
    def __init__( self, agent1, agent2 ):
        self.agents = [ agent1, agent2 ]
        self.board  = Board()

    @staticmethod
    def _nextTurn( agentIdx ):
        return ( agentIdx % 2 ) + 1

    def play( self ):
        finished = False
        agentIdx = 0
        while not finished:
            if self.board.isFull():
                break
            action = self.agents[ agentIdx ].getAction()
            res = self.board.add( agentIdx, action )
            if res == -1: ## agent made an illegal action
                self.agents[ agentIdx ].update( self.board, -1 )
                break
            didWin = self.board.check()
            if 0 != didWin: ## only the agent that did the last move can win
                self.agents[ agentIdx ].update( self.board, 1 )
                self.agents[ self._nextTurn( agentIdx ) ].update( self.board, -1 )
                break

            agentIdx = self._nextTurn( agentIdx )



