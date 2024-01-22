def bubble_sort(list: list[float]):
    n = len(list)

    for i in range(n):
        for j in range(n - 1):
            num1 = list[j]
            num2 = list[j + 1]
            swap: bool = num1 > num2

            if swap:
                list[j], list[j + 1] = num2, num1

    return list


list_to_filter = [456, 132, 43, 253, 77685, 987, 345, 2347, 8324, 0]
print("Lista antes de ser ordenada:", list_to_filter)
print("Lista após ser ordenada:", bubble_sort(list_to_filter))
