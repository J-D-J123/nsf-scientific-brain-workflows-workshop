# COLAB 1: Building Your First Research Workflow

## Course architecture

Data acquisition ➡️ Data analysis ➡️ Visualizing results ➡️ Documenting research

**Platform Context:** Google Colab Cloud VM (Standard CPU Runtime)  
**Motivating Domain:** Brain-Machine Interfaces & Neural Signal Analysis  
**Target Open Dataset:** Neural Voltage Signals (Extracellular Spiking Arrays)

## Instructions for the student
In this lab, you will act as a Workflow Designer building an integrated, automated research workflow for a single experimental subject.

Your objective is to pass the explicit **"AI Prompt Challenges"** directly to an AI coding assistant, evaluate the structural properties of the returned functions, and paste them into the designated code boundaries. Once your 4 stages are connected, you will use the Stage 5 Laboratory Playground at the bottom of the notebook to test your workflow under different analysis settings!

## Module 1: Data acquisition
As an example, we will work with a dataset that contains EEG signals recorded from participants playing emotionally different computer games (boring, calm, horror, funny). We will download and analyze data from participant S01.

Student AI prompt challenge - using this dataset: https://www.kaggle.com/datasets/wajahat1064/emotion-recognition-using-eeg-and-computer-games?resource=download/

Copy and paste the code block from the cell below and the following text block into your AI assistant:

> "Write a function get_data(data_config) that takes the DATA_CONFIG below, reads each file with pandas using urls from the values, adds a game identifier to each file (the corresponding key), concatenates all dataframe into one and returns it."

```py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_CONFIG = {
    "boring": "https://github.com/cyneuro/CI-BioEng-Class/raw/refs/heads/main/emotion_recognition/data/S01G1AllChannels.csv",
    "calm": "https://github.com/cyneuro/CI-BioEng-Class/raw/refs/heads/main/emotion_recognition/data/S01G2AllChannels.csv",
    "horror": "https://github.com/cyneuro/CI-BioEng-Class/raw/refs/heads/main/emotion_recognition/data/S01G3AllChannels.csv",
    "funny": "https://github.com/cyneuro/CI-BioEng-Class/raw/refs/heads/main/emotion_recognition/data/S01G4AllChannels.csv"
}
```

``` TODO: make /student folder and name it data_acquisition.py ```


## Module 2: Data analysis
Student AI prompt challenge

Copy and paste the following text block into your AI assistant:

>    "Assume the columns of my dataframe are recordings from individual electrodes (AF3 to T8), with the identifier saved in the "game" column. Write a function run_anova(data) that takes each electrode in the data separately (AF3 to T8) and runs a simple ANOVA between the games. Print out the composite significance results table."

``` TODO: make /student folder and name it data_analysis.py ```

#### Student AI prompt challenge

Copy and paste the following text block into your AI assistant:

   > "Assume the columns of my dataframe are recordings from individual electrodes (AF3 to T8), with the identifier saved in the "game" column. Write a function run_anova(data) that takes each electrode in the data separately (AF3 to T8) and runs a simple ANOVA between the games. Print out the composite significance results table."

``` TODO: make /student folder and name data_anova.py ```

## Module 3: Visualizing results

#### Student AI prompt challenge

Copy and paste the following text block into your AI assistant:

> "Now write a function plot_results() that takes a dataframe in this format and makes a seabron histogram showing averages and SEMs. It should also take the anova_result table from the previous step and indicate significance with stars and no significance with NS."

``` TODO: make /student folder and name plot_results.py ```