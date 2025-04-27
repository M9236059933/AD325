def duplicate_zeros(inventory):
    # count zeros in current array
    zeros = 0
    for item in inventory:
        if item == 0:
            zeros += 1

    n = len(inventory) # length of array
    i = n - 1 # last index for starting from the end

    while zeros > 0:
        # check if inside array bounds 
        if i + zeros < n:
            inventory[i + zeros] = inventory[i]
            
        # if current item is zero, duplicate it if in bounds
        if inventory[i] == 0:
            zeros -= 1
            if i + zeros < n:
                inventory[i + zeros] = 0

        i -= 1
