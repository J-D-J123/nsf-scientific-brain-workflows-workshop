
Copy of Colab1_Automation.ipynb_
COLAB 1: Building Your First Research Workflow
Course architecture

Data acquisition ➡️ Data analysis ➡️ Visualizing results ➡️ Documenting research

Platform Context: Google Colab Cloud VM (Standard CPU Runtime)
Motivating Domain: Brain-Machine Interfaces & Neural Signal Analysis
Target Open Dataset: Neural Voltage Signals (Extracellular Spiking Arrays)
Instructions for the student

In this lab, you will act as a Workflow Designer building an integrated, automated research workflow for a single experimental subject.

Your objective is to pass the explicit "AI Prompt Challenges" directly to an AI coding assistant, evaluate the structural properties of the returned functions, and paste them into the designated code boundaries. Once your 4 stages are connected, you will use the Stage 5 Laboratory Playground at the bottom of the notebook to test your workflow under different analysis settings!
Module 1: Data acquisition

As an example, we will work with a dataset that contains EEG signals recorded from participants playing emotionally different computer games (boring, calm, horror, funny). We will download and analyze data from participant S01.
Student AI prompt challenge

Copy and paste the code block from the cell below and the following text block into your AI assistant:

    "Write a function get_data(data_config) that takes the DATA_CONFIG below, reads each file with pandas using urls from the values, adds a game identifier to each file (the corresponding key), concatenates all dataframe into one and returns it."

[ ]
[ ]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_CONFIG = {
    "boring": "https://github.com/cyneuro/CI-BioEng-Class/raw/refs/heads/main/emotion_recognition/data/S01G1AllChannels.csv",
    "calm": "https://github.com/cyneuro/CI-BioEng-Class/raw/refs/heads/main/emotion_recognition/data/S01G2AllChannels.csv",
    "horror": "https://github.com/cyneuro/CI-BioEng-Class/raw/refs/heads/main/emotion_recognition/data/S01G3AllChannels.csv",
    "funny": "https://github.com/cyneuro/CI-BioEng-Class/raw/refs/heads/main/emotion_recognition/data/S01G4AllChannels.csv"
}

def get_data(data_config):
    dataframes = []

    for game, url in data_config.items():
        df = pd.read_csv(url)
        df["game"] = game
        dataframes.append(df)

    return pd.concat(dataframes, ignore_index=True)

data = get_data(DATA_CONFIG)
print(data.head())
print(data["game"].value_counts())

       AF3      AF4       F3       F4       F7        F8      FC5     FC6  \
0 -33.0205 -15.1846 -42.1795   1.6872  42.1793  -1.68720  -5.5436 -3.6154   
1 -28.6291 -20.0583 -42.5410 -10.4653  35.3100 -15.68600 -19.3110 -2.4344   
2 -21.8497 -10.9006 -32.0346  -2.3656  39.6993  -0.64483  -4.0523 -1.0830   
3 -25.1185 -10.9702 -32.7641  -3.4287  32.7378   4.69650  -8.6299 -1.7412   
4 -19.0316  -9.5886 -29.1108  -3.9459  35.3533   0.79929 -12.6914  1.0144   

        O1       O2       P7       P8       T7       T8  Unnamed: 14    game  
0  25.7899 -9.88190   5.5436  7.47180  11.8101  17.1128          NaN  boring  
1  17.4933  3.24420  18.7081  5.09510  17.3683   3.0708          NaN  boring  
2  26.8081 -3.45840   8.1861  8.40480  15.1209   9.3940          NaN  boring  
3  16.7637 -9.75860   1.1868  0.91086   4.3315   8.1073          NaN  boring  
4  13.1068 -0.73692   8.1054 -1.31300   8.1694   8.3442          NaN  boring  
game
boring    38252
calm      38252
horror    38252
funny     38252
Name: count, dtype: int64

Module 2: Data analysis
[ ]

pip install scipy

