import numpy as np

def save_matrix(matrix, filename,nl="\n"):
    np.savetxt(filename, matrix, fmt='%f', newline=nl)

def max_pooling(matrix, pool_size):
    N, M = matrix.shape
    N = N // pool_size * pool_size
    M = M // pool_size * pool_size
    matrix = matrix[:N, :M]
    return matrix.reshape(N // pool_size, pool_size, M // pool_size, pool_size).max(axis=(1, 3))

def avg_pooling(matrix, pool_size):
    N, M = matrix.shape
    N = N // pool_size * pool_size
    M = M // pool_size * pool_size
    matrix = matrix[:N, :M]
    return matrix.reshape(N // pool_size, pool_size, M // pool_size, pool_size).mean(axis=(1, 3))

def apply_pooling(pool_type, pool_size, matrix):
    if pool_type == 0:
        return max_pooling(matrix, pool_size)
    elif pool_type == 1:
        return avg_pooling(matrix, pool_size)
    else:
        raise ValueError("Unsupported pool type")
    
def generate_matrix(n):
    return np.random.rand(n, n).astype(np.float32)

def main():
    test_cases = [
        (0, 2, 10),  # Small matrix with max pooling
        (1, 4, 50),  # Medium matrix with avg pooling
        (0, 5, 100)  # Large matrix with max pooling
    ]

    for idx, (pool_type, pool_size, n) in enumerate(test_cases):
        matrix = generate_matrix(n)
        save_matrix(matrix,f'pooled_{idx}_poolsize_{pool_size}_size_{n}x{n}.txt'," ")
        pooled_matrix = apply_pooling(pool_type, pool_size, matrix)
        filename = f'pooled_{idx}_type_{pool_type}_poolsize_{pool_size}_size_{n}x{n}.txt'
        save_matrix(pooled_matrix, filename)
        print(f"Results saved to {filename}")

if __name__ == '__main__':
    main()
