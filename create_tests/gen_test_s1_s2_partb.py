import numpy as np

def generate_matrix(n, m):
    return np.random.rand(n, m).astype(np.float32)

def relu(x):
    return np.maximum(0, x)
def tanh(x):
    return np.tanh(x)

def apply_activation(activation_type, matrix):
    if activation_type == 0:
        return relu(matrix)
    elif activation_type == 1:
        return tanh(matrix)
    else:
        raise ValueError("Unsupported activation type")
    
def save_matrix(matrix, filename,nl="\n"):
    np.savetxt(filename, matrix, fmt='%f', newline=nl)
    
def main():
    test_cases = [
        (0, 10, 10),  # Small matrix with ReLU
        (1, 50, 50),  # Medium matrix with tanh
        (0, 100, 100)  # Large matrix with ReLU
    ]
    
    for idx, (activation_type, n, m) in enumerate(test_cases):
        matrix = generate_matrix(n, m)
        save_matrix(matrix,f'activation_{idx}_size_{n}x{m}.txt'," ")
        activated_matrix = apply_activation(activation_type, matrix)
        filename = f'activation_{idx}_type_{activation_type}_size_{n}x{m}.txt'
        save_matrix(activated_matrix, filename)
        print(f"Results saved to {filename}")

if __name__ == '__main__':
    main()        