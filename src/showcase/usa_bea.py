#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 03:18:46 2023

@author: green-machine

Subproject IX. USA BEA
"""

df = collect_usa_general()
# =============================================================================
# Project: Initial Version Dated: 05 October 2012
# =============================================================================
df.pipe(transform_investment_manufacturing).pipe(plot_investment_manufacturing)
# =============================================================================
# Project: Initial Version Dated: 23 November 2012
# =============================================================================
df.pipe(transform_investment).pipe(plot_investment)
# =============================================================================
# Project: Initial Version Dated: 16 June 2013
# =============================================================================
df.pipe(transform_manufacturing_money).pipe(plot_manufacturing_money)
# =============================================================================
# Project: Initial Version Dated: 15 June 2015
# =============================================================================
df.pipe(transform_d).pipe(plot_d)
# =============================================================================
# Project: Initial Version Dated: 17 February 2013
# =============================================================================
df_e_a, df_e_b = df.pipe(transform_e)
df_e_a.pipe(plot_e)
df_e_b.pipe(plot_e)
# =============================================================================
# Project: BEA Data Compared with Kurenkov Yu.V. Data
# =============================================================================
plot_kurenkov(df.pipe(combine_kurenkov))
