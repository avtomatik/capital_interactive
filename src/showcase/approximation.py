#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 02:40:19 2023

@author: green-machine

Subproject I. Approximation
"""

from linear import approximation_linear
from linear_log import approximation_linear_log

from thesis.src.lib.collect import stockpile_usa_mcconnel
from thesis.src.lib.tools import (calculate_power_function_fit_params_a,
                                  calculate_power_function_fit_params_b,
                                  calculate_power_function_fit_params_c)


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
    # =========================================================================
    # 'plot_approx_linear': Linear Approximation
    # =========================================================================
    approximation_linear()
    # =========================================================================
    # 'plot_approx_linear_log': Log-Linear Approximation
    # =========================================================================
    approximation_linear_log()
    power_function_fit()
