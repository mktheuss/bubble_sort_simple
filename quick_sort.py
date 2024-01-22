def quickSort(list: list[float], left, right):
    # Base case: if the left index is greater than or equal to the right index, the list is already sorted
    if left >= right:
        return

    # Choose a pivot element and rearrange the list elements accordingly
    m = calcMid(list, left, (left + right) // 2, right)
    list[left], list[m] = list[m], list[left]

    # Get the index of the pivot after rearranging the list
    pivot_index = partition(list, left, right)

    # Recursively apply QuickSort to the sublists on both sides of the pivot
    quickSort(list, left, pivot_index - 1)
    quickSort(list, pivot_index + 1, right)


# Function to partition the list around a pivot element
def partition(list: list[float], left, right):
    # Choose the leftmost element as the pivot
    pivot = list[left]
    i = left
    j = right

    # Continue until the indices i and j meet
    while i <= j:
        # Find an element on the left side greater than or equal to the pivot
        while list[i] < pivot:
            i += 1
            if i == right:
                break

        # Find an element on the right side less than or equal to the pivot
        while pivot < list[j]:
            j -= 1
            if j == left:
                break

        # Swap the elements if they are out of order
        if i >= j:
            break

        # Handle case where elements are equal
        if list[i] == list[j]:
            i += 1
            j -= 1
        else:
            list[i], list[j] = list[j], list[i]

    # Swap the pivot element to its correct position
    pivot, list[j] = list[j], pivot

    # Return the index of the pivot element
    return j


# Function to calculate the middle index among three indices based on the values
def calcMid(list, i, j, k):
    if list[i] < list[j]:
        return j if list[j] < list[k] else (i if list[i] < list[k] else k)
    else:
        return i if list[i] < list[k] else (j if list[j] < list[k] else k)


list_to_filter = [234, 654, -1, 43224, 3054, -12334, 0, 1]
print("Original List:", list_to_filter)
quickSort(list_to_filter, 0, len(list_to_filter) - 1)
print("Sorted List:", list_to_filter)
