from MathUtils import prepareDistanceMatrix
from BioUtils import filterCodingSequences, findCodonFrequencies, findDicodonFrequencies
from PrintUtils import printDistanceMatrix

bacterialFileNames = ["bacterial1.fasta", "bacterial2.fasta", "bacterial3.fasta", "bacterial4.fasta"]
mamalianFileNames = ["mamalian1.fasta", "mamalian2.fasta", "mamalian3.fasta", "mamalian4.fasta"]

codonFrequencies = []
dicodonFrequencies = []

for bacterial in bacterialFileNames:
    codingSequences = filterCodingSequences("data/" + bacterial)
    codonFrequencies.append(findCodonFrequencies(codingSequences))
    dicodonFrequencies.append(findDicodonFrequencies(codingSequences))

for mamalian in mamalianFileNames:
    codingSequences = filterCodingSequences("data/" + mamalian)
    codonFrequencies.append(findCodonFrequencies(codingSequences))
    dicodonFrequencies.append(findDicodonFrequencies(codingSequences))

printDistanceMatrix(prepareDistanceMatrix(codonFrequencies))
printDistanceMatrix(prepareDistanceMatrix(dicodonFrequencies))