def partition(num, low, high):
    pivot = num[low]
    i = low + 1
    j = high

    while True:
        while i <= high and num[i] < pivot:
            i += 1
        while j >= low and num[j] > pivot:
            j -= 1

        if i >= j:
            break

        num[i], num[j] = num[j], num[i]
        i += 1
        j -= 1

    num[low], num[j] = num[j], num[low]
    return j


def quick_sort(num, low, high):
    if low < high:
        p_i = partition(num, low, high)
        quick_sort(num, low, p_i - 1)
        quick_sort(num, p_i + 1, high)


k = [3,1,2]
print(k)
quick_sort(k,0,len(k)-1)
print(k)

