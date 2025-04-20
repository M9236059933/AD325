def merge_customer_data(customerData1, m, customerData2, n):
    i = m - 1 # Last index of customerData1
    j = n - 1 # Last index of customerData2
    k = m + n - 1 # Last index of merged array
    while i >= 0 and j >= 0:
        # Compare elements from the end of both arrays
        # and place the larger one in the merged array
        if customerData1[i] > customerData2[j]:
            customerData1[k] = customerData1[i]
            # Move the pointer in customerData1
            i -= 1
        else:
            customerData1[k] = customerData2[j]
            # Move the pointer in customerData2
            j -= 1
        k -= 1 # Fill the merged array from the end
    # If there are remaining elements in customerData2, copy them to customerData1
    while j >= 0:
        customerData1[k] = customerData2[j]
        j -= 1
        k -= 1

        