import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("A lista deve conter nove números")
    
    matrix = np.array(numbers).reshape(3, 3)
    
    def to_list(arr):
        return arr.astype(float).tolist()
    
    calculations = {
        'mean': [to_list(matrix.mean(axis=0)),
                 to_list(matrix.mean(axis=1)),
                 float(matrix.mean())],
        'variance': [to_list(matrix.var(axis=0)),
                     to_list(matrix.var(axis=1)),
                     float(matrix.var())],
        'standard deviation': [to_list(matrix.std(axis=0)),
                               to_list(matrix.std(axis=1)),
                               float(matrix.std())],
        'max': [to_list(matrix.max(axis=0)),
                to_list(matrix.max(axis=1)),
                int(matrix.max())],
        'min': [to_list(matrix.min(axis=0)),
                to_list(matrix.min(axis=1)),
                int(matrix.min())],
        'sum': [to_list(matrix.sum(axis=0)),
                to_list(matrix.sum(axis=1)),
                float(matrix.sum())]
    }
    
    return calculations
