def valid_parentheses(string):
    """A function that takes a string of parentheses and determines
    if their order is valid.
    
    >>> valid_parentheses('()')
    True
    >>> valid_parentheses('(')
    False
    >>> valid_parentheses('(())((()())())')
    True
    >>> valid_parentheses(')test')
    False
    >>> valid_parentheses('hi(hi)()')
    True
    >>> valid_parentheses("")
    True
    >>> valid_parentheses('hi())(')
    False
    >>> valid_parentheses('har()(qwk)wcobfny)(amomq(pjazowjvvjutotk)')
    True
    """
    assert len(string) <= 100, 'insert a shorter string, max 100 lenght'
    par_list = [x for x in string if x == '(' or x == ')']
    # could make it with a flag e.g. count = 0
    listlen = len(par_list)
    if listlen == 0:
        return True
    for _ in par_list:
        if par_list[0] == '(' and ')' in par_list:
            if par_list.count('(') == par_list.count(')') and par_list[-1] == ')':
                return True
            else: return False
        else:
            return False
            
"""Getting an error in codewars:

Testing for har()(qwk)wcobfny)(amomq(pjazowjvvjutotk)
It should work for random inputs too: True should equal False

To test for a random string I tried adding in global frame:

import random
import string

rand_string = string.ascii_letters + string.digits + string.punctuation

However in this way the doctest for 

>>>valid_parentheses(''.join(random.choice(rand_string) for i in range(100)))

Can either return False or True and it invalidates the program

Issue link https://www.codewars.com/kata/valid-parentheses/discuss/python
"""
