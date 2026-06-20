def merge_sort(arr):
    """
    Part 1: Dividing phase.
    Recursively splits the array down to single elements.
    """
    # Base case: a list of 1 or 0 elements is already sorted
    if len(arr) <= 1:
        return arr

    # Find the midpoint and split the array
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Part 2: Merging phase.
    # Combine the sorted halves back together
    return merge(sorted_left, sorted_right)



def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.
    """
    result = []
    i = j = 0

    # Compare elements from both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from the left or right list
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result



arr= [38, 27, 43, 3, 9, 82, 10]
result = merge_sort(arr)
print(result)
    
