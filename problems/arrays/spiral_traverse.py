"""
Spiral Traverse

Write a function that takes in an n x m two-dimensional array and returns a one-
dimensional array if all array's element in spiral order.

Spiral order starts at the top left of the corner of the 2D array, goes right,
and proceeds down in a spiral pattern all the way until all elements have been visited.
"""


def spiralTraverse(array):
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    output = []
    while startCol <= endCol and startRow <= endRow:

        # traverse all cols in top row
        for col in range(startCol, endCol + 1):
            output.append(array[startRow][col])

        # traverse all rows in last col
        for row in range(startRow + 1, endRow + 1):
            output.append(array[row][endCol])

        # traverse all cols in bottom row
        for col in reversed(range(startCol, endCol)):
            # handle edge case when there's a single row in the middle of the
            # matrix. In this case, we don't double count the values in this row
            # since we have already counted in the first loop above
            if startRow == endRow:
                break
            output.append(array[endRow][col])

        # traverse all rows in first col
        for row in reversed(range(startRow + 1, endRow)):
            # similarly,  handle edge case when there's a single col in the
            # middle of the  matrix. In this case, we don't double count the
            # values in this col since we have already counted in the second loop above
            if startCol == endCol:
                break
            output.append(array[row][startCol])

        # move in 1 level of traversal
        startCol += 1
        startRow += 1
        endCol -= 1
        endRow -= 1

    return output
