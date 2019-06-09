def sqdigits(num):
    """Squares each digit in num. num is integer
    >>> sqdigits(2)
    4
    >>> sqdigits(24)
    416
    """
    digits = [int(x) for x in str(abs(num))] #make a list of int values
    for digit in digits:
        print(digit*digit, end="") #end= indicates delimiter in print

#other solutions

"""
def sq(num):
    words = list(str(num)) # split the text
    for word in words:  # for each word in the line:
        print(int(word)**2, end="") # print the word"""
    
"""def square_digits(num):
    return int(''.join(map(lambda x: str(int(x)*int(x)), str(num))))
    
    def sq(num):
    z = ''.join(str(int(i)**2) for i in str(num))
    return int(z)
"""
sqdigits(24)
