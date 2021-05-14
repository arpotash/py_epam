from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(0)
    []
    >>> fizzbuzz(-2)
    []
    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    """
    lst = []
    for num in range(1, n + 1):
        num_str = str(num)
        if num % 15 == 0:
            num_str = "fizzbuzz"
        elif num % 3 == 0:
            num_str = "fizz"
        elif num % 5 == 0:
            num_str = "buzz"
        lst.append(num_str)
    return lst
