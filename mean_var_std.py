import numpy as np

def calculate(lists):
    if len(lists) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the list into a 3x3 numpy array
    matrix = np.array(lists).reshape(3, 3)
    
    # Calculate mean, variance, standard deviation, max, min, and sum
    mean = [list(np.mean(matrix, axis=0)), list(np.mean(matrix, axis=1)), np.mean(matrix)]
    variance = [list(np.var(matrix, axis=0)), list(np.var(matrix, axis=1)), np.var(matrix)]
    std_dev = [list(np.std(matrix, axis=0)), list(np.std(matrix, axis=1)), np.std(matrix)]
    max_val = [list(np.max(matrix, axis=0)), list(np.max(matrix, axis=1)), np.max(matrix)]
    min_val = [list(np.min(matrix, axis=0)), list(np.min(matrix, axis=1)), np.min(matrix)]
    sum_val = [list(np.sum(matrix, axis=0)), list(np.sum(matrix, axis=1)), np.sum(matrix)]
    
    # Create the dictionary
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }
    
    return calculations

