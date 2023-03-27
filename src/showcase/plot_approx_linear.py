#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:54:01 2023

@author: green-machine
"""

from lib.collect import stockpile_usa_bea
from lib.plot import plot_approx_linear


def main():
    """
    Project: Linear Approximation

    Returns
    -------
    None.

    """
    SERIES_IDS = {
        'A191RX': 'https://apps.bea.gov/national/Release/TXT/NipaDataA.txt',
        'A191RC': 'https://apps.bea.gov/national/Release/TXT/NipaDataA.txt',
        'A006RC': 'https://apps.bea.gov/national/Release/TXT/NipaDataA.txt',
        'A191RC': 'https://apps.bea.gov/national/Release/TXT/NipaDataA.txt'
    }
    stockpile_usa_bea(SERIES_IDS).dropna(axis=0).pipe(plot_approx_linear)


if __name__ == '__main__':
    main()
