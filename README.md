# MargSetu

<p align="center">
  <a href="https://github.com/HarshCasper/MargSetu">
    <img src="https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera.s3.amazonaws.com/media/coursera-logo-square.png?auto=format%2Ccompress&dpr=1" alt="Logo" width="150" height="150">
  </a>

## 📌 Introduction

This Web Application powered by Machine Learning and Flask API is a Recommender System which can be used to recommend <b>Massive Open Online Courses (MOOCs)</b> to Students and 
Professionals according to their needs and proficiency. The [Dataset](https://github.com/HarshCasper/MargSetu/tree/master/Data) used to process the Data Model and power the Application has been scrapped from Coursera's Public Catalog which consists of more than 4000+ Courses in various domains like Data Scientist, DevOps Engineers and Cloud Development Roles. Using Gensim for developing Natural Language Processing Model, a Doc2Vec Model was used to generate predictions for a given role. 

## 🎯 Purpose of the Project

 <b>Massive Open Online Courses (MOOCs)</b> are increasingly being relied on by Students and Professionals to learn new skills and get the know-how of various technologies and toolkits. While this has allowed the awareness among people, this has also led them to take multiple unreliable course materials that simply don't do justice to people. This Machine Learning Application tries to recommend the appropriate courses to Students and Professionals according to the Job-Profile they are aiming for. 
 
 Our Model performs fairly well when it comes to recommending the appropriate courses and hence allows the right recommendations to be generated as per the technology or tooling that someone is aiming to learn.
 
 ## 🏁 Technology Stack

* [Flask](https://github.com/pallets/flask)
* [HTML](https://www.w3.org/TR/html52/)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Gensim](https://pypi.org/project/gensim/) 
* [Pandas](https://pandas.pydata.org/)

## 🏃‍♂️ Local Installation

1. Drop a ⭐ on the Github Repository. 
2. Clone the Repo by going to your local Git Client and pushing in the command: 

```sh
https://github.com/HarshCasper/MargSetu.git
```

3. Install the Packages: 
```sh
pip install -r requirements.txt
```

4. At last, push in the command:
```sh
python app.py
```

5. Go to ` http://127.0.0.1:5000/` and enjoy the application.

## 📋 Further Changes to be Done

- [ ] Deploying the Web Application on Cloud.
- [ ] Development of the Model using Tensorflow/PyTorch.
- [ ] Enhance the User-Interface using HTML/CSS.
- [ ] Set the Application on Docker.
- [ ] Improve the Quality of Predictions.
- [ ] Add a more interactive User-Interface and integrate various other parameters.

## 📜 LICENSE

[MIT](https://github.com/HarshCasper/MargSetu/blob/master/LICENSE)
