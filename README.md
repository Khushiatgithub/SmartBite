# 🍽️ SmartBite – AI-Powered Restaurant Website

A modern restaurant e-commerce platform with an integrated AI mood-based dish recommendation system.
SmartBite allows users to browse menus, explore dishes, and get personalized food suggestions based on their current mood, using a machine-learning model built with Python and Flask.

## 🚀 Features
### 🍔 Restaurant Website (Frontend)

Beautiful, responsive UI

Menu browsing

Category-wise dishes

Clean, modern layout

### 🤖 AI Mood-Based Dish Suggestion

User enters a mood (e.g., sad, happy, tired, stressed)

ML model predicts the mood category

System recommends the best dishes for that mood

Real-time response using Flask backend

Custom mapping of mood → dishes

### 🧠 Machine Learning Model

Trained using scikit-learn

Uses vectorizer + label encoder + LogisticRegression model

Mood classes: happy, sad, angry, tired, bored, stressed, excited

Easily extendable for more moods or dishes

### 🌐 Full-Stack Integration

Flask backend serves predictions

Frontend interacts through /predict route

Dynamic UI updates recommended dishes instantly

Screenshots of project:

![Picture1](https://i.postimg.cc/Kv60983w/Screenshot-2025-11-15-231301.png)


## 🛠️ Tech Stack
### Frontend

HTML

CSS

JavaScript

### Backend

Python

Flask Web Framework

### Machine Learning

scikit-learn

joblib

pandas

### Tools

VS Code

GitHub

Browser DevTools

## 🔧 Setup Instructions
### 1. Clone the repository
git clone https://github.com/Khushiatgithub/SmartBite.git
cd SmartBite

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the Flask Mood Model Server
cd model
python app.py


The backend will run on:

http://127.0.0.1:5000/

### 4. Use the Mood Predictor

Open your browser → enter a mood → get instant dish suggestions 🍽️🤩

## 🎉 Highlights

Designed SmartBite — an aesthetic restaurant e-commerce website

Implemented AI-powered mood recognition

Automatically suggests dishes based on how the user feels

Built using Flask, Machine Learning, and clean frontend UI




