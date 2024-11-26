def smith_waterman_cell(matrix, seq1, seq2, i, j, match_score=1, mismatch_penalty=-1, gap_penalty=-2):
    """
    Calculate the value of a cell in the Smith-Waterman scoring matrix.

    Args:
        matrix (list of list of int): The scoring matrix.
        seq1 (str): First sequence (horizontal).
        seq2 (str): Second sequence (vertical).
        i (int): Row index (1-based for the sequences).
        j (int): Column index (1-based for the sequences).
        match_score (int): Score for a match (default is 2).
        mismatch_penalty (int): Penalty for a mismatch (default is -1).
        gap_penalty (int): Penalty for a gap (default is -1).

    Returns:
        int: The value of the cell at position (i, j).
    """
    if i == 0 or j == 0:
        # Cells in the first row or column are initialized to 0
        return 0

    # Match or mismatch score
    match = (
        matrix[i - 1][j - 1] + (match_score if seq1[j - 1] == seq2[i - 1] else mismatch_penalty)
    )
    # Gap penalties
    delete = matrix[i - 1][j] + gap_penalty
    insert = matrix[i][j - 1] + gap_penalty

    # Smith-Waterman: Take the maximum of these values or 0 (local alignment)
    #print(f"H[{i}][{j}] = {max(0, match, delete, insert)}\n match = {match}\n delete = {delete}\n insert = {insert}\n\n")
    return max(0, match, delete, insert)

# Example usage
if __name__ == "__main__":
    seq1 = "ATCG"
    seq2 = "AGCG"
    
    # Initialize a zero-filled matrix
    rows, cols = len(seq2) + 1, len(seq1) + 1
    matrix = [[0] * cols for _ in range(rows)]

    # Fill the matrix row by row
    for i in range(1, rows):
        for j in range(1, cols):
            matrix[i][j] = smith_waterman_cell(matrix, seq1, seq2, i, j)

    # Print the matrix
    for row in matrix:
        print(row)
