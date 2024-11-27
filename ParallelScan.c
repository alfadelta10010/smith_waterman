#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MATCH_SCORE 1
#define MISMATCH_SCORE -1
#define GAP_SCORE -2

const char *seq1 = "AGTGACGTCACCAGGACTGCATCAGGATTGACAGTATAGTTTCGTGGAGG";
const char *seq2 = "CAAGCCTGGCGAAATAAGAATATGACGGAT";

void prefixMax(int *inputArray, int *outputArray, int length) {
    outputArray[0] = inputArray[0];
    for (int i = 1; i < length; i++) {
        outputArray[i] = (outputArray[i - 1] > inputArray[i]) ? outputArray[i - 1] : inputArray[i];
    }
}

int HIntermediate(int *rowIPrev, int jPos, int iPos) {
    int matchMismatch = (seq1[jPos - 1] == seq2[iPos - 1]) ? MATCH_SCORE : MISMATCH_SCORE;
    int score1 = rowIPrev[jPos] + GAP_SCORE;
    int score2 = rowIPrev[jPos - 1] + matchMismatch;
    return (score1 > score2 ? score1 : score2) > 0 ? (score1 > score2 ? score1 : score2) : 0;
}

int HFinal(int finalInput, int jPos) {
    int gapScoreCalc = jPos * GAP_SCORE;
    return (finalInput > gapScoreCalc) ? finalInput : gapScoreCalc;
}

int main() {
    int rows = strlen(seq2) + 1;
    int cols = strlen(seq1) + 1;

    // Initialize matrix
    int **matrix = (int **)malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; i++) {
        matrix[i] = (int *)calloc(cols, sizeof(int));
    }

    // Temporary arrays
    int *hPrime = (int *)calloc(cols - 1, sizeof(int));
    int *gapArray = (int *)calloc(cols - 1, sizeof(int));
    int *prefixOut = (int *)calloc(cols - 1, sizeof(int));
    int *Lij = (int *)calloc(cols - 1, sizeof(int));

    for (int i = 1; i < rows; i++) {
        for (int j = 1; j < cols; j++) {
            hPrime[j - 1] = HIntermediate(matrix[i - 1], j, i);
        }

        for (int j = 0; j < cols - 1; j++) {
            hPrime[j] += ((cols - j - 2) * GAP_SCORE);
            gapArray[j] = -((cols - j - 2) * GAP_SCORE);
        }

        prefixMax(hPrime, prefixOut, cols - 1);
        for (int j = 0; j < cols - 1; j++) {
            Lij[j] = prefixOut[j] + gapArray[j];
        }

        for (int j = 0; j < cols - 1; j++) {
            matrix[i][j + 1] = HFinal(Lij[j], j);
        }
    }

    // Print final matrix
    printf("Final Matrix:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }

    // Cleanup
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
    free(hPrime);
    free(gapArray);
    free(prefixOut);
    free(Lij);

    return 0;
}
