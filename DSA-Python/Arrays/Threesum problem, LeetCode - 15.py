def tzero(array):
    array = array.sort()
    result = set()
    n=len(array)
    for i in range(n):
        if n!=0 and array[i]==array[i-1]:
            continue
        j = i+1
        k = n-1
        while j < k:
            t_sum = array[i]+array[j]+array[k]
            if t_sum < 0 :
                j+=1
            elif t_sum > 0:
                k-=1
            else:
                temp = [array[i],array[j],array[k]]
                result.add(tuple(temp))
                j+=1
                k-=1
                while j < k and array[j]==array[j-1]:
                    j+=1
                while k>j and array[k]==array[k+1]:
                    k-=1
    return result
            
