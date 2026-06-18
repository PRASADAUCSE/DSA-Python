def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        # Assume the first unsorted element is the minimum
        min_index = i
        
        # Inner loop finds the actual minimum element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

# Example execution
numbers = [2,4,3,5,1]
print(selection_sort(numbers))
