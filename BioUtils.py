from MathUtils import calculateDistance, squareRoot
from Bio import SeqIO
from Bio.Seq import Seq

codons = "ARNDCEQGHILKMFPSTWYV"

def filterCodingSequences(filename):
    sequences = []
    for seq in SeqIO.parse(filename, "fasta"):
        for j in range(0, 3):
            if len(seq.seq[j:]) % 3 != 0:
                sequence = Seq(seq.seq[j:-(len(seq.seq[j:]) % 3)])
                sequences.append(sequence)
                sequences.append(sequence.reverse_complement())
            else:
                sequence = Seq(seq.seq[j:])
                sequences.append(sequence)
                sequences.append(sequence.reverse_complement())
    codingSequences = []
    for sequence in sequences:
        lastStopIndex = 0
        for k in range(0, len(sequence), 3):
            if k < lastStopIndex:
                continue
            if sequence[k:k + 3] == 'ATG':
                for j in range(k, len(sequence), 3):
                    if sequence[j:j + 3] == 'TAA' or sequence[j:j + 3] == 'TAG' or sequence[j:j + 3] == 'TGA':
                        if j + 3 - k >= 100:
                            codingSequences.append(sequence[k:j + 3].translate())
                        lastStopIndex = j + 3
                        break
    return codingSequences


def findCodonFrequencies(sequences):
    codonFrequencies = []
    for codon in codons:
        counter = 0
        sequencesLength = 0
        for sequence in sequences:
            sequencesLength += len(sequence)
            for k in range(len(sequence)):
                if sequence[k] == codon:
                    counter += 1
        codonFrequencies.append(counter / sequencesLength)
    return codonFrequencies


def findDicodonFrequencies(sequences):
    dicodonFrequencies = []
    for firstCodon in codons:
        for secondCodon in codons:
            counter = 0
            sequencesLength = 0
            for sequence in sequences:
                sequencesLength += len(sequence)
                for k in range(len(sequence) - 1):
                    if sequence[k] == firstCodon and sequence[k + 1] == secondCodon:
                        counter += 1
            dicodonFrequencies.append(counter / sequencesLength)
    return dicodonFrequencies