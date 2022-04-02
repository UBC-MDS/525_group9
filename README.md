# DSCI 525 Group 9

## Introduction

In this project we work on a dataset containing daily rainfall in NSW, Australia from 1889 to 2014. In addition, the dataset contains daily rainfall predictions for this region obtained from various climate models in the World Climate Research Programme Coupled Model Intercomparison Project 6 (WCRP CMIP6). The dataset is about 6 GB in size, and various memory reducing techniques are explored to efficiently handle this data. After performing a simple EDA, it was found that about 5% of the data contains missing values, that the longitude/latitude grids the climate models span are slightly different, and that the models return a diverse array of predicted distributions of rainfall for each month. These factors will have to be taken into account when modelling, which is the ultimate goal of this project. In the future, we will build a cloud-deployed ensemble model that accepts the outputs of the climate models as features to predict daily rainfall in Australia.

## Contributors

- Daniel King (@danfke)
- Pavel Levchenko @plevchen)
- Rong Li (@lirnish)
- Sukhleen Kaur (@sukhleen999)

## References
Data for analysis of this project is taken from https://figshare.com/articles/dataset/Daily_rainfall_over_NSW_Australia/14096681
