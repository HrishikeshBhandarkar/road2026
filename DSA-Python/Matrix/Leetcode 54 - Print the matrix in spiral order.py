def SpiralMatrix(matrix):
    if not matrix or not matrix[0]:
        return []

    top , left = 0 , 0
    result = []
    bottom , right = len(matrix) , len(matrix[0])

    while top<=bottom and left<=bottom:
        for i in range (left,right+1):
            result.append(matrix[top][i])
        top+=1
        for i in range (top,bottom+1):
            result.append(matrix[i][right])
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                result.append(matrix[i][bottom])
            bottom-=1
        if left<=right:
            for i in range (bottom,top-1,-1):
                result.append(matrix[left][i])
            left+=1
    return result


