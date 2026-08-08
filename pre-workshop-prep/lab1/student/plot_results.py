import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from data_analysis import data, anova_results


def plot_results(data, anova_result):
    # Ensure output directory exists
    output_dir = "plots"
    os.makedirs(output_dir, exist_ok=True)

    electrodes = [
        "AF3", "AF4", "F3", "F4", "F7", "F8",
        "FC5", "FC6", "O1", "O2", "P7", "P8",
        "T7", "T8"
    ]

    summary = []

    for electrode in electrodes:
        for game in data["game"].unique():
            values = data[data["game"] == game][electrode].dropna()

            summary.append({
                "electrode": electrode,
                "game": game,
                "mean": values.mean(),
                "sem": values.sem()
            })

    summary = pd.DataFrame(summary)

    for electrode in electrodes:
        plot_data = summary[summary["electrode"] == electrode]

        plt.figure(figsize=(8, 5))

        ax = sns.barplot(
            data=plot_data,
            x="game",
            y="mean",
            errorbar=None
        )

        ax.errorbar(
            x=np.arange(len(plot_data)),
            y=plot_data["mean"],
            yerr=plot_data["sem"],
            fmt="none",
            capsize=5
        )

        result = anova_result[
            anova_result["electrode"] == electrode
        ].iloc[0]

        significance = "*" if result["significant"] else "NS"

        max_value = (plot_data["mean"] + plot_data["sem"]).max()
        
        x_center = (len(plot_data) - 1) / 2.0
        y_position = max_value + (abs(max_value) * 0.03)

        ax.text(
            x_center,
            y_position,
            significance,
            ha="center",
            va="bottom",
            fontsize=14
        )

        plt.title(f"{electrode} EEG Signal by Game")
        plt.xlabel("Game")
        plt.ylabel("Mean EEG Signal")
        plt.tight_layout()

        # Save plot to 'plots/' directory and close figure buffer
        file_path = os.path.join(output_dir, f"{electrode}_eeg_signal.png")
        plt.savefig(file_path, dpi=300)
        plt.close()

    print(f"Saved {len(electrodes)} plots to the '{output_dir}/' folder.")


plot_results(data, anova_results)