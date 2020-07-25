import numpy as np
import pickle
from flask import Flask, request, Response, render_template, jsonify
import gensim
import pandas as pd

# Initializing the Flask Application
app = Flask('cr_app')

# Route 1: Shows a Form to the User to fill in
@app.route('/')
def home():
    return render_template('form.html')

# Route 2: Accept the Form Submission and process it
@app.route('/submit')
def submit():
    jd = request.args["JobDesc"] 
    doc = gensim.utils.simple_preprocess(jd) 
    model = pickle.load(open('./model.p', 'rb')) 
    vector = model.infer_vector(doc) 
    top = 5 
    sims = model.docvecs.most_similar([vector], topn=top)
    course_ids = [sim[0] for sim in sims] 
    df = pd.read_csv('./Data/Course_Data/Coursera_Catalog.csv') 
    course_names = [df.iloc[id]['name'] for id in course_ids] 
    course_descriptions = [df.iloc[id]['description'][0:150] + "..." for id in course_ids] 
    return render_template('results.html', len=top, names=course_names, descriptions=course_descriptions)

if __name__ == '__main__':
    app.run(debug=True)
