#!/usr/bin/env python
# coding: utf-8

# # **COVID-19 Public Health Authority (PHU) cases Analysis**

# In[1]:


# Import our dependencies
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.graph_objects as go
import plotly.express as px


# #### **Import, analyze, clean, and preprocess a “real-world” classification dataset.**

# In[2]:


# Import our input dataset
df = pd.read_csv('./Resources/Ontario.csv')
df.head()


# #### **Inspect Data**

# In[3]:


# show number of columns and rows
df.shape


# In[4]:


# show DF Columns
df.columns


# In[5]:


# Return data types
df.dtypes


# #### **Clean Data**

# In[6]:


# Return columns with Null values 
for column in df.columns:
    print(f"Column {column} has {df[column].isnull().sum()} null values")


# In[7]:


# Retrun df duplicates
print(f"Duplicate entries: {df.duplicated().sum()}")


# ### **Aggregate data by Accurate_Episode_date**

# In[8]:


df .groupby(["Accurate_Episode_Date"]) .count()


# ### **Filter data by Public Health Units (PHU)**

# In[9]:


data_df = df .groupby(["Reporting_PHU", "Reporting_PHU_Latitude", "Reporting_PHU_Longitude"]) .count()["Row_ID"] .reset_index() .rename(columns={"Row_ID" : "Cases"})

data_df["OnsetWithin"] = "current day"

data_df


# #### **Gather Dateframe information**
# - Display dataframe
# - Display Categorical Variable list ('float64')
# - Display Column unique values 

# In[10]:


# Display Dataframe
df.head()


# #### **Display Variable List**

# In[11]:


# Categorical variable list
df_cat = df.dtypes[df.dtypes == "float64"].index.tolist()
df_cat


# In[12]:


# Unique numbers
df[df_cat].nunique()


# ### **Categorical Variables using one-hot encoding** 
# - One-hot encoding identifies all unique column values and splits the single categorical column into a series of columns, each containing information about a single unique categorical value
# - Although one-hot encoding is a very robust solution, it can be very memory-intensive. Therefore, categorical variables with a large number of unique values might become difficult to navigate or filter once encoded.

# ### **Bucketing or binning**
# **The process of reducing the number of unique categorical values in a dataset is known as bucketing or binning**
# - Bucketing data typically follows one of two approaches:
# - 1) Collapse all of the infrequent and rare categorical values into a single “other” category.
# - 2) Create generalized categorical values and reassign all data points to the new corresponding values

# 

# In[13]:


# Application type counts
Reporting_PHU_counts = df.Reporting_PHU.value_counts()
Reporting_PHU_counts


# In[14]:


# Visualize the value counts
Reporting_PHU_counts.plot.density()


# The **Reporting_PHU** columns variables appear a lot in of dataset, they are a feature of our model

# #### **Tasks**
# According to the density plot, the most common unique values have more than 1000 instances within the dataset. Therefore, we can bucket any occurence that appears fewer than 1000 times in the dataset as “other.” To do this, we’ll use a Python for loop and Pandas’ replace method. 
# - Determine which values to replace
# - Replace in DataFrame
# - Check to make sure binning was successful

# In[15]:


# replace values
replace_Reporting_PHU = list(Reporting_PHU_counts[Reporting_PHU_counts < 1000].index)

# use for loop to replace values
for i in replace_Reporting_PHU:
    df.Reporting_PHU  = df.Reporting_PHU.replace(i,"Other")

# Bucketing sucess
df.Reporting_PHU .value_counts()


# #### **Tasks**
# Now that we have reduced the number of unique values in the country variable, we’re ready to transpose the variable using one-hot encoding. The easiest way to perform **one-hot encoding** in Python is to use Scikit-learn’s **OneHotEncoder** module on the country variable. To build the encoded columns, we must **create an instance** of OneHotEncoder and **“fit”** the encoder with our values.

# In[16]:


# Create the OneHotEncoder instance
enc = OneHotEncoder(sparse=False)

# Fit the encoder and produce encoded DataFrame
PHU_df = pd.DataFrame(enc.fit_transform(df.Reporting_PHU.values.reshape(-1,1)))

# Rename encoded columns
PHU_df.columns = enc.get_feature_names(['Reporting_PHU'])
PHU_df.head()


# In[17]:


# Merge the two DataFrames,drop  Reporting_PHU column
# PHU_df = df.merge(encode_df,left_index=True,right_index=True).drop("Reporting_PHU",axis=1)


# #### **Dataframe information**
# - dataframe data type
# - variable list
# - column unique values

# In[18]:


PHU_df.dtypes


# In[19]:


# Categorical variable list
df_cat = PHU_df.dtypes[PHU_df.dtypes == "float64"].index.tolist()
df_cat


# In[20]:


# Unique numbers, must be < 10
PHU_df[df_cat].nunique()


# #### **Split our training and testing data**
# - We need to split our training and testing data before fitting our **StandardScaler instance**. This prevents testing data from influencing the standardization function.
# - To build our training and testing datasets, we need to separate two values:
# - input values (which are our independent variables commonly referred to as model features or “X” in TensorFlow documentation (Links to an external site.))
# - target output (our dependent variable commonly referred to as target or “y” in TensorFlow documentation)

# - **Use Sklearn train_test_split method to split data into training and test**
#     - X_train, X_test, y_train, y_test 
# - **Prepare dataset for neural network model**
#     - Normalize or standardize our numerical variables

# In[21]:


# Split our preprocessed data into our features and target arrays
y = PHU_df["Reporting_PHU_Ottawa Public Health"].values
X = PHU_df.drop(["Reporting_PHU_Ottawa Public Health","Reporting_PHU_Other"],1).values

# Split the preprocessed data into a training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)


