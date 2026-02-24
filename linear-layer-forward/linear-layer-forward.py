def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    n_samples = len(X)
    d_in = len(X[0]) if n_samples > 0 else 0
    d_out = len(b)
    
    # Initialize output as list of lists (n_samples x d_out)
    y = [[0.0 for _ in range(d_out)] for _ in range(n_samples)]
    
    # For each sample
    for i in range(n_samples):
        # For each output neuron
        for j in range(d_out):
            # Compute weighted sum: sum over k (X[i][k] * W[k][j])
            weighted_sum = 0.0
            for k in range(d_in):
                weighted_sum += X[i][k] * W[k][j]
            # Add bias
            y[i][j] = weighted_sum + b[j]
    
    return y