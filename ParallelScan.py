matchScore = 1
mismatchScore = -1
gapScore = -2
seq1 = "ATCG"
seq2 = "AGCG"

# Pls do not modify anything below this
print("Reference: ", seq1)
print("Read: ", seq2)

def prefixMax(inputArray):
    outputArray = [inputArray[0]]
    for i in range(1, len(inputArray)):
        outputArray.append(max(outputArray[-1], inputArray[i]))
    return outputArray

def HIntermediate(rowIPrev, jPos, iPos):
  global mismatchScore, matchScore, gapScore, seq1, seq2
  return max(0, int(rowIPrev[jPos] + gapScore), int(rowIPrev[jPos-1] + (matchScore if seq1[jPos-1] == seq2[iPos-1] else mismatchScore)))

def HFinal(finalInput, jPos):
  global gapScore
  return max(finalInput[jPos], int((jPos * gapScore)))


rows, cols = len(seq2) + 1, len(seq1) + 1
matrix = [[0] * cols for _ in range(rows)]
hPrime = [0 * rows for _ in range(cols-1)]
gapArray = [0 * rows for _ in range(cols-1)]
Lij = [0 * rows for _ in range(cols-1)]
for i in range(1, rows):
  for j in range(1, cols):
    hPrime[j-1] = HIntermediate(matrix[i-1], j, i)
  #print(f"H'{i},{j}: ", hPrime)
  for j in range(0, cols-1):
    hPrime[j] = int(hPrime[j]+((len(hPrime)-j) - 1)*gapScore)
    gapArray[j] = int(-((len(hPrime)- j - 1) * gapScore))
  prefixOut = prefixMax(hPrime)
  Lij = [a + b for a, b in zip(prefixOut, gapArray)]
  for j in range(0, cols-1):
    matrix[i][j+1] = HFinal(Lij,j) 
print("Final Matrix:")
for row in matrix:
  print(row)
print("")
