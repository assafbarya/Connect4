from board import Board

def main():

    b = Board()
    color = 1
    while (1):
        column = int( input('enter column') )
        r = b.add( color, column )
        if -1 == r:
            print ('error')
            break

        r = b.check()
        print (b)
        if r in [ 1, 2 ]:
            print ('{} won'.format(r))
            break
        
        color = ( color % 2 ) + 1


            















main()