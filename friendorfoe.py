def friend(): #doctest needs work
    """Make a program that filters a list of strings and returns a list 
    with only strings of 4 letters in it.
    
    >>> input = ["a", "ab", "abc", "abcd", "abcde"]
    ["abcd"]
    """
    friend_list = []
    filling_active = True
    while filling_active:
        name = input("\nEnter a name: ")
        friend_list = friend_list + [name]
        repeat = input("\nWould you like to enter another name? y/n ")
        if repeat == 'n':
            filling_active = False
    for friend in friend_list:
        if len(friend) == 4:
            print(friend)
        
friend()
