speciesNames = ["B1", "B2", "B3", "B4", "M1", "M2", "M3", "M4"]

def printDistanceMatrix(matrix):
    print(len(matrix))
    for distanceList in matrix:
        print(speciesNames[matrix.index(distanceList)], end=" ")

        for distance in distanceList:
            print(distance, end=" ")
        print()
