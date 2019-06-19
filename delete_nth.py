def delete_nth(order, max_e):
    """ Doctest.
    >>> delete_nth([20,37,20,21], 1)
    [20,37,21]
    >>> delete_nth([1,1,3,3,7,2,2,2,2], 3)
    [1, 1, 3, 3, 7, 2, 2, 2]
    """
    resp = []
    for i in order:
            k = 0
            if resp.count(i) == max_e:
                k = max_e + 1
            while k <= max_e:
                resp += [i]
                k += 1
                if i in resp:
                    break
    return resp


# alt solution

def delete_nth_b(order,max_e):
    resp = []
    for i in order:
        if resp.count(i) < max_e:
            resp.append(i)
    return resp
