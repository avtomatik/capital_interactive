#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 02:40:19 2023

@author: green-machine

Subproject I. Approximation
"""

# =============================================================================
# 'plot_approx_linear': Linear Approximation,
# 'plot_approx_linear_log': Log-Linear Approximation,
# 'calculate_power_function_fit_params_a': Power Function Approximation,
# 'calculate_power_function_fit_params_b': Power Function Approximation,
# 'calculate_power_function_fit_params_c': Power Function Approximation
# =============================================================================

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

SERIES_IDS = ('Валовой внутренний продукт, млрд долл. США',)
stockpile_usa_mcconnel(SERIES_IDS).pipe(
    calculate_power_function_fit_params_a, (2800, 0.01, 0.5)
)

SERIES_IDS = (
    'Ставка прайм-рейт, %',
    'Национальный доход, млрд долл. США',
)
stockpile_usa_mcconnel(SERIES_IDS).pipe(
    calculate_power_function_fit_params_b, (4, 12, 9000, 3000, 0.87)
)

SERIES_IDS = (
    'Ставка прайм-рейт, %',
    'Валовой объем внутренних частных инвестиций, млрд долл. США',
)
stockpile_usa_mcconnel(SERIES_IDS).pipe(
    calculate_power_function_fit_params_c, (1.5, 19, 1.7, 1760)
)
