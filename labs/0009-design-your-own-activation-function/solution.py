import numpy as np

def activation(x):
    '''
    Apply an activation function element-wise.
    
    Args:
        x: numpy array of any shape (raw neuron outputs)
    
    Returns:
        numpy array of same shape (activated outputs)
    
    Requirements:
        - Must be non-linear (not just returning x)
        - Must work on arrays of any shape
        - Must be deterministic
    '''
    # TODO: Implement your activation function
    
    """
    SiLU = x*sigma(x) where sigma(x) is its own sigmoid function

    gradient of SiLU is sigma(x) + x*sigma(x)*(1-sigma(x))

    """
    sigmoid = 1/(1+np.exp(-x))
    SiLU = x*sigmoid
    result = SiLU  # Replace with your activation
    
    return result
