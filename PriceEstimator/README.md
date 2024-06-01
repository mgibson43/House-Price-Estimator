## Capstone project for Western Governors University Bachelor's of Computer Science. 

https://priceestimator.fly.io

The project involved creating a machine learning model to solve a business problem. In this case, I chose to create a house price estimator using a large dataset.

I trained the model using supervised linear regression. The file where the training takes place can be found at the top level of the repository directory and is named "HousePriceEstimator.ipynb"

I then built a web application to allow myself and others to put the trained model to use. In the web app, the user must fill out a simple form to indicate what criteria they wish their desired house to have and submit the form. Once submitted, the web app will send the data to the back end through a POST request and the user will be sent to the estimation.html page. The data will be filtered to a format acceptable by the model for predictions. The model will then be fed the data and return a prediction which will be displayed on the estimation.html page.

User Guide
1.	Launch the application at https://priceestimator.fly.dev
2.	Fill out the form to match the type of house you are looking for.
a.	All fields must be filled.
b.	Use numerical input in the open fields.
c.	To select what city you wish to make an estimation in, you must first select a state to determine what cities are available.
3.	After all fields are filled out, click the “Estimate” button.
4.	You will be taken to a page that displays your range of house price estimations.
a.	If you wish to make another estimation, click on the “Make another estimation” button.
