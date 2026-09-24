import torch
import torch.nn as nn

def train_neuron(features: torch.Tensor, labels: torch.Tensor, initial_weights: torch.Tensor, initial_bias: float, learning_rate: float, epochs: int) -> tuple[list[float], float, list[float]]:
    """
    Simulates a single neuron with sigmoid activation and trains it using
    backpropagation with MSE loss via SGD.

    Args:
        features: Input feature tensor of shape (n_samples, n_features)
        labels: Binary label tensor of shape (n_samples,)
        initial_weights: Initial weight tensor of shape (n_features,)
        initial_bias: Initial bias scalar
        learning_rate: Learning rate for SGD
        epochs: Number of training epochs

    Returns:
        Tuple of (updated_weights, updated_bias, mse_values) all rounded to 4 decimal places
    """
    w = initial_weights
    b = initial_bias
    losses = []
    n = len(features)
    for _ in range(epochs):
        x = torch.matmul(features,w) + b
        y_hat = torch.sigmoid(x)

        loss = ((y_hat - labels)**2).mean()
        losses.append(round(loss.item(), 4))
        w_grad = torch.matmul(features.T,2/n * (y_hat-labels) * y_hat * (1-y_hat))
        b_grad = (2/n * (y_hat-labels) * y_hat * (1-y_hat)).sum()

        w -= learning_rate*w_grad
        b -= learning_rate*b_grad
    updated_weights = [round(val, 4) for val in w.tolist()]
    updated_bias = round(b.tolist(), 4)
    return (updated_weights, updated_bias, losses)