def insertion_sort(list: list[float]):
    n = len(list)

    for i in range (1, n):
        num = list[i]
        j = i - 1
        while j >=0 and num < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = num
    return list


list_to_filter = [1, 6, 123, 756, 534, 243, 465, 786, 867, 465, 435, 432, 23]
print("Lista antes de ser ordenada:", list_to_filter)
print("Lista após ser ordenada:", insertion_sort(list_to_filter))
