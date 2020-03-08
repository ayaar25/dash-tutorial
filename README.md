# Dash Simple Interactive Bar Chart Tutorial

## Description
This repository consists of a source code written in python3 to visualise data of COVID-19 from South Korea that is available
on Kaggle within this [link](https://www.kaggle.com/kimjihoo/coronavirusdataset).

In this simple tutorial, you will see an interactive dashboard visualise the total suspects of COVID-19 in South Korea based
on gender and age. The data gained, unfortunately, contains lots of missing value or NaN for the columns 'sex' and 'age'.
Therefore, this dashboard visualisation only shows you about 5.7% of the real dataset.

![alt text](https://github.com/ayaar25/dash-tutorial/blob/master/pictures/dash-covid.gif "Dash Tutorial")

## Environment Set Up
Before you get the dashboard running, you need to first have python3 installed in your laptop. You can check this 
[link](https://realpython.com/installing-python/) for its installation.

After having python3 ready, you need to install dash and pandas python library by typing

```
pip install -r requirements.txt
```

## Run Dashboard
To run the program, on your terminal in the directory where the python file placed, type

```
python3 dash_tutorial.py
```

after that, you'll get this output on your terminal

```
Running on http://127.0.0.1:8050/
Debugger PIN: 775-976-572
 * Serving Flask app "dash_tutorial" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
```

Click on http://127.0.0.1:8050/ or type it on your browser and voila, you have your dashboard running.

