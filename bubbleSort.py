# write your bubble sort algorithm below

def bubble_sort(lst):
    # Iterate over the list to perform bubble sort
    for i in range(len(lst)):
        swapped = False  # Flag to optimize the algorithm       
        # Iteration for comparing adjacent elements
        print("Iteration:", i + 1)  # Display the current iteration
        for j in range(len(lst) - 1):
            # Compare and swap adjacent elements if necessary
            print("Comparing:", lst[j], lst[j + 1])
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True  # Set the swapped flag to indicate a swap occurred
        
        # Optimization: If no swaps occurred in the current iteration, the list is already sorted
        if not swapped:
            return lst
    
    return lst



# testing algorithm
sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")
