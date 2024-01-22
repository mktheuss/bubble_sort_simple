def merge_sort(list: list[float]) -> list[float]:
    n = len(list)
    if n > 1:
        # Creating two halves of the list
        mid = n // 2
        sub_list1 = list[:mid]
        sub_list2 = list[mid:]

        # Sorting both halves of the list
        merge_sort(sub_list1)
        merge_sort(sub_list2)

        # Initial value of trackers
        i = j = k = 0

        # Pick larger between indexes of both halves of the list and iterate
        while i < len(sub_list1) and j < len(sub_list2):
            if sub_list1[i] < sub_list2[j]:
                list[k] = sub_list1[i]
                i += 1
            else:
                list[k] = sub_list2[j]
                j += 1
            k += 1

        # Picks remaining elements and sorts them
        while i < len(sub_list1):
            list[k] = sub_list1[i]
            i += 1
            k += 1

        while j < len(sub_list2):
            list[k] = sub_list2[j]
            j += 1
            k += 1

    return list


list_to_sort = [312, 543, 56, -12, -543, 0, 432, 43324]
print("List before sorting:", list_to_sort)
print("List after sorting:", merge_sort(list_to_sort))
