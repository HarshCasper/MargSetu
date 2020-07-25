# Exploratory Data Analysis 

In this Module, Test Datasets have been created to check out the efficiency of our Model. This notebook `Job_Posts_EDA.ipynb` examines the dataset of 
job posts from Glassdoor. It finds that there are issues in this dataset, such as duplicate rows and adverstisements mixed in. However, because
only a small portion of this data is used for testing out the recommender model, these issues will not affect the project and do not need to be fixed here.

Later a small set of labeled data is taken in `Create_Test_Set.ipynb` that can be used to test the Doc2Vec model. Specifically, 10 sample job descriptions under 2 job titles (data scientist and data 
engineer) are selected. It matches each of these 2 job titles with 5 courses that I believe the model should recommend. 
This sample data will then be used to test the accuracy of the model.

