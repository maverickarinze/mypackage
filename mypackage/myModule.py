def top_n(items, n):
    """Returns top n items in a list, in descending order

    Args:
        items(array): list or array-like object
        n (int): number of items to return

    Return:
        Array: Top n items in descending order"""

    for i in range(n): #Keep sorting until we have top n
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]: #If this item is bigget than the next item
                items[j], items[j+1] = items[j+1], items[j] #Swap the items

    #Get last 2 items
    top_n = items[-n:]

    #Return in descending order
    return top_n[::-1]