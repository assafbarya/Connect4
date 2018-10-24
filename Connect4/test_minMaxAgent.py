import unittest
from board import Board
from minMaxAgent import MinMaxAgent

class Test_test_minMaxAgent( unittest.TestCase ):
    def test_Win1( self ):
        b = Board()
        a = MinMaxAgent( 1, 1 )
        b.add( 1, 0 )
        b.add( 1, 1 )
        b.add( 1, 2 )
        a.update( b, 'reward' )
        self.assertEqual( a.getAction(), 3 )

    def test_Win2( self ):
        b = Board()
        a = MinMaxAgent( 1, 1 )
        b.add( 1, 0 )
        b.add( 1, 0 )
        b.add( 1, 0 )
        a.update( b, 'reward' )
        self.assertEqual( a.getAction(), 0 )

    def test_Win3( self ):
        '''
        0000000
        0000000
        2000000
        1200000
        1120000
        1110000
        '''
        b = Board()
        for col in range( 3 ):
            for _times in range( 3 - col ):
                b.add( 1, col )

        for col in range( 3 ):
            b.add( 2, col )

        a = MinMaxAgent( 1, 1 )
        a.update( b, 'reward' )
        self.assertEqual( a.getAction(), 3 )

    def test_Win4( self ):
        '''
        0000000
        0000000
        2000000
        1200000
        1100000
        1112000
        '''
        b = Board()
        for col in range( 3 ):
            for _times in range( 3 - col ):
                b.add( 1, col )
        b.add( 2, 0 )
        b.add( 2, 1 )
        b.add( 2, 3 )
        a = MinMaxAgent( 2, 1 )
        a.update( b, 'reward' )
        self.assertEqual( a.getAction(), 2 )

    def test_Win5( self ):
        '''
        0000000
        0000000
        0000000
        0000000
        0000000
        0101000
        '''
        b = Board()
        b.add( 1, 1 )
        b.add( 1, 3 )
        a = MinMaxAgent( 1, 3 )
        a.update( b, 'reward' )
        self.assertEqual( a.getAction(), 2 )


    def test_DontLose( self ):
        b = Board()
        a = MinMaxAgent( 1, 2 )
        b.add( 2, 0 )
        b.add( 2, 1 )
        b.add( 2, 2 )
        a.update( b, 'reward' )
        self.assertEqual( a.getAction(), 3 )

    def test_DontLose2( self ):
        '''
        0000000
        0000000
        2000000
        1200000
        1100000
        1112000
        '''
        b = Board()
        for col in range( 3 ):
            for _times in range( 3 - col ):
                b.add( 1, col )
        b.add( 2, 0 )
        b.add( 2, 1 )
        b.add( 2, 3 )
        a = MinMaxAgent( 1, 2 )
        a.update( b, 'reward' )
        self.assertEqual( a.getAction(), 2 )

    def test_DontLose3( self ):
        '''
        0000000
        0000000
        0000000
        0000000
        0000000
        0101000
        '''
        b = Board()
        b.add( 1, 1 )
        b.add( 1, 3 )
        a = MinMaxAgent( 2, 4 )
        a.update( b, 'reward' )
        self.assertIn( a.getAction(), [ 0, 2, 3 ] )

    def test_DontLose4( self ):
        '''
        0000000
        0000000
        1000000
        2010000
        2111000
        2221000
        inevitable loss
        '''
        b = Board()
        moves = [ ( 2, 0 ), ( 2, 0 ), ( 2, 0 ), ( 1, 0 ), 
                  ( 2, 1 ), ( 1, 1 ),
                  ( 2, 2 ), ( 1, 2 ), ( 1, 2 ),
                  ( 1, 3 ), ( 1, 3 ) ]
        for color, column in moves:
            b.add( color, column )
        a = MinMaxAgent( 2, 4 )
        a.update( b, 'reward' )
        self.assertIn( a.getAction(), [ 0,1,2,3,4,5,6 ] )

if __name__ == '__main__':
    unittest.main()
