import matplotlib.pyplot as plt 
import numpy as np 

def magnetisation( spins ) :
  mag = 0
  # Your code to calculate the magnetisation goes here
  
  return mag
  
# Create a list of the posssible values the magnetisation can take
magnetisations = 17*[0]
for i in range(17) : magnetisations[i] = -8+i

# Create a list that will hold the number of microstates with each magnetisation 
fraction_of_microstates = 17*[0]
# Your code to do the loop over all the microstates and to count how many times each 
# of the magnetisation values appear goes here

  
# This will plot the energies of the configurations against their numerical indexes. 
plt.bar( magnetisations, fraction_of_microstates, width=0.1 )
plt.xlabel("magnetisation")
plt.ylabel("Fraction of configurations")
plt.savefig( "density_of_mag.png" )
