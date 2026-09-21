import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:
    n = predicted_probs.shape[0]
    total = 0
    for i in range(n):
        for j in range(predicted_probs[i].size):
            if true_labels[i][j] == 1:
              total += true_labels[i][j]*np.log(predicted_probs[i][j]+epsilon)

    avg = -1/n*total
    return avg