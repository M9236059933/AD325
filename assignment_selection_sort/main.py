def selection_sort(arr):
    n = len(arr)
    # Loop through all array elements
    for i in range(n):

        # Assume the current index is the minimum
        min_index = i

        # We need to go through the remaining unsorted array (right side of i)
        for j in range(i + 1, n):

            # If an element smaller than the current minimum is found, update min_index
            if arr[j] < arr[min_index]:
                min_index = j

        # Finally swap the found minimum with the current element, for Java and C++ need to use temp variable
        arr[i], arr[min_index] = arr[min_index], arr[i]

