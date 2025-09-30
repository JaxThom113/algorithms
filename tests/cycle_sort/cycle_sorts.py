"""

Using this Python file as a way to test and 
compare different cycle sorts

Wikipedia: https://en.wikipedia.org/wiki/Cycle_sort
Geeks4Geeks: https://www.geeksforgeeks.org/dsa/python-program-for-cycle-sort/
YouTube: https://www.youtube.com/watch?v=wx_nkK3GBco 

"""

# Cycle sort currently in the repository
def cycle_sort(arr):
    len_arr = len(arr)
    # Finding cycle to rotate.
    for cur in range(len_arr - 1):
        item = arr[cur]

        # Finding an index to put items in.
        index = cur
        for i in range(cur + 1, len_arr):
            if arr[i] < item:
                index += 1

        # Case of there is not a cycle
        if index == cur:
            continue

        # Putting the item immediately right after the duplicate item or on the right.
        while item == arr[index]:
            index += 1
        arr[index], item = item, arr[index]

        # Rotating the remaining cycle.
        while index != cur:

            # Finding where to put the item.
            index = cur
            for i in range(cur + 1, len_arr):
                if arr[i] < item:
                    index += 1

            # After item is duplicated, put it in place or put it there.
            while item == arr[index]:
                index += 1
            arr[index], item = item, arr[index]
    return arr

# Wikipedia cycle sort
def wiki_cycle_sort(array):
    """Sort an array in place and return the number of writes."""
    writes = 0

    # Loop through the array to find cycles to rotate.
    # Note that the last item will already be sorted after the first n-1 cycles.
    for cycle_start in range(0, len(array) - 1):
        item = array[cycle_start]

        # Find where to put the item.
        pos = cycle_start
        for i in range(cycle_start + 1, len(array)):
            if array[i] < item:
                pos += 1

        # If the item is already there, this is not a cycle.
        if pos == cycle_start:
            continue

        # Otherwise, put the item there or right after any duplicates.
        while item == array[pos]:
            pos += 1

        array[pos], item = item, array[pos]
        writes += 1

        # Rotate the rest of the cycle.
        while pos != cycle_start:
            # Find where to put the item.
            pos = cycle_start
            for i in range(cycle_start + 1, len(array)):
                if array[i] < item:
                    pos += 1

            # Put the item there or right after any duplicates.
            while item == array[pos]:
                pos += 1
            array[pos], item = item, array[pos]
            writes += 1

    return array # modified to return array, not writes

# Geeks4Geeks cycle sort
def g4g_cycle_sort(array):
    writes = 0

    # Loop through the array to find cycles to rotate.
    for cycleStart in range(0, len(array) - 1):
        item = array[cycleStart]

        # Find where to put the item.
        pos = cycleStart
        for i in range(cycleStart + 1, len(array)):
            if array[i] < item:
                pos += 1

        # If the item is already there, this is not a cycle.
        if pos == cycleStart:
            continue

        # Otherwise, put the item there or right after any duplicates.
        while item == array[pos]:
            pos += 1
        array[pos], item = item, array[pos]
        writes += 1

        # Rotate the rest of the cycle.
        while pos != cycleStart:

            # Find where to put the item.
            pos = cycleStart
            for i in range(cycleStart + 1, len(array)):
                if array[i] < item:
                    pos += 1

            # Put the item there or right after any duplicates.
            while item == array[pos]:
                pos += 1
            array[pos], item = item, array[pos]
            writes += 1

    return array # modified to return array, not writes

# YouTube video cycle sort
def yt_cycle_sort(l):
    writes = 0

    for c_start in range(0, len(l)-1):
        item = l[c_start]

        pos = c_start
        for i in range(c_start+1, len(l)):
            if l[i] < item:
                pos += 1

        if pos == c_start:
            continue
    
        while item == l[pos]:
            pos +=1 

        l[pos], item = item, l[pos]
        writes += 1

        while pos != c_start:
            pos = c_start
            for i in range(c_start+1, len(l)):
                if l[i] < item:
                    pos += 1

            while item == l[pos]:
                pos += 1
            l[pos], item = item, l[pos]
            writes += 1

    return l

# My cycle sort
def cycle_sort(arr):
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