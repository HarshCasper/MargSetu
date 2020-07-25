# Data Modelling 

Data Modelling is implemented using a Doc2Vec model for matching course descriptions to job descriptions. It trains the model on a corpus of course descriptions (from the Coursera catalog). 
Then it evaluates the model by testing it out with a 
sample set of job descriptions for which relevant courses have already been pre-selected. Finally, the model is "pickled" for use by a Flask API. 

The Libraries and Modules used for this purpose are: 

- [Numpy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Gensim](https://pypi.org/project/gensim/)
- [Scipy Spatial](https://docs.scipy.org/doc/scipy/reference/spatial.html)
- [Pickle](https://docs.python.org/3/library/pickle.html)
