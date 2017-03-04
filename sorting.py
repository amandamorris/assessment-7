#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    # iterate through the list
    #     if an element is greater than the next element, swap them
    # do this until you get through the list without swapping?
    for num in range(len(lst) - 1):
        for index in range(len(lst) - 1 - num):
            swapped = False
            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
                swapped = True
        if not swapped:
            break
    return lst



def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    merged = []
    # as long as at least one of the lists isn't empty:
    while list1 or list2:
        # if list1 is empty, pop from list2
        if not list1:
            merged.append(list2.pop(0))
        # if list2 is empty, pop from list1
        elif not list2:
            merged.append(list1.pop(0))
        # otherwise compare the first element of the lists, and pop the smaller
        elif list1[0] < list2[0]:
            merged.append(list1.pop(0))
        else:
            merged.append(list2.pop(0))
    return merged


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    # base case - single element list is already sorted
    if len(lst) == 1:
        return lst

    midpoint = len(lst)/2

    # split list into 2 halves, call merge sort on each half
    left_lst = merge_sort(lst[:midpoint])
    right_lst = merge_sort(lst[midpoint:])

    return merge_lists(left_lst, right_lst)




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