# - **To apply our standardization, we need to create a StandardScaler instance by adding and running the following code:**
# - **Once we have our StandardScalerinstance, we need to fit the input data by adding and running the next line of code:**
#     - Create StandardScaler instance
#     - fit the StandardScaler
#     - Scale the data**

# In[22]:


# Create a StandardScaler instance
scaler = StandardScaler()

# Fit the StandardScaler
X_scaler = scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)


# #### **Tasks**
# At last, our data is preprocessed and separated and ready for modelling. For our purposes, we will use the same framework we used for our basic neural network:
# - For our input layer, we must add the number of input features equal to the number of variables in our feature DataFrame.
# - In our hidden layers, our deep learning model structure will be slightly different—we’ll add two hidden layers with only a few neurons in each layer. To create the second hidden layer, we’ll add another Keras Dense class while defining our model. All of our hidden layers will use the relu activation function to identify nonlinear characteristics from the input values.
# - In the output layer, we’ll use the same parameters from our basic neural network including the sigmoid activation function. The sigmoid activation function will help us predict the probability that an employee is at risk for attrition.

# #### **Define Model**
# - Deep neural net
# - First hidden layer
# - Second hidden layer
# - Output layer
# - Check the structure of the model

# In[23]:


# Define the model - deep neural net
number_input_features = len(X_train[0])
hidden_nodes_layer1 =  8
hidden_nodes_layer2 = 5

nn = tf.keras.models.Sequential()

# First hidden layer
nn.add(
    tf.keras.layers.Dense(units=hidden_nodes_layer1, input_dim=number_input_features, activation="relu")
)

# Second hidden layer
nn.add(tf.keras.layers.Dense(units=hidden_nodes_layer2, activation="relu"))

# Output layer
nn.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))

# Check the structure of the model
nn.summary()


# Now it is time to compile our model and define the loss and accuracy metrics. Since we want to use our model as a binary classifier, we’ll use the **binary_crossentropy loss function**, **adam optimizer**, and **accuracy metrics**, which are the same parameters we used for our basic neural network. To compile the model, add and run the following code:

# #### **Compile neural network**
# - Use **adam optimizer**, which uses a gradient descent approach to ensure that the algorithm will not get stuck on weaker classifying variables and feature
# - The **loss metric** is used by machine learning algorithms to score the performance of the model through each iteration and **epoch** by evaluating the inaccuracy of a single input.
# - Use **binary_crossentropy**, which is specifically designed to evaluate a binary classification mode

# In[24]:


# Compile the model
nn.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])


# #### **Train Model**
# Training and evaluating the deep learning model is no different from a basic neural network. Depending on the complexity of the dataset, we may opt to increase the number of epochs to allow for the deep learning model more opportunities to optimize the weight coefficients. To train our model, we must add and run the following code:

# In[25]:


# Train the model
fit_model = nn.fit(X_train,y_train,epochs=100) #epochs (run through the data)


# In[26]:


# Evaluate the model using the test data
model_loss, model_accuracy = nn.evaluate(X_test,y_test,verbose=2)
print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")


# #### **Summary**

# Looking at the performance metrics from the model, the neural network was able to correctly classify each of the points in the test data. In other words, the model was able to correctly classify data it was not trained on **94%** of the time. Although perfect model performance is ideal, more complex datasets and models may not be able to achieve 100% accuracy. Therefore, it is important to establish model performance thresholds before designing any machine learning mode. As seen from the results of the **Deep Learning** model metrics, the observation made was that the model correctly identified **Ontario Public Health Autority** data to be **94%** accurate

# - **Create a Keras Sequentail model(add layers) for our new neural network model**
#     - The **nn_model** object will store the entire architecture of our neural network model
#     - Add layers to our Sequential model using **Keras Dense class**
# - **Compile Neural Network**

# In[27]:


# Define model
nn.summary()


# **The summary returned the number of weight parameters for each layer which equals to the number of input valuse by the number of neurons**

# In[28]:


# Define the model - deep neural net
number_input_features = len(X_train[0])
hidden_nodes_layer1 =  8
hidden_nodes_layer2 = 5

nn = tf.keras.models.Sequential()

# First hidden layer
nn.add(
    tf.keras.layers.Dense(units=hidden_nodes_layer1, input_dim=number_input_features, activation="relu")
)

# Second hidden layer
nn.add(tf.keras.layers.Dense(units=hidden_nodes_layer2, activation="relu"))

# Output layer
nn.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))

# Check the structure of the model
nn.summary()


# In[29]:


# Compile the model
nn.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])


# In[30]:


# Train the model
fit_model = nn.fit(X_train,y_train,epochs=200)


# In[31]:


# Evaluate the model using the test data
model_loss, model_accuracy = nn.evaluate(X_test,y_test,verbose=2)
print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")


# After adding more epochs (200) and running it again; the deep learning model's performance metrics indicated that the model returned the same results as the first one

# ### **Plot PHU Hotspots in Ontario Canada**

# In[32]:


from plotly.offline import plot
import plotly.graph_objs as go
fig = px.scatter_mapbox(data_df, lat="Reporting_PHU_Latitude", lon="Reporting_PHU_Longitude",  
            color="OnsetWithin", 
            color_discrete_sequence=["red", "darkblue", "yellow", "white"], 
            size="Cases", hover_name="Reporting_PHU", 
            size_max=28, zoom=5.4, 
            center=dict(lat=45,lon=-79.4), 
            height=800, 
            labels={"OnsetWithin" : "Onset w/in Date"},
            title=" Confirmed Cases per Public Health Unit" )
fig.update_layout(mapbox_style="open-street-map")
fig.show()
plot(fig, auto_open=True)


# In[ ]:




