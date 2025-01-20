def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """그냥 하나 pivot으로 정하고 그거보다 작은건 왼쪽, 큰건 오른쪽으로 보내면 됨.
    이것도 분할정복.
    """

    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, right = [], []
    for i, val in enumerate(arr):
        if i == len(arr) // 2:
            continue
        if val <= pivot:
            left.append(val)
        else:
            right.append(val)
    return [*quick_sort(left), pivot, *quick_sort(right)]
