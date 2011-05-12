# -*- coding: utf-8 -*-
"""
This file houses static functions that are of general use.
"""

__author__ = "Brian Connelly <bdc@msu.edu>"
__credits__ = "Brian Connelly"

def mean(data):
    """Calculate the mean of a list of numbers

    Parameters:

    *data*
        a list of numbers whose mean to calculate

    """

    return float(sum(data))/len(data)

def std(data):
    """Calculate the standard deviation of a list of numbers

    Parameters:

    *data*
        a list of numbers whose standard deviation to calculate

    """
    m = mean(data)
    sumsq = 0

    for d in data:
        sumsq += (d - m)**2

    return (sumsq / len(data))**(0.5)

