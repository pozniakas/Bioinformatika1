import math

def calculateDistance(num1, num2):
    return math.pow((num1 - num2), 2)

def squareRoot(num1):
    return math.sqrt(num1)

def prepareDistanceMatrix(frequencies):
    matrix = [[0.0 for _ in range(8)] for _ in range(8)]
    for i in range(0, len(frequencies) - 1):
        for j in range(i + 1, len(frequencies)):
            counter = 0.0
            for k in range(len(frequencies[i])):
                counter += calculateDistance(frequencies[i][k], frequencies[j][k])
            matrix[i][j] = squareRoot(counter)
            matrix[j][i] = matrix[i][j]
    return matrix