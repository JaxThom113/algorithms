def cycle_sort(arr):
    """

    My own implementation of cycle sort
    
    Average time complexity : O(N^2)
    Worst case time complexity : O(N^2)

    """

    # Traverse through array
    for cycle_start in range(0, len(arr)-1):
        current_num = arr[cycle_start]

        # Find position where current num belongs
        pos = cycle_start
        for i in range(cycle_start + 1, len(arr)):
            if arr[i] < current_num:
                pos += 1

        # If current num is already where it needs to be, then there is no cycle
        if pos == cycle_start:
            continue
    
        # Otherwise, swap current to this spot, after duplicates if there are any
        while current_num == arr[pos]:
            pos += 1 
        arr[pos], current_num = current_num, arr[pos]

        # Rotate the rest of the cycle
        while pos != cycle_start:
            # Same code as above, just without the check if it's already where it needs to be
            pos = cycle_start
            for i in range(cycle_start + 1, len(arr)):
                if arr[i] < current_num:
                    pos += 1

            while current_num == arr[pos]:
                pos += 1
            arr[pos], current_num = current_num, arr[pos]

    return arr
