#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 03:16:06 2023

@author: green-machine

Subproject VIII. Complex
"""

df = combine_cobb_douglas().pipe(transform_cobb_douglas,
                                   year_base=1899).iloc[:, range(5)]

for col in df.columns:
    df.loc[:, [col]].pipe(plot_uscb_complex)

SERIES_IDS = (
    {'D0004': 'dataset_uscb.zip'}, {'D0130': 'dataset_uscb.zip'},
    {'F0003': 'dataset_uscb.zip'}, {'F0004': 'dataset_uscb.zip'},
    {'P0110': 'dataset_uscb.zip'}, {'U0001': 'dataset_uscb.zip'},
    {'U0008': 'dataset_uscb.zip'}, {'X0414': 'dataset_uscb.zip'},
    {'X0415': 'dataset_uscb.zip'}
)

for series_id in SERIES_IDS:
    print(f'Processing {series_id}')
    stockpile_usa_hist(series_id).pipe(plot_uscb_complex)