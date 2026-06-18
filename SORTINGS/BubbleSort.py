def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop to traverse through all list elements
    for i in range(n):
        swapped = False
        
        # Inner loop for adjacent comparisons
        # Last i elements are already in place, so we skip them
        for j in range(0, n - i - 1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no two elements were swapped in the inner loop, the list is sorted
        if not swapped:
            break

# Example usage:
data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(data)
print("Sorted array:", data)
# Output: [11, 12, 22, 25, 34, 64, 90]
