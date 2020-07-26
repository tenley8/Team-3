# Machine Learning Model for World-Wide Cases

## Overview
We are aiming to create a regression model that can explain the COVID-19 cases growth and fatality rate of countries world-wide depending on demographics data.

## Model
#### Pre-processing
Following steps are taking during pre-processing of data.
* Remove ACTIVE cases as results are unknown
* All gender with small number of data available are binned as "Other" for the reason stated in the [initial analysis](#Initial-Analysis)
* Encoding categorical variable to numeric variable
* 2 datasets were created using different dependent variables.
    * outcome: RECOVERED or FATAL
    * ever_hospitalized: 1 (yes) or 0 (no)
* Split dataset into a training and testing dataset using default setting (training: 75%, testing: 25%)
* Scaling dataset as population density and average income are relatively large values compared with other

#### ML Models
We tested the Neural Network Binary Classification Models and Random Forest Classifier (RF Model).
We believe the RF Model would be a better model choice for this analysis as;
* Both models had similar accuracy of around 90%
* Random Forest Classifier has better explainability and can show which dependent variable had more impact to the outcome.