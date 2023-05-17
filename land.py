import re
import math

class Land(object):
    def eval(self, listone):
        tokensone = listone.split()
        listar = list(map(int, tokensone))
        value = 0
        foundIslands = []
        # listar[0] has the row/column size n of the matrix,
        # listar[1], listar[2], ... denote the binary value of
        # each entry of the matrix. listar[j+(i-1)*n] denotes (i,j) entry
        # your code here, value is the answer
        for i in range(0, len(listar)):
            if listar[i] == 1 and i not in foundIslands:
                pass #

        return value
    
    def left(place):
        pass
    
    def left(place):
        pass
    def left(place):
        pass
    def left(place):
        pass

if __name__ == '__main__':
    calc = Land()
    calc.eval()