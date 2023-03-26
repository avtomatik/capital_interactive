#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 02:59:11 2023

@author: green-machine

Subproject IV. Cobb--Douglas
"""

# =============================================================================
# On Original Dataset
# =============================================================================
df = stockpile_cobb_douglas(5)

# =============================================================================
# On Expanded Dataset
# =============================================================================
df_d, df_e = collect_usa_manufacturing_two_fold()
df_f, df_g, df_h = collect_usa_manufacturing_three_fold()

df.iloc[:, range(3)].pipe(plot_cobb_douglas_complex)
df.iloc[:, (0, 1, 3)].pipe(plot_cobb_douglas_complex)
df.iloc[:, (0, 1, 4)].pipe(plot_cobb_douglas_complex)
# =============================================================================
# No Capacity Utilization Adjustment
# =============================================================================
df_d.pipe(plot_cobb_douglas_complex)
# =============================================================================
# Capacity Utilization Adjustment
# =============================================================================
df_e.pipe(plot_cobb_douglas_complex)
# =============================================================================
# Option: 1929--2013, No Capacity Utilization Adjustment
# =============================================================================
df_f.pipe(plot_cobb_douglas_complex)
# =============================================================================
# Option: 1967--2013, No Capacity Utilization Adjustment
# =============================================================================
df_g.pipe(plot_cobb_douglas_complex)
# =============================================================================
# Option: 1967--2012, Capacity Utilization Adjustment
# =============================================================================
df_h.pipe(plot_cobb_douglas_complex)
collect_usa_manufacturing_latest().pipe(plot_cobb_douglas_complex)
