import numpy as np
from scipy import signal

def save_matrix_to_file(matrix, filename,nl="\n"):
    """Save the matrix to a space-separated text file."""
    np.savetxt(filename, matrix, fmt='%f', newline=nl)

# Set seed for reproducibility
np.random.seed(0)

# Generate medium size matrix and kernels
A = np.random.rand(25, 25).astype(np.float32)
K1 = np.random.rand(3, 3).astype(np.float32)
K2 = np.random.rand(7, 7).astype(np.float32)

# Save matrices to files
save_matrix_to_file(A, 'medium_matrix_25x25.txt',' ')
save_matrix_to_file(K1, 'small_kernel_3x3_25.txt', ' ')
save_matrix_to_file(K2, 'large_kernel_7x7_25.txt', ' ')

# Function to perform convolution
def perform_convolution(input_matrix, kernel):
    return signal.convolve2d(input_matrix, kernel, mode='valid')

# Compute convolution for both kernels
output_small_kernel = perform_convolution(A, K1)
output_large_kernel = perform_convolution(A, K2)

# Save output matrices to files
save_matrix_to_file(output_small_kernel, 'output_small_kernel_25.txt')
save_matrix_to_file(output_large_kernel, 'output_large_kernel_25.txt')
