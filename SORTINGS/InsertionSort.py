def insertion(n):
    for i in range(len(n)):
        j = i
        while j > 0 and n[j] < n[j-1]:
            n[j], n[j-1] = n[j-1], n[j]
            j -= 1
    return n

n = [3, 5, 9, 1, 6, 2, 6]
print(insertion(n))