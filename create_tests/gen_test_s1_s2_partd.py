import numpy as np

def generate_vector(size):
    return np.random.randn(size).astype(np.float32)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    e_x = np.exp(x - np.max(x))  # Subtract max for numerical stability
    return e_x / e_x.sum()

def apply_probability_function(function_type, vector):
    if function_type == 0:
        return sigmoid(vector)
    elif function_type == 1:
        return softmax(vector)
    else:
        raise ValueError("Unsupported function type")

def save_vectors(original, transformed, filename):
    with open(filename, 'a') as file:
        file.write("Original Vector:\n")
        np.savetxt(file, original[np.newaxis], fmt="%f")
        file.write("Transformed Vector (Probabilities):\n")
        np.savetxt(file, transformed[np.newaxis], fmt="%f")
        file.write("\n")

def main():
    test_cases = [
        (0, 10),
        (1, 50),
        (0, 100),
    ]

    filename = 'vectors_and_probabilities.txt'

    # Clear the file initially
    open(filename, 'w').close()

    for idx, (function_type, size) in enumerate(test_cases):
        vector = generate_vector(size)
        probabilities = apply_probability_function(function_type, vector)
        save_vectors(vector, probabilities, filename)
        print(f"Test Case {idx+1} - Function Type: {'Sigmoid' if function_type == 0 else 'Softmax'}, Size: {size} - Saved to {filename}")

if __name__ == '__main__':
    main()
