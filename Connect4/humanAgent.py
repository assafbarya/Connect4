class HumanAgent(object):
    """description of class"""
    def getAction( self ):
        return int( input( 'Enter move' ) )

    def update( self, nextState, _reward ):
        print( nextState )


