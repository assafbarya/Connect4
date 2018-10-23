import unittest
from board import Board

class Test_board( unittest.TestCase ):
    def test_getHeight( self ):
        for col in range( 7 ):
            for height in range( 6 ):
                b = Board()
                for _ in range( height ):
                    b.add( 1, col )
                self.assertEqual( b.getHeight( col ), height )

    def test_check_diag( self ):
        '''
        0000000
        0000000
        2000000
        1200000
        1120000
        1112000
        '''
        b = Board()
        for col in range( 3 ):
            for _times in range( 3 - col ):
                b.add( 1, col )

        self.assertEqual( b.check(), 0 )

        for col in range( 4 ):
            b.add( 2, col )
        self.assertEqual( b.check(), 2 )





        
if __name__ == '__main__':
    unittest.main()
