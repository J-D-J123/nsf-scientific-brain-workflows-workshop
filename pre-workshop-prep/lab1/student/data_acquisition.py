###
# Name: Joseph Johnson 
# Date: 8/7/2026
#
# AI tool: OpenAI ChatGPT 
# Percentage of code AI : 100%
# 
###

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