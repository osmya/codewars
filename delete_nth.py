def delete_nth(order, max_e):
    """ Doctest.
    >>> delete_nth([20,37,20,21], 1)
    [20,37,21]
    >>> delete_nth([1,1,3,3,7,2,2,2,2], 3)
    [1, 1, 3, 3, 7, 2, 2, 2]
    """
    new_order = []
    for i in order:
            k = 0
            if new_order.count(i) == max_e:
                k = max_e + 1
            while k <= max_e:
                new_order += [i]
                k += 1
                if i in new_order:
                    break
    return new_order
