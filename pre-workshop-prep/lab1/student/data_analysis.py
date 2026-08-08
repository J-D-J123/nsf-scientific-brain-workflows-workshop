###
# Name: Joseph Johnson 
# Date: 8/7/2026
#
# Description:
# This program performs a one-way ANOVA on EEG data from 14
# individual electrodes. The data is grouped by game/emotion
# condition (boring, calm, horror, and funny). For each electrode,
# the program compares the EEG signals between the four conditions
# and calculates an F-statistic and p-value. A result is considered
# statistically significant when the p-value is less than 0.05.
# The program prints and returns a table containing the ANOVA
# results for each electrode.
#
# AI tool: OpenAI ChatGPT 
# Percentage of code AI : 100%
# 
###

import pandas as pd
from scipy.stats import f_oneway

from data_acquisition import DATA_CONFIG, get_data


def run_anova(data):
    electrodes = [
        "AF3", "AF4", "F3", "F4", "F7", "F8",
        "FC5", "FC6", "O1", "O2", "P7", "P8",
        "T7", "T8"
    ]

    results = []

    for electrode in electrodes:
        groups = [
            group[electrode].dropna().values
            for _, group in data.groupby("game")
        ]

        f_stat, p_value = f_oneway(*groups)

        results.append({
            "electrode": electrode,
            "F-statistic": f_stat,
            "p-value": p_value,
            "significant": p_value < 0.05
        })

    results_df = pd.DataFrame(results)

    print("ANOVA Significance Results")
    print(results_df.to_string(index=False))

    return results_df


data = get_data(DATA_CONFIG)
anova_results = run_anova(data)