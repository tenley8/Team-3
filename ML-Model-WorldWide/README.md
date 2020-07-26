# Machine Learning Model for World-Wide Cases

## Overview
We are aiming to create a regression model that can explain the COVID-19 cases growth and fatality rate of countries world-wide depending on demographics data.

## Model
#### Pre-processing
Following steps are taking during pre-processing of data.
* Taken data from 100th day since the data of first case reported in each country
* Drop all rows with Null Data
* No Encoding was required as all values are numeric
* 2 datasets were created using different dependent variables.
    * Number of cases per Million
    * Fatality Rate (Total Deaths / Total Cases)
* Split dataset into a training and testing dataset using default setting (training: 80%, testing: 20%)

#### ML Models
Although the model was created using multiple linear regression model, R squared value is really low indicating that model was unable to explain the results.
During Segment 3, we will try testing Non-Linear model such as Random Forrest Regression model.