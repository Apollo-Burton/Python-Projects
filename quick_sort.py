a = [12, 54, 867, 24, 45, 65, 23, 90, 1, 27, 99, 144]

# Define the partition function that returns a pivot index
def partition(low: int, high: int) -> int:
    i = low
    j = high
    pivot = a[low]  # Choose the first element as the pivot

    # Iterate until i and j cross over each other
    while i < j:
        # Move i to the right as long as the element is less than or equal to the pivot
        while a[i] <= pivot and i < high:
            i += 1
        # Move j to the left as long as the element is greater than the pivot
        while a[j] > pivot and j > low:
            j -= 1
        # If i and j haven't crossed over, swap the elements at i and j
        if i < j:
            a[i], a[j] = a[j], a[i]
    
    # Swap the pivot with the element at j, which is now in its correct sorted position
    a[j], a[low] = a[low], a[j]
    return j

# Define the quick_sort function that sorts the array recursively using partition function
def quick_sort(low: int, high: int):
    if low < high:
        j = partition(low, high)  # Get the pivot index from partition function
        quick_sort(low, j - 1)  # Recursively call quick_sort function on the two sub-arrays divided by pivot
        quick_sort(j + 1, high)

# Test the sorting algorithm
print("Unsorted:", a)
quick_sort(0, len(a) - 1)
print("Sorted:", a)
