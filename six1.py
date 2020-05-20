import numpy as np
def countSpecialElements(matrix):
    nRows = len(matrix)
    nCount = 0
    for row in matrix:
        for indexCol, element in enumerate(row):
            if element == min(row) or element == max(row):
                if row.count(element) > 1:
                    return -1
                nCount = nCount + 1
            else:
                listColumn = []
                for indexRow in range(0, nRows):
                    listColumn.append(matrix[indexRow][indexCol])
                if element == min(listColumn) or element == max(listColumn):
                    if listColumn.count(element) > 1:
                        return -1
                    nCount = nCount + 1
    return nCount
if __name__ == '__main__':
    nCount = countSpecialElements([[1, 3, 4], [5, 2, 9], [8, 7, 6]])
    print(nCount)
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(int, input().split()))
    matrix = np.array(entries).reshape(R, C)
    print(countSpecialElements(matrix)) 
