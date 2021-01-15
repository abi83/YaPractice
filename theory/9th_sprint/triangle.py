def returnsides(short_cathet):
    """
    >>> returnsides(1)
    (2, 1.73)
    >>> returnsides(2)
    (4, 3.46)
    >>> returnsides(3)
    (6, 5.2)
    """
    return 2*short_cathet, round((short_cathet**2 + 2*short_cathet**2)**(1/2),2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

