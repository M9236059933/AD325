def bubble_sort(array):
    # Get the length of the array
    n = len(array) 
    
    # Outer loop we go through the entire list
    for i in range(n):
        
        # Inner loop we go through the list from the beginning to the last unsorted element
        last_unsorted = n - i - 1
        for j in range(0, last_unsorted):
            
            # Compare the current element with the next one
            if array[j] > array[j + 1]:

                # If the current element is bigger, swap them, for C# or Java use a temporary variable
                # After the swap, the larger number moves one position to the right
                array[j], array[j + 1] = array[j + 1], array[j]

    # Return the sorted array
    return array  


def bubble_sort_optimized(array):
    # Get the length of the array
    n = len(array)

    # Outer loop we go through the entire list
    for i in range(n):

        # We create a flag to check if we made any swaps
        swapped = False

        # Inner loop we go through the list from the beginning to the last unsorted element
        last_unsorted = n - i - 1
        for j in range(0, last_unsorted):

            # Compare the current element with the next one
            if array[j] > array[j + 1]:

                # If the current element is bigger, swap them, for C# or Java use a temporary variable
                # After the swap, the larger number moves one position to the right
                array[j], array[j + 1] = array[j + 1], array[j]

                # Set the flag to True, indicating a swap was made
                swapped = True

        # If no swaps were made in the inner loop, the array is already sorted
        if not swapped:

            # We can break out of the loop early
            break

    # Return the sorted array
    return array