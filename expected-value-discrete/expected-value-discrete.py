import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x=np.asarray(x)
    p=np.asarray(p)
    if not np.isclose(p.sum(), 1.0):
        raise ValueError("Probabilities must sum to 1")
    return float(np.sum(x*p))
    pass
