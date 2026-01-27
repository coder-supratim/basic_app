def findDuplicateElements(nums):
    """
    This function takes a list of elements and returns a list of duplicate elements found in the input list.
    
    Parameters:
    nums (list): A list of elements which may contain duplicates.
    
    Returns:
    list: A list containing the duplicate elements.
    """
    once = set()
    dups = set()

    for num in nums:
        if num in once:
            dups.add(num)
        else:
            once.add(num)

    return dups
	
print(findDuplicateElements([5,1,2,3,3,5]))