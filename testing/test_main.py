import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_magnetisation(self) : 
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
                spins[j] = np.floor( num / 2**(4-j) )
                num = num - spins[j]*2**(4-j)
                if spins[j]==0 : spins[j] = -1
            self.assertTrue( magnetisation( spins )==sum(spins), "The function for evaluating the magnetisation is incorrect" )
            
    def test_graph(self) :
        counts = 17*[0]
        for i in range(2**8) :
            num, spins = i, 8*[0]
            for j in range(8) :
                spins[j] = np.floor( num / 2**(7-j) )
                num = num - spins[j]*2**(7-j)
                if spins[j]==0 : spins[j] = -1
            binn = int( magnetisation(spins)  + 8 ) 
            counts[binn] = counts[binn] + 1
  
        for i in range(17) : counts[i] = counts[i] / (2**8)
  
        fighand=plt.gca()
        for k in range(17) :
            patch = fighand.patches[k]
            self.assertTrue( np.abs( patch.get_xy()[0] + 0.5*patch.get_width() - (-8+k) )<1e-7, "The graph showing the magnetisations is incorrect" )
            self.assertTrue( np.abs(patch.get_height() - counts[k] )<1e-7, "The graph showing the magnetisations is incorrect" )
