# Steve Phillips-Ward


import random
# Problem 2
# Insertion Sort implementation

def insertion_sort(A):
    n = len(A)

    #track comparisons and movemenents
    comparisons = 0
    exchanges = 0

    #for loop to iterate through the array
    for i in range(1, n):

        key = A[i]
        j = i - 1

        #move elemnts based on value comparison check and exchange count
        while j >= 0 and A[j] > key:
            comparisons += 1
            A[j + 1] = A[j]
            j -= 1
            exchanges += 1
        
        #Handle the case where the while loop condition fails due to A[j] <= key
        if j >= 0:
            comparisons += 1

        # place the key in its correct position
        A[j + 1] = key

    print("Insertion Sort Result:", A)
    print("Comparisons:", comparisons)
    print("Exchanges:", exchanges)
    print()

# Generate arrays to be applied to problem 2
print("Insertion Sort:")
A = [1,2,3,4,5,6,7,8,9,10]
B = [10,9,8,7,6,5,4,3,2,1]

print("Best Case:")
insertion_sort(A.copy())
print("Worst Case:")
insertion_sort(B.copy())



# Problem 4
# Randomized Quick Sort implementation

def randomized_partition(A, Low, High, recurrence):
    #Select a random pivot index
    pivot_index = random.randint(Low, High)
    pivot_value = A[pivot_index]

    #Swap the pivot with the last element
    A[pivot_index], A[High] = A[High], A[pivot_index]

    pivot = A[High]
    i = Low - 1

    # Partition the array around the pivot
    for j in range(Low, High):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    # Place the pivot in its correct position
    A[i + 1], A[High] = A[High], A[i + 1]

    print(f"recurrence: {recurrence}, pivot: {pivot_value}")
    print(f"Subarray after partitioning: {A[Low:High+1]}")
    print()

    return i + 1  # <--- RETURN THE PIVOT INDEX

def randomized_quicksort(A, Low, High, recurrence=1):
    if Low < High:
        print(f"recurrence: {recurrence}, current subarray: {A[Low:High+1]}")
        print(f"Size of subproblem: {High - Low + 1}")

        q = randomized_partition(A, Low, High, recurrence)

        #Left Side
        randomized_quicksort(A, Low, q - 1, recurrence + 1)
        #Right Side
        randomized_quicksort(A, q + 1, High, recurrence + 1)

print("Randomized Quick Sort:")

C = [5,6,2,1,9,11,7,10,4]
print("Original Array:", C)
randomized_quicksort(C, 0, len(C) - 1)
print("Sorted Array:", C)
print()

# Problem 5
# Merge Sort Implementation

def merge(A, Low, Mid, High):
    # Create temporary arrays for left and right subarrays
    left = A[Low:Mid + 1]
    right = A[Mid + 1:High + 1]

    i = j = 0
    k = Low

    # Merge the two subarrays back into A
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements of left, if any
    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements of right, if any
    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1

def merge_sort(A, Low, High, recurrence=1):
    if Low < High:
        print(f"recurrence: {recurrence}, current subarray: {A[Low:High+1]}")
        print(f"Size of subproblem: {High - Low + 1}")

        Mid = (Low + High) // 2

        #Left Side
        merge_sort(A, Low, Mid, recurrence + 1)
        #Right Side
        merge_sort(A, Mid + 1, High, recurrence + 1)

        #Merge the sorted halves
        merge(A, Low, Mid, High)


print("Merge Sort:")
D = [8,3,7,5,9,2]
print("Original Array:", D)
merge_sort(D, 0, len(D) - 1)
print("Sorted Array:", D)
print()
