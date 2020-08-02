![header_pic](images/covid.png)

# Team-3 COVID-19 Analysis 

#### Table of Contents  

* [Background](#Background)
* [Project Overview](#project-overview)
* [Resources](#resources)
* [Data Source and Database](#Data-Source-and-Database)
* [Machine Learning Model](#Machine-Learning-Models)
* [Presentation](#presentation)
* [Interactive Dashboards](#Interactive-Dashboards)
* [Findings and Recommendation](#Findings-and-Recommendation)

## Background

Coronavirus disease 2019 (Covid-19) was first spotted in Wuhan, China and it rapidly spread out globally within 2-3 months. As of July 2020, more than 11 million cases and 500k deaths have been reported across the world and the numbers of cases continues to increase. 

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

## Resources
- **Software:** VS Code, Tableau Public, JupyterLab, pgAdmin 4, Amazon Web Services & Google Slides
- **Languages:** HTML, CSS, Python, & PostgreSQL

## Data Source and Database
Details of data sources used, clean-up / data exploration process and the database relationship diagrams are describled under [Resources Folder](Resources).

## Machine Learning Models
Details of our machine learning (ML) models are explained under [Toronto Data Analysis](ML-Model_Toronto).

## Presentation
Please visit our [google slide presenation](https://docs.google.com/presentation/d/1YYGahoh_9MaWsczrZiGQP4bnX_7asvut2Ps5z8Q_0l4/edit?usp=sharing)

## Interactive Dashboards
**Worldwide COVID-19 Dashboard**
- Please visit our [visual dashboard](https://public.tableau.com/profile/tenley5222#!/vizhome/COVID-19_15942366549880/WorlwideCOVID-19?publish=yes), which presents a visual dashboard representation of Worlwide COVID-19 Dashboard.

**ML-Model Toronto Dashboard**
- Dashboard for Toronto Data is stored under [Dashboard Toronto](Dashboard_Toronto).

## Findings and Recommendation
Analysis performed for COVID-19 cases in Toronto indicates that the outcome of the COVID-19 could significantly depend on not only the age but demographic and ecnonomic factors.
However lack of availability of in-depth data prevents us from deriving further conclusion.

For further analysis, although only aggregated data is available, [World-Wide Data](ML-Model-WorldWide) may help us understand more about COVID-19.
