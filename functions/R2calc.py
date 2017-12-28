import numpy as np

def R2calc(Y, Yhat):
    """Function to determine the determination coefficient
    
    Parameters
    ------------
    Y: np.array
       Measured values
    Yhat: np.array
       Estimated values from the fit
       
    Returns
    ------------
    R2: float
        The coeficient of determination
    """
    ##Average of our measurements
    Ybar = np.mean(Y)
    
    #Sum Squared of residues
    SSres = np.sum((Y - Yhat)**2)
    #Total Sum Squared
    SStot = np.sum((Y - Ybar)**2)
    
    R2 = 1 - SSres / SStot
        
    return R2