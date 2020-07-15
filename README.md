![header_pic](images/covid.png)

# Team-3 COVID-19 Analysis 

#### Table of Contents  

* [Background](#Background)
* [Project Overview](#project-overview)
* [Team](#Team)
* [Resources](#resources)
* [Database](#Database)
* [Machine Learning Model](#Machine-Learning-Models)
* [Summary](#summary)



## Test

## Background

Coronavirus disease 2019 (Covid-19) was first spotted in Wuhan, China and it rapidly spread out gobally within 2-3 months. As of July 2020, more than 11 million cases and 500k deaths have been reported across the world and the numbers of cases continues to increase. 

We selected the Covid-19 as the topic for our project, as better understanding of how the virus spread and how we can reduce a risk of fatality is crucial to reduce the pressure on our health care system and better prepare ourselves for the next outbreak of new viruses.

## Project Overview
This project aims to create the machine learning models which is capable of predicting the growth of Covid-19 cases and its fatality rate.

There are two sets of dataset available. One contains the number of cases and deaths by country (World Wide Dataset) and another that shows outcomes of individual cases in Ontario, Canada (Ontario Dataset).
We applied Regression model to World Wide Dataset to analyze correlations between Covid-19 spread and death by demographics. 
For Ontario Dataset, Neural network model was used to create a binary classifier that is capable of predicting the risk of the fatality depending on gender, age and region.

Some of the questions we are hoping to answer are;
- Age: Which age group has the highest risk of dying from Covid-19
- Gender: Which gender is at risk of contracting Covid-19
- Income: Do lower income communities (low GDP per Capita) have higher risk of contracting COVID-19?
- Health: Do people with pre-existing conditions have a greater risk of dying from COVID-19
- Lifestyle: What aspects of individual lifestyle such as weight, behaviour and proper nutrution impacts probability of catching Covid-19 or dying from Covid-19?

## Team
#### Members
* Joyce Ou
* Mohamed Ibrahim
* Momar Drame
* Tenley Wiltshire
* Taishi Matsuda

#### Communication Protocol
* Team-3 Slack - With any updates or questions
* Required Meeting - Every Tuesday Night, Thursday Night and Sunday Morning
* Optional Meeting - Friday Night, Saturday. To be scheduled based on the requirement.

## Resources
- **Software:** VS Code, Tableau, & JupyterLab  
- **Languages:** HTML, CSS, Python, JS 
- **Data Source:** [CovidWorldWide.csv](Resources\CovidWorldWide.csv) (World Wide Dataset), [Ontario.csv](Resources\Ontario.csv) (Ontario Dataset)


## Database
Database relationship diagram and data source are saved under [Resources Folder](Resources).
For first segment, csv files listed above are used, however, from the segment 2, PostgreSQL database will be used.

## Machine Learning Models
Mockup Machine Learning Model which predics the outcome of the individual who catched Covid-19 is created under [ML-Model-Ontario](ML-Model-Ontario).
The model already has 92% accuracy with minimum epochs and tunings. We will further work on fine-tuning the model in the next segment.

We are also planning to create another Regression Model that can predict the trend of how quickly the virus spread depending on the countries' GDP, Population, Age Distribution and etc.

[test](#Test)

## Summary 
TO BE UPDATED
