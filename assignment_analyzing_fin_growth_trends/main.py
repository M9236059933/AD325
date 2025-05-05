def sortedSquares(array):
    squares = []
    for num in array:
        squares.append(num * num)
    squares.sort()
    return squares