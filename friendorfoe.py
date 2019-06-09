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


# rewrote it with a return direct to list and initial arg that can be a list

def friends(x):
    friend_list = [x]
    filling_active = True
    while filling_active:
        name = input("Enter a name ")
        friend_list = friend_list + [name]
        add = input("Do you want to add another? ")
        if add == 'no':
            filling_active = False
    return [friend for friend in friend_list if len(friend) == 4]

        
list = friends('Jono')
