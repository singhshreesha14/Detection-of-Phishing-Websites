**Project Title: Detection of Phishing Websites
 Description:**

This project aims to detect phishing websites using Machine Learning techniques. The system analyzes various characteristics of URLs to determine whether a website is legitimate or fraudulent. It helps users avoid malicious websites that attempt to steal sensitive information such as usernames, passwords, and credit card details.

The web application is built using Flask as the backend framework and integrates a Random Forest Classifier model trained on a CSV dataset containing URL-based features. The trained model predicts whether a given URL is “phishing” or “legitimate.”

The interface allows users to input a website URL, and upon submission, the model processes the input and returns the classification result in real time. The system thus provides a simple yet effective tool for enhancing online security awareness.

**Technologies Used:**

Python – Core programming language

Flask – Web framework for backend development

Machine Learning – RandomForestClassifier for classification

HTML, CSS – Frontend interface design

CSV Dataset – Stores URL features and training data

**Key Features:**

User-friendly web interface for entering URLs

Real-time phishing detection and result display

Machine learning model trained on phishing datasets

Easy to extend with new features or datasets

Fast and accurate classification

 **Future Enhancements:**

Integration with browser extensions for live protection

Addition of database storage (SQLite/MySQL)

Advanced visualization of phishing detection statistics

Deployment on cloud platforms (Heroku/AWS/GCP)
