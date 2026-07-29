def longest_sequence(array):
    array.sort()
    print(array)
    last_num=array[0]
    max_sequence=0
    count=1
    
    for i in array:
        if last_num==i:
            continue
        if i == last_num+1:
            count+=1
        else: 
            count=1
        if max_sequence<count:
            max_sequence=count
        last_num=i
    return  max_sequence
array = [0]
print(array)
print(longest_sequence(array))    