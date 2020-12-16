import matplotlib.pyplot as plt 
import numpy as np 

def magnetisation( spins ) :
  mag = 0
  # Your code to calculate the magnetisation goes here
  mag = sum(spins) 
  return mag
  
# Create a list of the posssible values the magnetisation can take
magnetisations = 17*[0]
for i in range(17) : magnetisations[i] = -8+i

# Create a list that will hold the number of microstates with each magnetisation 
fraction_of_microstates = np.zeros(17)
# Your code to do the loop over all the microstates and to count how many times each 
# of the magnetisation values appear goes here
for index in range(2**8) :
  spins, ind = 8*[0], index
  # Your code to convert the integer index to the corresponding spin coordinates goes here
  for i in range(8) :
      spins[i] = np.floor( index / 2**(7-i) )
      index = index - spins[i]*(2**(7-i))
      if spins[i]==0 : spins[i] = -1
  nbin = int( magnetisation(spins) ) + 8
  fraction_of_microstates[nbin] = fraction_of_microstates[nbin] + 1
  

fraction_of_microstates = fraction_of_microstates / 2**8
# This will plot the energies of the configurations against their numerical indexes. 
plt.bar( magnetisations, fraction_of_microstates, width=0.1 )
plt.xlabel("magnetisation")
plt.ylabel("Fraction of configurations")
plt.savefig( "density_of_mag.png" )
