# Project Overview
We will explore the different Ontario Public Health Authority region's COVID-19 cases and implement a neural networks using the TensorFlow platform in Python. We will  implement a Deep neural networks using the Ontario.csv datasets, including image, natural language, and numerical datasets. 

## Resources
- **Data Source:** [Ontario.csv](https://data.ontario.ca/dataset/confirmed-positive-cases-of-covid-19-in-ontario/resource/455fd63b-603d-4608-8216-7d8647f43350)
- **Software:** Jupyter Notebook, Python 

## Objective
- Import, analyze, clean, and preprocess a “real-world” classification dataset
- Filter data by Public Health Units (PHU)
- Gather Dateframe information
- **Use Sklearn train_test_split method to split data into training and test**
    - X_train, X_test, y_train, y_test 
- **Prepare dataset for neural network model**
    - Normalize or standardize our numerical variables
- **Create a Keras Sequentail model(add layers) for our new neural network model**
    - The **nn_model** object will store the entire architecture of our neural network model
    - Add layers to our Sequential model using **Keras Dense class**
- **Compile Neural Network**

#### Instructions: Preprocess all numerical and categorical variables, as needed:
- Combine rare categorical values via bucketing.
- Encode categorical variables using one-hot encoding.
- Standardize numerical variables using Scikit-Learn’s StandardScaler class.
- Using a TensorFlow neural network design of your choice, create a binary classification model that can predict if an Alphabet Soup funded organization will be successful based on the features in the dataset. 
- Compile, train, and evaluate your binary classification model. Be sure that your notebook produces the following outputs:
   - Final model loss metric
   - Final model predictive accuracy
   
**Optimize  model training and input data to achieve a target predictive accuracy higher than 75%**