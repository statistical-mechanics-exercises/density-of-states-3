# The density of magnetisations

In the previous exercise you worked out how to compute the __density of states__ for our Ising model.  This was nothing more than a bar chart which showed how many microstates have each of the possible values for the energy.  In this exercise we are going to do something similar but now we will look at the fraction of the total number of microstates many that have each of the possible values for the magnetisation.  

As in the previous exercise we are going to consider a system of 8 Ising spins.  As the magnetisation is just the sum of the spin coordinates the lowest value this quantity can take is -8 and the highest value is 8.  We will thus create a list called `fraction_of_microstates` containing 17 elements.  The first element in this list will tells us the fraction of microstates that have a magnetisation of -8,  the second will tell us the fraction of microstates that have a magnetisation of -7, the third will tell us the fraction of microstates that have a mangnetisation of -6 and so on.  We will calculate the numbers in this list using:

![](https://render.githubusercontent.com/render/math?math=P(M_i)=\frac{1}{M}\sum_{j=1}^M\delta(M(\mathbf{X}_j)-M_i)\quad\textrm{where}\quad\delta(0)=1\quad\delta(x)=0\quad\textrm{if}\quad\x\ne\1)

In this expression the sum runs over all the microstates and ![](https://render.githubusercontent.com/render/math?math=M(\mathbf{x}_j)) is the magnetisation of microstate ![](https://render.githubusercontent.com/render/math?math=\mathbf{x}_j), which remember is just the sum of the spins.  To complete the code in the box on the left you will need to write a function called `magnetisation`, which calculate the magnetisation from the microscopic coordinates for the spins.

Once you have written the function to calculate the magnetisation you will need to write the code to generate every possible microstate the spins can adopt.  You will need to use your `magnetisation` function to evaluate the magnetisation for each of these microstates and you will then need to update the appropriate element of the list called `fraction_of_microstates` to reflect the fact that you have found an additional configuration that has this particular magnetisation.

Last but not least you will need to normalise the list called `fraction_of_microstates` so that it contains the fraction of the microstates that have each of the particular values for the magnetisation rather than the number of microstates that have these values.

Once you have completed the exercise a graph will be produced showing the various values of magnetisation against the number of microstates that have each of the possible values for the magnetisation. 
