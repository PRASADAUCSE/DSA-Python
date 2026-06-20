def divide(arr, left, right):
    if(left >= right):
        return
    pos = partition(arr, left, right)
    divide(arr, left, pos-1)
    divide(arr, pos+1, right)

def partition(arr, left, right):
    i=left
    j = right
    pivot = arr[left]
    while(i<j):
        while(i<=right and arr[i] <= pivot):
            i+=1
        while(j>=left and arr[j] >= pivot):
            j-=1
        
        if(i<j):
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

n = [5,3,12,4,5,6]
divide(n, 0, len(n)-1)
print(n)
