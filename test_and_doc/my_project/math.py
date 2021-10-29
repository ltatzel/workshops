"""
Module for calculating some means.

:author: Toto Titi <toto.titi@is.mpg.de>
"""


def arithmetic_mean(seq):
    """
    Method calculating the arithmetic mean of a sequence.

    :param iter seq: Sequence
    :return: Arithmetic mean
    :rtype: float
    """
    return sum(seq) / len(seq)


def geometric_mean(seq):
    """
    Method calculating the geometric mean of a sequence.

    :param iter seq: Sequence
    :return: Geometric mean
    :rtype: float
    """
    n = len(seq)

    if not n:
        raise ValueError("Sequence must have a least one element.")
    if any(e < 0 for e in seq):
        raise TypeError("Only positive numbers are allowed.")

    product = 1
    for e in seq:
        product = e * product
    return product ** (1 / n)


def harmonic_mean(seq):
    """
    Method calculating the harmonic mean of a sequence.

    Args:
        seq (iter): Sequence

    Returns:
        float: Harmonic mean
    """
    # This is just the inverse of the arithmetic mean
    # of the inverse data
    inv_seq = [1 / x for x in seq]
    return 1 / arithmetic_mean(inv_seq)
