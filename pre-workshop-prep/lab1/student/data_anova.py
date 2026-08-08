###
# Name: Joseph Johnson 
# Date: 8/7/2026
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
            data[data["game"] == game][electrode].dropna()
            for game in data["game"].unique()
        ]

        f_stat, p_value = f_oneway(*groups)

        results.append({
            "Electrode": electrode,
            "F-statistic": f_stat,
            "p-value": p_value,
            "Significant": p_value < 0.05
        })

    results_df = pd.DataFrame(results)

    print("ANOVA Significance Results")
    print(results_df.to_string(index=False))

    return results_df


data = get_data(DATA_CONFIG)
anova_results = run_anova(data)