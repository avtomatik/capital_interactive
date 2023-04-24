#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 03:34:11 2023

@author: green-machine

Subproject XII. USA Douglas & Kendrick
"""


from matplotlib import pyplot as plt

from thesis.src.common import get_fig_map_us_ma
from thesis.src.lib.plot import plot_cobb_douglas
from thesis.src.lib.pull import pull_series_ids_description
from thesis.src.lib.read import read_usa_hist
from thesis.src.lib.stockpile import stockpile_usa_hist
from thesis.src.lib.transform import transform_cobb_douglas


def plotSpecialLabels(archive_id, num, start, stop, step, title, measure, label):
    plt.figure(num)
    for _ in range(start, stop, step):
        plt.plot(read_usa_hist(
            archive_id, _MAP_SERIES.iloc[_, 0]), label=_MAP_SERIES.iloc[_, 1])
    plt.title(title)
    plt.xlabel('Period')
    plt.ylabel(measure)
    plt.grid()
    plt.legend(label)


_MAP_SERIES = pull_series_ids_description('dataset_usa_kendrick.zip')

plotSpecialLabels('dataset_douglas.zip', 21, 90, 115,
                  3, 'Birth Rates by Countries', 'Births Rate Per 1000 People', TITLES_EUR)
plt.show()

# =============================================================================
# projectUSADouglas0001.py
# =============================================================================



def plot_douglas(archive_name, num, start_at, stop, step, titles, measures):
    plt.figure(num)
    for _ in range(start_at, stop, step):
        plt.plot(read_usa_hist(
            archive_name, _MAP_SERIES.iloc[_, 0]), label=_MAP_SERIES.iloc[_, 1])
    plt.title(titles)
    plt.xlabel('Period')
    plt.ylabel(measures)
    plt.grid()
    plt.legend()


def plot_douglas_labels(archive_name, num, start_at, stop, step, titles, measures, label):
    plt.figure(num)
    for _ in range(start_at, stop, step):
        plt.plot(read_usa_hist(
            archive_name, _MAP_SERIES.iloc[_, 0]), label=_MAP_SERIES.iloc[_, 1])
    plt.title(titles)
    plt.xlabel('Period')
    plt.ylabel(measures)
    plt.grid()
    plt.legend(label)


_MAP_SERIES = pull_series_ids_description('dataset_douglas.zip')

plot_douglas('dataset_douglas.zip', 1, 0, 12, 1, TITLES[0], 'Percentage')
plot_douglas('dataset_douglas.zip', 2, 12, 23, 1, TITLES[1], 'Percentage')
plot_douglas('dataset_douglas.zip', 3, 23, 34, 1, TITLES[2], 'Percentage')
plot_douglas('dataset_douglas.zip', 4, 34, 45, 1, TITLES[3], 'Percentage')
plot_douglas('dataset_douglas.zip', 5, 45, 55, 1, TITLES[4], 'Percentage')
plot_douglas('dataset_douglas.zip', 6, 55, 66, 1, TITLES[5], 'Percentage')
plot_douglas('dataset_douglas.zip', 7, 66, 76, 1, TITLES[6], 'Percentage')
plot_douglas('dataset_douglas.zip', 8, 76, 86, 1, TITLES[7], 'Percentage')
plot_douglas('dataset_douglas.zip', 9, 86, 89, 1, TITLES[8], 'Percentage')
plot_douglas('dataset_douglas.zip', 10, 89, 90, 1, TITLES[9], 'Percentage')
plot_douglas('dataset_douglas.zip', 11, 90, 93, 1, TITLES[10], 'Rate Per 1000')
plot_douglas('dataset_douglas.zip', 12, 93, 96, 1, TITLES[11], 'Rate Per 1000')
plot_douglas('dataset_douglas.zip', 13, 96, 99, 1, TITLES[12], 'Rate Per 1000')
plot_douglas('dataset_douglas.zip', 14, 99, 102, 1, TITLES[13], 'Rate Per 1000')
plot_douglas('dataset_douglas.zip', 15, 102, 105, 1, TITLES[14], 'Rate Per 1000')
plot_douglas_labels('dataset_douglas.zip', 16, 105, 111, 1, TITLES[15], 'Rate Per 1000', TITLES_DEU)
plot_douglas('dataset_douglas.zip', 17, 111, 114, 1, TITLES[16], 'Rate Per 1000')
plot_douglas('dataset_douglas.zip', 18, 114, 117, 1, TITLES[17], 'Rate Per 1000')
plot_douglas('dataset_douglas.zip', 19, 117, 121, 1, TITLES[18], 'Mixed')
plot_douglas('dataset_douglas.zip', 20, 121, 124, 1, TITLES[19], 'Millions of Dollars')
plot_douglas_labels('dataset_douglas.zip', 21, 90, 115, 3, TITLES[20], 'Births Rate Per 1000 People', TITLES_EUR)
plt.show()

# =============================================================================
# projectUSAKendrick0001.py
# =============================================================================



_MAP_SERIES = pull_series_ids_description('dataset_usa_kendrick.zip')


plot_douglas('dataset_usa_kendrick.zip', 1, 0, 8, 1, TITLES[0], 'Dimension')
plot_douglas('dataset_usa_kendrick.zip', 2, 8, 19, 1, TITLES[1], 'Dimension')
plot_douglas('dataset_usa_kendrick.zip', 3, 19, 30, 1, TITLES[2], 'Dimension')
plot_douglas('dataset_usa_kendrick.zip', 4, 30, 38, 1, TITLES[3], 'Dimension')
plot_douglas('dataset_usa_kendrick.zip', 5, 38, 46, 1, TITLES[4], 'Dimension')
plot_douglas('dataset_usa_kendrick.zip', 6, 46, 54, 1, TITLES[5], 'Dimension')
# =============================================================================
# 'KTA10S07', 'KTA10S08' Not Working
# =============================================================================

plot_douglas('dataset_usa_kendrick.zip', 7, 54, 60, 1, TITLES[6], 'Dimension')
plot_douglas('dataset_usa_kendrick.zip', 8, 62, 72, 1, TITLES[7], 'Dimension')
plot_douglas('dataset_usa_kendrick.zip', 9, 72, 84, 1, TITLES[8], 'Dimension')
plot_douglas('dataset_usa_kendrick.zip', 10, 84, 96, 1, TITLES[9], 'Dimension')
plot_douglas('dataset_usa_kendrick.zip', 11, 96, 100, 1, TITLES[10], 'Dimension')
plot_douglas('dataset_usa_kendrick.zip', 12, 100, 111, 1, TITLES[11], 'Dimension')
plt.show()
# =============================================================================
# projectUSAKendrick0002.py
# =============================================================================



def plot_douglas(archive_name, num, start_at, stop, step, titles, measures):
    '''Same, But Flat Dictionary'''
    plt.figure(num)
    for _ in range(start_at, stop, step):
        plt.plot(read_usa_hist(
            archive_name, _MAP_SERIES.iloc[_, 0]), label=_MAP_SERIES.iloc[_, 0])
    plt.title(titles)
    plt.xlabel('Period')
    plt.ylabel(measures)
    plt.grid()
    plt.legend()


_MAP_SERIES = pd.read_csv('dataset_usa_kendrick.zip',
                          usecols=[4]).drop_duplicates()
_MAP_SERIES = _MAP_SERIES.reset_index(drop=True)

plot_douglas('dataset_usa_kendrick.zip',
             1, 0, 7, 1, 'Kendrick J.W. Indexes', 'Percentage')
plt.show()

# =============================================================================
# project_usa_douglas_kendrick.py
# =============================================================================


def plot_douglas(df, dictionary, num, start, stop, step, title, measure, label=None):
    """
    df: Source Database,
    dictionary: Dictionary of Series Codes to Series Titles from Source Database,
    num: Plot Number,
    start: Start Series Code,
    stop: Stop Series Code,
    step: Step for Series Codes,
    title: Plot Title,
    measure: Dimenstion for Series,
    label: Additional Sublabels"""
    plt.figure(num)
    for _ in range(start, stop, step):
        plt.plot(read_usa_hist(
            df, dictionary.iloc[_, 0]), label=dictionary.iloc[_, 1])
    plt.title(title)
    plt.xlabel('Period')
    plt.ylabel(measure)
    plt.grid()
    if label is None:
        plt.legend()
    else:
        plt.legend(label)
# =============================================================================
# Douglas European Demographics & Growth of US Capital
# =============================================================================

_MAP_SERIES = pull_series_ids_description('dataset_douglas.zip')

plot_douglas('dataset_douglas.zip', _MAP_SERIES, 1, 0, 12, 1, TITLES[0], 'Percentage')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 2, 12, 23, 1, TITLES[1], 'Percentage')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 3, 23, 34, 1, TITLES[2], 'Percentage')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 4, 34, 45, 1, TITLES[3], 'Percentage')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 5, 45, 55, 1, TITLES[4], 'Percentage')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 6, 55, 66, 1, TITLES[5], 'Percentage')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 7, 66, 76, 1, TITLES[6], 'Percentage')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 8, 76, 86, 1, TITLES[7], 'Percentage')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 9, 86, 89, 1, TITLES[8], 'Percentage')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 10, 89, 90, 1, TITLES[9], 'Percentage')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 11, 90, 93, 1, TITLES[10], 'Rate Per 1000')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 12, 93, 96, 1, TITLES[11], 'Rate Per 1000')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 13, 96, 99, 1, TITLES[12], 'Rate Per 1000')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 14, 99, 102, 1, TITLES[13], 'Rate Per 1000')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 15, 102, 105, 1, TITLES[14], 'Rate Per 1000')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 16, 105, 111, 1, TITLES[15], 'Rate Per 1000', TITLES_DEU)
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 17, 111, 114, 1, TITLES[16], 'Rate Per 1000')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 18, 114, 117, 1, TITLES[17], 'Rate Per 1000')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 19, 117, 121, 1, TITLES[18], 'Mixed')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 20, 121, 124, 1, TITLES[19], 'Millions of Dollars')
plot_douglas('dataset_douglas.zip', _MAP_SERIES, 21, 90, 115, 3, TITLES[20], 'Births Rate Per 1000 People', TITLES_EUR)
plt.show()

# =============================================================================
# Douglas Production Function
# =============================================================================
YEAR_BASE = 1899
plot_cobb_douglas(
    *stockpile_usa_hist(SERIES_IDS).pipe(transform_cobb_douglas, year_base=YEAR_BASE), get_fig_map_us_ma(YEAR_BASE))

# =============================================================================
# Kendrick Macroeconomic Series
# =============================================================================

_MAP_SERIES = pull_series_ids_description('dataset_usa_kendrick.zip')

plot_douglas('dataset_usa_kendrick.zip', _MAP_SERIES, 1, 0, 8, 1, TITLES[0], 'Millions Of 1929 Dollars')
plot_douglas('dataset_usa_kendrick.zip', _MAP_SERIES, 2, 8, 19, 1, TITLES[1], 'Millions Of 1929 Dollars')
plot_douglas('dataset_usa_kendrick.zip', _MAP_SERIES, 3, 19, 30, 1, TITLES[2], 'Millions Of Current Dollars')
plot_douglas('dataset_usa_kendrick.zip', _MAP_SERIES, 4, 30, 38, 1, TITLES[3], 'Millions Of 1929 Dollars')
plot_douglas('dataset_usa_kendrick.zip', _MAP_SERIES, 5, 38, 46, 1, TITLES[4], 'Thousands')
plot_douglas('dataset_usa_kendrick.zip', _MAP_SERIES, 6, 46, 54, 1, TITLES[5], 'Millions')
plot_douglas('dataset_usa_kendrick.zip', _MAP_SERIES, 7, 54, 60, 1, TITLES[6], 'Millions Of 1929 Dollars')
plot_douglas('dataset_usa_kendrick.zip', _MAP_SERIES, 8, 60, 72, 1, TITLES[7], 'Millions Of 1929 Dollars')
plot_douglas('dataset_usa_kendrick.zip', _MAP_SERIES, 9, 72, 84, 1, TITLES[8], 'Percentage')
plot_douglas('dataset_usa_kendrick.zip', _MAP_SERIES, 10, 84, 96, 1, TITLES[9], 'Percentage')
plot_douglas('dataset_usa_kendrick.zip', _MAP_SERIES, 11, 96, 100, 1, TITLES[10], 'Percentage')
plot_douglas('dataset_usa_kendrick.zip', _MAP_SERIES, 12, 100, 111, 1, TITLES[11], 'Percentage')
plot_douglas('dataset_usa_kendrick.zip', _MAP_SERIES, 13, 111, 118, 1, TITLES[12], 'Percentage')
plt.show()


# =========================================================================
# Douglas European Demographics & Growth of US Capital
# =========================================================================
ARCHIVE_NAME = 'dataset_douglas.zip'
# GROUP_ITERS = (
#     0,
#     12,
#     23,
#     34,
#     45,
#     55,
#     66,
#     76,
#     86,
#     89,
#     90,
#     93,
#     96,
#     99,
#     102,
#     105,
#     111,
#     114,
#     117,
#     121,
#     124,
#     90,
#     115,
# )
GROUP_ITERS = (
    # =====================================================================
    # TODO: Confirm
    # Table XXVII Birth, Death And Net Fertility Rates For Denmark, 1800-1931, Source: Danmarks Statistik, Statistisk Aarbog.
    # DT27BS01
    # DT27BS02
    # DT27BS03
    #
    # Table 62 Estimated Total British Capital In Terms Of The 1865 Price Level Invested Inside And Outside The United Kingdom By Years From 1865 To 1909, And Rate Of Growth Of This Capital
    # DT62AS01
    # DT62AS02
    # DT62AS03
    # DT62AS04
    #
    # Table 63 Growth Of Capital In The United States, 1880-1922
    # DT63AS01
    # DT63AS01
    # DT63AS02
    # =====================================================================
    0,
    12,
    23,
    34,
    45,
    55,
    66,
    76,
    86,
    89,
    90,
    93,
    96,
    99,
    102,
    105,
    111,
    114,
    117,
    121,
    124,
    99,
    124,
)
TITLES = (
    'Table I Indexes of Physical Production, 1899=100 [1899$-$1926]',
    'Table II Wholesale Price Indexes, 1899=100 [1899$-$1928]',
    'Table III Exchange Value = Ratio of Wholesale Prices to General Price Level: Nine Groups and Manufacturing [1899$-$1928]',
    'Table IV Relative Total Value Product for Nine Groups and All Manufacturing [1899$-$1926]',
    'Table V Employment Index: Nine Industries and Manufacturing, 1899$-$1927',
    'Table VI Value Product Per Employee: Nine Industries and Manufacturing, 1899$-$1926',
    'Table VII Index of Money Wages: Nine Groups and Manufacturing, 1899$-$1927',
    'Table VIII Index of Real Wages: Nine Groups and Manufacturing, 1899$-$1926',
    'Table 19 The Movement of Labor, Capital, and Product In\nMassachusetts Manufacturing, 1890$-$1926, 1899=100',
    'Table 24 The Revised Index of Physical Production for\nAll Manufacturing in the United States, 1899$-$1926',
    'Chart 67. Birth, Death, and Net Fertility Rates in Sweden, 1750$-$1931\nTable XXV Birth, Death and Net Fertility Rates for Sweden, 1750$-$1931,\nSource: Computed from data given in the Statistisk ?rsbok for Sverige.',
    'Chart 68. Birth, Death, and Net Fertility Rates in Norway, 1801$-$1931\nTable XXVI Birth, Death and Net Fertility Rates for Norway, 1801$-$1931,\nSource: Statistisk ?rbok for Kongeriket Norge.',
    'Chart 69. Birth, Death, and Net Fertility Rates in Denmark, 1800$-$1931\nTable XXVII Birth, Death and Net Fertility Rates for Denmark, 1800$-$1931,\nSource: Danmarks Statistik, Statistisk Aarbog.',
    'Chart 70. Birth, Death, and Net Fertility Rates in Great Britain, 1850$-$1932\nTable XXVIII Birth, Death and Net Fertility Rates for England and Wales, 1850$-$1932,\nSource: Statistical Abstract for the United Kingdom.',
    'Chart 71. Birth, Death, and Net Fertility Rates in France, 1801$-$1931\nTable XXIX Birth, Death and Net Fertility Rates for France, 1801$-$1931,\nSource: Statistique generale de la France: Mouvement de la Population.',
    'Chart 72$\'$. Birth, Death, and Net Fertility Rates in Germany, 1871$-$1931\nTable XXX Birth, Death And Net Fertility Rates For:\n(A) Germany, 1871$-$1931\n(B) Prussia, 1816$-$1930\nSource: Statistisches Jahrbuch fur das Deutsche Reich.',
    'Chart 73. Birth, Death, and Net Fertility Rates in Switzerland, 1871$-$1931\nTable XXXI Birth, Death and Net Fertility Rates for Switzerland, 1871$-$1931,\nSource: Statistisches Jahrbuch der Schweiz.',
    'Chart 74. Birth, Death, and Net Fertility Rates in Italy, 1862$-$1931\nTable XXXII Birth, Death and Net Fertility Rates for Italy, 1862$-$1931,\nSource: Annuario Statistico Italiano.',
    'Table 62 Estimated Total British Capital In Terms of the 1865 Price Level\nInvested Inside and Outside the United Kingdom by Years From\n1865 to 1909, and Rate of Growth of This Capital',
    'Table 63 Growth of Capital in the United States, 1880$-$1922',
    'Birth Rates by Countries',
)
TITLES_DEU = (
    'Germany Birth Rate', 'Germany Death Rate', 'Germany Net Fertility Rate',
    'Prussia Birth Rate', 'Prussia Death Rate', 'Prussia Net Fertility Rate',
)
TITLES_EUR = (
    'Sweden', 'Norway', 'Denmark', 'England & Wales', 'France', 'Germany',
    'Prussia', 'Switzerland', 'Italy',
)
MEASURES = (
    'Percentage',
    'Percentage',
    'Percentage',
    'Percentage',
    'Percentage',
    'Percentage',
    'Percentage',
    'Percentage',
    'Percentage',
    'Percentage',
    'Rate Per 1000',
    'Rate Per 1000',
    'Rate Per 1000',
    'Rate Per 1000',
    'Rate Per 1000',
    'Rate Per 1000',
    'Rate Per 1000',
    'Rate Per 1000',
    'Mixed',
    'Millions of Dollars',
    'Births Rate Per 1000 People',
)

LABELS = (
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    TITLES_DEU,
    None,
    None,
    None,
    None,
    TITLES_EUR,
)

plot_douglas(
    ARCHIVE_NAME,
    GROUP_ITERS[:-2],
    TITLES[:-1],
    MEASURES[:-1],
    LABELS
)
plot_douglas(
    ARCHIVE_NAME,
    GROUP_ITERS[-2:],
    (TITLES[-1],),
    (MEASURES[-1],),
    (LABELS[-1],),
    len(TITLES),
    3
)

# =========================================================================
# Douglas Production Function
# =========================================================================
# =========================================================================
# Cobb--Douglas Algorithm as per C.W. Cobb, P.H. Douglas. A Theory of Production, 1928 & P.H. Douglas. The Theory of Wages, 1934;
# =========================================================================
YEAR_BASE = 1899
MAP_FIG_US_MA = get_fig_map_us_ma(YEAR_BASE)
SERIES_IDS = {
    'DT19AS03': 'dataset_douglas.zip',
    'DT19AS02': 'dataset_douglas.zip',
    'DT19AS01': 'dataset_douglas.zip'
}
plot_cobb_douglas(
    *stockpile_usa_hist(SERIES_IDS).pipe(transform_cobb_douglas, year_base=YEAR_BASE), MAP_FIG_US_MA)
# =========================================================================
# Kendrick Macroeconomic Series
# =========================================================================
ARCHIVE_NAME = 'dataset_usa_kendrick.zip'
GROUP_ITERS = (
    0,
    8,
    19,
    30,
    38,
    46,
    54,
    60,
    72,
    84,
    96,
    100,
    111,
    118,
)
TITLES = (
    'Table A-I Gross And Net National Product, Adjusted Kuznets Concepts, Peacetime And National Security Version, 1869$-$1957 (Millions Of 1929 Dollars)',
    'Table A-IIa Gross National Product, Commerce Concept, Derivation From Kuznets Estimates, 1869$-$1957 (Millions Of 1929 Dollars)',
    'Table A-IIb Gross National Product, Commerce Concept, Derivation From Kuznets Estimates, 1869$-$1929; And Reconciliation With Kuznets Estimates, 1937, 1948, And 1953 (Millions Of Current Dollars)',
    'Table A-III National Product, Commerce Concept, By Sector, 1869$-$1957 (Millions Of 1929 Dollars)',
    'Table A-VI National Economy. Persons Engaged, By Major Sector, 1869$-$1957 (Thousands)',
    'Table A-X National Economy: Manhours, By Major Sector, 1869$-$1957 (Millions)',
    'Table A-XV National Economy: Real Capital Stocks, By Major Sector, 1869$-$1957 (Millions Of 1929 Dollars)',
    'Table A-XVI Domestic Economy And Private Sectors: Real Capital Stocks, By Major Type, 1869$-$1953 (Millions Of 1929 Dollars)',
    'Table A-XIX National Economy: Real Net Product, Inputs, And Productivity Ratios, Kuznets Concept, National Security Version, 1869$-$1957 (1929=100)',
    'Table A-XXII Private Domestic Economy. Real Gross Product, Inputs, And Productivity Ratios, Commerce Concept, 1869$-$1957 (1929=100)',
    'Table A-XXII: Supplement Private Domestic Economy: Productivity Ratios Based On Unweighted Inputs, 1869$-$1957 (1929=100)',
    'Table A-XXIII Private Domestic Nonfarm Economy: Real Gross Product, Inputs, And Productivity Ratios, Commerce Concept, 1869$-$1957 (1929=100)',
    'Table D-II. Manufacturing: Output, Labor Inputs, and Labor Productivity Ratios, 1869-1957 (1929=100)',
)
MEASURES = (
    'Millions Of 1929 Dollars',
    'Millions Of 1929 Dollars',
    'Millions Of Current Dollars',
    'Millions Of 1929 Dollars',
    'Thousands',
    'Millions',
    'Millions Of 1929 Dollars',
    'Millions Of 1929 Dollars',
    'Percentage',
    'Percentage',
    'Percentage',
    'Percentage',
    'Percentage',
)

plot_douglas(ARCHIVE_NAME, GROUP_ITERS, TITLES, MEASURES)
