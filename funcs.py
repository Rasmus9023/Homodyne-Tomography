import numpy as np
import math as mt
import cmath as cm
import scipy as sp

#### **Random sample generation**

def Rsamp(arr, lnspcfnc):
    """
    Generates a rejection sample using a desired line spacing
    
    ------------------------------------------------------------

    arr : an array containing the given histogram values
    lnspcfnc : the x-axis grid size of span(-lnspcfnc;lnspcfnc)

    ------------------------------------------------------------

    Returns a sample of dimension lnspcfnc with values of 
    """
    maxval = max(arr)
    Ry = np.random.uniform(0,maxval,200)
    xgrid = np.linspace(-lnspcfnc,lnspcfnc,200)
    indices = np.where(arr>Ry)
    Rsample = xgrid[indices]
    
    return Rsample

# For loop for iteration; maybe change (avoid for-loops)




# Ignore this function as it does not correlate with the function inputs for eq. (1) of Lvovsky
# I still keep it as it can create a lot of samples fast
# (BUT DONT USE IT WITH THE FORMULA eq. (1))

def RepRsamp(iter,arr,lnspcfnc):
    """ 
    Generates a rejection sample of any number of iterations

    ----------------------------------------------------------
    
    iter : the number of iterations
    arr : an array containing the given histogram values
    lnspcfnc : the x-axis grid size of span(-lnspcfnc;lnspcfnc)
    """
    RsampIter = np.array([])
    for i in range(iter):
        RsampIter = np.append(RsampIter,Rsamp(arr,lnspcfnc))
    return RsampIter



#### **Below is the likelyhood-function, eq. (1) of Lvovsky as well as the overlap function eq. (8)**

#### **CreateMatrixOverlap was used before I realized that the overlap-function could have vectorize() as a decorator**

# Definition of the likelyHood-function

def likelyHood(pr,f):
    """
    Likelyhood-function (eq. 1 of Lvovsky et. al.)
    
    -------------------------------------------------------------------------

    pr : array of prj values (probability values)
    f : array of fj values (number of occurences for each observation)

    -------------------------------------------------------------------------

    Returns a value in range [0;1]
    """
    product = 1.
    for j in range(len(f)):
        product *= pr[j]**f[j]
#        print(product) #If debugging
    return product

# Overlap function defined as eq. 8 in the paper

@np.vectorize
def overlap(n,theta_indx,x):
    """
    Overlap of two states (see eq. 8 of Lvovsky et. al.)

    ----------------------------------------------------

    n : index of density operator
    x : observation value (or yj values)
    theta_index : index of theta values (e.g. in list [0,30,60,90,120,150])

    ----------------------------------------------------

    Returns a float value of overlap
    """
    thetas = [0,30*mt.pi/180,60,90,120,150]
    thetas = [i**mt.pi/180 for i in thetas]
    theta = thetas[theta_indx]
    hermit = sp.special.hermite(n)
    overl = cm.exp(1j * n * theta) * (2./mt.pi)**(1/4) * hermit(mt.sqrt(2)*x) \
            /(mt.sqrt(2**n * mt.factorial(n)))*mt.exp(-x**2)
    return overl

# Creates (help)matrices to calculate the overlap

# These are not used as we vectorize the overlap function

def projector(theta, x, max_photon=19):

    pass

def CreateMatrixOverlap(rows,cols,theta_indx,yjs):
    """
    Creates a matrix with with elements given by the overlap function
    The function works as a help-function to derive values without making a nested for-loop
    
    -----------------------------------------------------------------

    rows : number of rows
    cols : number of columns
    theta_indx : index of theta values (e.g. in list [0,30,60,90,120,150])
    yjs : list of observations

    -----------------------------------------------------------------
    
    Returns a matrix of dim (rows,cols)
    """
    # This function could and should be optimized, but for now it's functional and I understand it

    M = np.ones((rows,cols))

    # If we have more columns than rows it means that we initialize each row element as an overlap element

    if cols > rows:
        for i in range(rows):
            for j in range(cols):
                M[i,j] = overlap(j,theta_indx,yjs[i])

    # If we have more rows than columns it means that we initialize each column element as an overlap element

    else:
        for i in range(cols):
            for j in range(rows):
                M[j,i] = overlap(j,theta_indx,yjs[i])

    return M