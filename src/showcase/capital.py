#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 02:50:18 2023

@author: green-machine

Subproject II. Capital
"""

# =============================================================================
# Project: Fixed Assets Dynamics Modelling:
# Fixed Assets Turnover Linear Approximation
# Gross Fixed Investment to Gross Domestic Product Ratio Linear Approximation
# Alpha: Investment to Capital Conversion Ratio Dynamics
# =============================================================================

# =============================================================================
# Original Result on Archived Data:
# =============================================================================
{
    's_1': -7.28110931679034e-05,
    's_2': 0.302917968959722,
}
# =============================================================================
# Original Result on Archived Data:
# =============================================================================
{
    'λ1': -0.000413347827690062,
    'λ2': 1.18883834418742,
}
df_a, df_b = collect_usa_investment_turnover_bls()
df_c, df_d = collect_usa_investment_turnover()
df_a.pipe(plot_model_capital, year_base=2005)
df_c.pipe(plot_model_capital, year_base=2012)
# =============================================================================
# Project: Discrete Fourier Transform based on Simpson's Rule Applied to Fixed Assets of the US
# =============================================================================
df_b.pipe(plot_fourier_discrete)
df_d.pipe(plot_fourier_discrete)
