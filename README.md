# Data Analyst Intern Project: Twitter Data Analysis and Modeling

## Project Overview
This project demonstrates the end-to-end data processing and machine learning workflow using various AWS services. The key steps involved in the project are:

1. **Data Collection**: Web scraping Twitter posts using Selenium and storing the data in a CSV file.
2. **Data Storage**: Uploading the CSV data to Amazon S3 for secure and scalable storage.
3. **Data Preprocessing**: Creating a custom Python script in Visual Studio Code and executing it on an Amazon EMR cluster with the Spark framework to preprocess the data.
4. **Model Training**: Training two machine learning models (Random Forest and Gradient Boosting) using AWS SageMaker's Notebook Instance to predict the number of retweets for a given set of attributes.
5. **Model Deployment**: Deploying the trained model as a serverless function using AWS Lambda.
6. **API Development**: Creating an API using Amazon API Gateway to expose the model's predictions.

## Technologies and Services Used
- **Web Scraping**: Selenium
- **Data Storage**: Amazon S3
- **Data Processing**: Amazon EMR, Spark
- **Model Training**: AWS SageMaker
- **Model Deployment**: AWS Lambda
- **API Development**: Amazon API Gateway
- **Programming Language**: Python

