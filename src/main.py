#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 02:56:02 2023

@author: green-machine

Subproject III. Capital Interactive
"""


from core.plot import plot_capital_retirement

# =============================================================================
# Alpha: Capital Retirement Ratio
# Pi: Investment to Capital Conversion Ratio
# =============================================================================
# =============================================================================
# Project: Interactive Capital Acquisitions
# =============================================================================
# =============================================================================
# capital_acquisitions.yaml
# =============================================================================
# =============================================================================
# Project: Interactive Capital Retirement
# =============================================================================
# =============================================================================
# capital_retirement.yaml
# =============================================================================


df = combine_capital_combined_archived()
MAP = {
    # =========================================================================
    # Nominal Product
    # =========================================================================
    'A191RC': 'PNU',
    # =========================================================================
    # Real Product
    # =========================================================================
    'A191RX': 'PRU',
    # =========================================================================
    # Labor
    # =========================================================================
    'bea_labor_mfg': 'LUU',
}
df.columns = MAP.values()
# =============================================================================
# Nominal Investment
# =============================================================================
df['IRU'] = df.iloc[:, 0].mul(df.iloc[:, 2]).div(df.iloc[:, 1])
# =============================================================================
# Maximum Nominal Product
# =============================================================================
df['PNM'] = df.iloc[:, 1].div(df.iloc[:, 5]).mul(100)
# =============================================================================
# Maximum Real Product
# =============================================================================
df['PRM'] = df.iloc[:, 2].div(df.iloc[:, 5]).mul(100)
# =============================================================================
# Fixed Assets, End-Period
# =============================================================================
df['CRU'] = df.iloc[:, 3].mul(df.iloc[:, 2]).div(df.iloc[:, 1])
df.iloc[:, (6, 1, 2, 8, 9, 4)].dropna(axis=0).pipe(
    calculate_capital_aquisition
)
df.iloc[:, (6, 1, 2, 9, 4)].dropna(axis=0).pipe(plot_capital_retirement)
df.iloc[:, (6, 7, 8, 9, 4)].dropna(axis=0).pipe(plot_capital_retirement)
