def getRow(rowIndex):
    def getRowHelper(row, col, rowLength):
        # base case
        if col == 0 or col == rowLength - 1:
            return 1
        else:
            # call function recursively to find the pascal number
            # get left parent
            if (row - 1, col - 1) not in store.keys():
                store[(row - 1, col - 1)] = getRowHelper(row - 1, col - 1, rowLength - 1)
            left = store[(row - 1, col - 1)]
            # get right parent
            if (row - 1, col) not in store.keys():
                store[(row - 1, col)] = getRowHelper(row - 1, col, rowLength - 1)
            right = store[(row - 1, col)]
            return left + right



    # allocate space for output array
    output = [None] * (rowIndex + 1)
    # use a dictionary to reduce function calls
    store = {}
    for i in range(len(output)):
        output[i] = getRowHelper(rowIndex, i, len(output))
    return output

print(getRow(24))
