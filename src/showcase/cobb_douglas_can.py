#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 03:03:53 2023

@author: green-machine

Subproject V. Cobb--Douglas CAN
"""

# =============================================================================
# First Figure: Exact Correspondence with 'note_incomplete_th05_2014_07_10.docx'
# =============================================================================
MAP_FIG = {
    'fg_a': 'Chart I Progress in Manufacturing {}$-${} ({}=100)',
    'fg_b': 'Chart II Theoretical and Actual Curves of Production {}$-${} ({}=100)',
    'fg_c': 'Chart III Percentage Deviations of $P$ and $P\'$ from Their Trend Lines\nTrend Lines=3 Year Moving Average',
    'fg_d': 'Chart IV Percentage Deviations of Computed from Actual Product {}$-${}',
    'fg_e': 'Chart V Relative Final Productivities of Labor and Capital',
    'year_base': 2007,
}
ARCHIVE_IDS = {
    # =========================================================================
    # Capital
    # =========================================================================
    310004: (2007, "Geometric (infinite) end-year net stock", "industrial"),
    # =========================================================================
    # Labor : "v2523012", Preferred Over "v3437501" Which Is Quarterly
    # =========================================================================
    'v2523012': 2820012,
    # =========================================================================
    # Manufacturing
    # =========================================================================
    'v65201809': 3790031,
}
ARCHIVE_IDS = {
    # =========================================================================
    # Capital
    # =========================================================================
    36100096: (
        2012,
        "Manufacturing",
        "Linear end-year net stock",
        (
            "Non-residential buildings",
            "Engineering construction",
            "Machinery and equipment"
        )
    ),
    # =========================================================================
    # Labor : "v2523012", Preferred Over "v3437501" Which Is Quarterly
    # =========================================================================
    'v2523012': 14100027,
    # =========================================================================
    # Manufacturing
    # =========================================================================
    'v65201809': 36100434,
}
df = combine_can(ARCHIVE_IDS)
plot_cobb_douglas(
    *df.pipe(transform_cobb_douglas, year_base=2007),
    MAP_FIG
)
df.pipe(plot_cobb_douglas_3d)
# =============================================================================
# archive_id = 36100210
# df = read_can(archive_id)
# archive_id = 18100081
# df = read_can(archive_id)
# =============================================================================
