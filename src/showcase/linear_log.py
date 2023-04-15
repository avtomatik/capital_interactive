#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 16:01:47 2023

@author: green-machine
"""

from thesis.src.lib.collect import stockpile_usa_bea
from thesis.src.lib.plot import plot_approx_linear_log


def approximation_linear_log() -> None:
    """
    Project: Log-Linear Approximation

    Returns
    -------
    None.

    """
    SERIES_IDS = {
        'A191RX': 'https://apps.bea.gov/national/Release/TXT/NipaDataA.txt',
        'A191RC': 'https://apps.bea.gov/national/Release/TXT/NipaDataA.txt',
        'kcptotl1es00': 'https://apps.bea.gov/national/FixedAssets/Release/TXT/FixedAssets.txt',
        'A032RC': 'https://apps.bea.gov/national/Release/TXT/NipaDataA.txt'
    }
    stockpile_usa_bea(SERIES_IDS).dropna(axis=0).pipe(plot_approx_linear_log)

    SERIES_IDS = {
        'A191RX': 'https://apps.bea.gov/national/Release/TXT/NipaDataA.txt',
        'A191RC': 'https://apps.bea.gov/national/Release/TXT/NipaDataA.txt',
        'kcptotl1es00': 'https://apps.bea.gov/national/FixedAssets/Release/TXT/FixedAssets.txt',
        'A191RC': 'https://apps.bea.gov/national/Release/TXT/NipaDataA.txt'
    }
    stockpile_usa_bea(SERIES_IDS).dropna(axis=0).pipe(plot_approx_linear_log)


if __name__ == '__main__':
    approximation_linear_log()
