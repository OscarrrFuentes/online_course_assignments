import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    timestep_rabpop = CURRENTRABBITPOP
    for i in range(timestep_rabpop):
        if random.random()<=1-(timestep_rabpop/MAXRABBITPOP) and CURRENTRABBITPOP < MAXRABBITPOP:
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    timestep_rabpop = CURRENTRABBITPOP
    timestep_foxpop = CURRENTFOXPOP
    for i in range(timestep_foxpop):
        if CURRENTRABBITPOP > 10 and random.random() <= timestep_rabpop/MAXRABBITPOP:
            CURRENTRABBITPOP -= 1
            if random.random() <= 1/3:
                CURRENTFOXPOP += 1
        else:
            if random.random() <= 9/10 and CURRENTFOXPOP > 10:
                CURRENTFOXPOP -= 1
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabpops = []
    foxpops = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabpops.append(CURRENTRABBITPOP)
        foxpops.append(CURRENTFOXPOP)
    return (rabpops, foxpops)


pops = runSimulation(200)
pylab.plot(pops[0], label = 'rabbits')
pylab.plot(pops[1], label = 'foxes')
pylab.legend(loc = 'best')
pylab.show()
pylab.close()
rab_coeff = pylab.polyfit(range(200), pops[0], 2)
fox_coeff = pylab.polyfit(range(200), pops[1], 2)
pylab.plot(pylab.polyval(rab_coeff, range(200)))
pylab.title('Rabbits')
pylab.show()
pylab.close()
pylab.plot(pylab.polyval(fox_coeff, range(200)))
pylab.title('Foxes')
pylab.show()
pylab.close()