#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 02:40:19 2023

@author: green-machine

Subproject I. Approximation
"""

from lib.collect import stockpile_usa_bea, stockpile_usa_mcconnel
from lib.plot import plot_approx_linear, plot_approx_linear_log
from lib.tools import (calculate_power_function_fit_params_a,
                       calculate_power_function_fit_params_b,
                       calculate_power_function_fit_params_c)


def linear_fit() -> None:
    """
    'plot_approx_linear': Linear Approximation,
    'plot_approx_linear_log': Log-Linear Approximation

    Returns
    -------
    None
        DESCRIPTION.

    """
    SERIES_IDS = {
        'A191RX': 'https://apps.bea.gov/national/Release/TXT/NipaDataA.txt',
        'A191RC': 'https://apps.bea.gov/national/Release/TXT/NipaDataA.txt',
        'A006RC': 'https://apps.bea.gov/national/Release/TXT/NipaDataA.txt',
        'A191RC': 'https://apps.bea.gov/national/Release/TXT/NipaDataA.txt'
    }
    stockpile_usa_bea(SERIES_IDS).dropna(axis=0).pipe(plot_approx_linear)

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


def power_function_fit() -> None:
    """
    'calculate_power_function_fit_params_a': Power Function Approximation,
    'calculate_power_function_fit_params_b': Power Function Approximation,
    'calculate_power_function_fit_params_c': Power Function Approximation

    Returns
    -------
    None
        DESCRIPTION.

    """
    SERIES_IDS = ('Валовой внутренний продукт, млрд долл. США',)
    PARAMS = (2800, 0.01, 0.5)
    stockpile_usa_mcconnel(SERIES_IDS).pipe(
        calculate_power_function_fit_params_a, PARAMS
    )

    SERIES_IDS = (
        'Ставка прайм-рейт, %',
        'Национальный доход, млрд долл. США',
    )
    PARAMS = (4, 12, 9000, 3000, 0.87)
    stockpile_usa_mcconnel(SERIES_IDS).pipe(
        calculate_power_function_fit_params_b, PARAMS
    )

    SERIES_IDS = (
        'Ставка прайм-рейт, %',
        'Валовой объем внутренних частных инвестиций, млрд долл. США',
    )
    PARAMS = (1.5, 19, 1.7, 1760)
    stockpile_usa_mcconnel(SERIES_IDS).pipe(
        calculate_power_function_fit_params_c, PARAMS
    )


if __name__ == '__main__':
    linear_fit()
    power_function_fit()
