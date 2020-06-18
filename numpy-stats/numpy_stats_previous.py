import numpy as np


def calculate(list):
    if(len(list) != 9):
        return 'List must contain nine numbers.'

    matrix = np.array(list).reshape(3, 3)

    mean = []
    mean.append(np.mean(matrix, axis=0).tolist())
    mean.append(np.mean(matrix, axis=1).tolist())
    mean.append(np.mean(matrix))

    variance = []
    variance.append(np.var(matrix, axis=0).tolist())
    variance.append(np.var(matrix, axis=1).tolist())
    variance.append(np.var(matrix))

    standard_deviation = []
    standard_deviation.append(np.std(matrix, axis=0).tolist())
    standard_deviation.append(np.std(matrix, axis=1).tolist())
    standard_deviation.append(np.std(matrix))

    dictionary = {
        "mean": mean,
        "variance": variance,
        "standard deviation": standard_deviation
    }
    return dictionary
