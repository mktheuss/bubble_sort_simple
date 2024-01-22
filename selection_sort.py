def selection_sort(list: list[float]):
    n = len(list)
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if list[j] < list[min_index]:
                min_index = j

        (list[i], list[min_index]) = (list[min_index], list[i])
    
    return list


list_to_filter = [11, 1234, 45, 756, 897, 765, -45, 34]
print("Lista antes de ser ordenada:", list_to_filter)
print("Lista após ser ordenada:", selection_sort(list_to_filter))
