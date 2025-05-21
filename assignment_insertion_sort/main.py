def insertion_sort(array):
    # Get the length of the array
    n = len(array)  

    # We start from the second element (index 1), as the first element we consider as sorted
    # Traverse through 1 to n
    for i in range(1, n):

        # The element which we want to insert into the sorted part
        key = array[i] 

        # Pointer for the last index of the sorted part
        j = i - 1

        # We check that index is inside the bounds of sorted part of array (j is not negative)  
        # And compare each element in the sorted part with the key
        # If the element is greater than the key, we need to shift it to the right
        while j >= 0 and array[j] > key:

            # Shift the larger element to the right, to make space for the key
            # In this case we create a new space for the key
            array[j + 1] = array[j]

            # After moving the element, we need to check the next element in the sorted part
            # So we move the pointer to the left
            j -= 1       

        # Insert the key into its correct position in the sorted part
        array[j + 1] = key

    # Return the sorted array
    return array  