Requirement already satisfied: scipy in /usr/local/lib/python3.12/dist-packages (1.16.3)
Requirement already satisfied: numpy<2.6,>=1.25.2 in /usr/local/lib/python3.12/dist-packages (from scipy) (2.0.2)

[ ]


Student AI prompt challenge

Copy and paste the following text block into your AI assistant:

    "Assume the columns of my dataframe are recordings from individual electrodes (AF3 to T8), with the identifier saved in the "game" column. Write a function run_anova(data) that takes each electrode in the data separately (AF3 to T8) and runs a simple ANOVA between the games. Print out the composite significance results table."

[ ]

from scipy.stats import f_oneway
import pandas as pd

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

[ ]

anova_result = run_anova(data)

ANOVA Significance Results
Electrode  F-statistic  p-value  Significant
      AF3     0.001111 0.999949        False
      AF4     0.012042 0.998194        False
       F3     0.040109 0.989291        False
       F4     0.008768 0.998874        False
       F7     0.006097 0.999346        False
       F8     0.081791 0.969952        False
      FC5     0.011744 0.998260        False
      FC6     0.041308 0.988820        False
       O1     0.012095 0.998181        False
       O2     0.055138 0.982970        False
       P7     0.077225 0.972321        False
       P8     0.017965 0.996726        False
       T7     0.037164 0.990423        False
       T8     0.002724 0.999804        False

Module 3: Visualizing results
Student AI prompt challenge

Copy and paste the following text block into your AI assistant:

    "Now write a function plot_results() that takes a dataframe in this format and makes a seabron histogram showing averages and SEMs. It should also take the anova_result table from the previous step and indicate significance with stars and no significance with NS."

[ ]

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_results(data, anova_result):
    electrodes = [
        "AF3", "AF4", "F3", "F4", "F7", "F8",
        "FC5", "FC6", "O1", "O2", "P7", "P8",
        "T7", "T8"
    ]

    # Calculate the mean and SEM for each game and electrode
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

    # Create a plot for each electrode
    for electrode in electrodes:
        plot_data = summary[summary["electrode"] == electrode]

        plt.figure(figsize=(8, 5))

        ax = sns.barplot(
            data=plot_data,
            x="game",
            y="mean",
            errorbar=None
        )

        # Add SEM error bars
        ax.errorbar(
            x=np.arange(len(plot_data)),
            y=plot_data["mean"],
            yerr=plot_data["sem"],
            fmt="none",
            capsize=5,
            color="black"
        )

        # Get ANOVA significance result for this electrode
        result = anova_result[
            anova_result["Electrode"] == electrode
        ].iloc[0]

        if result["Significant"]:
            significance = "*"
        else:
            significance = "NS"

        # Add significance label above the plot
        max_value = (plot_data["mean"] + plot_data["sem"]).max()

        ax.text(
            1.5,
            max_value,
            significance,
            ha="center",
            va="bottom",
            fontsize=14
        )

        plt.title(f"{electrode} EEG Signal by Game")
        plt.xlabel("Game")
        plt.ylabel("Mean EEG Signal")
        plt.tight_layout()
        plt.show()

[ ]

plot_results(data, anova_result)

Module 4: Documenting research
Student AI prompt challenge

Copy and paste the code block from the cell below and the following text block into your AI assistant:

    "Assume the anova table from above is saved in the anova_result variable. Write a documentation logging function document_reserach that creates a pandas dataframe with the following columns: current date, number of singificant (p < 0.05) electrodes and returns it."

[ ]

# TODO: Your code here

[ ]

document_research(anova_result)

Embedded playground

Task 1. Hypothesize which two game types could produce vastly different emotional responses and re-run the analyses only for these game types.

Task 2. Use AI to add basic preprocessing (re-referencing, filtering) to the workflow after obtaining the data and before running ANOVA. Does it affect the significance results?
[ ]

data = get_data(DATA_CONFIG)
anova_result = run_anova(data)
plot_results(data, anova_result)
document_research(anova_result)

Colab paid products
-
Cancel contracts here
