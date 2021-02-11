<center><h1 align="center">Boom-Bikes Bike Rentals.</h1></center>

<p>A US bike-sharing provider BoomBikes has recently suffered considerable dips in their revenues due to the ongoing Corona pandemic. The company is finding it very difficult to sustain in the current market scenario. So, it has decided to come up with a mindful business plan to be able to accelerate its revenue as soon as the ongoing lockdown comes to an end, and the economy restores to a healthy state. They also want to expand their business outside US. Hence they want their potential partners to forecast the number of bikes rented by customers in various conditions.</p>

<center><h1 align="center">Business Goal.</h1></center>
<p>The objective of this project is to model the demand for shared bikes with the available independent variables. It will be used by the management and potential partners to understand how exactly the demands vary with different features. They can accordingly manipulate the business strategy to meet the demand levels and meet the customer's expectations. Further, the model will be a good way for management to understand the demand dynamics of a new market. </p>

<center><h5 align="center"><a href="https://boombikes-prediction-api.herokuapp.com/">Click here to visit the home page</a></h6></center>
<center><h5 align="center"><a href="https://boombikes-prediction-api.herokuapp.com/index">Click here to visit the prediction page directly</a></h6></center>

<center><h3 align="center">Below is the preview of the application home-page.</h3></center>
<div align="center">
    <img src="/static/img/homepage.jpg" width="400px"/>
</div>

<center><h3 align="center">Below is the preview of the prediction page</h3></center>
<div align="center">
	<img src="/static/img/prediction.jpg" width="400px"/>
</div>


<center><h1 align="center">Components of the project.</h1></center>
<h3>Project is divided into 2 parts:</h3>
<h4>Part 1: Building Machine Learning Model and Prediction.</h4>
<ol type="1">
<li> Data: day.csv</li>
<li><a href="https://github.com/ds-souvik/Prediction-of-Bike-Rental-Count-Linear-Regression-and-Deployment-along-with-deployment/blob/master/BoomBikes%20Prediction%20model.ipynb">Boombikes Prediction model.ipynb: The notebook is divided into 3 parts</a>


	- Data understanding and Data cleaning.
	- Detailed EDA and inferences in every step.
	- Data Preparation for modelling.
	- Training the model.
	- Model Evaluation: p-value, VIF, r-squared, adjusted r squared, residual analysis.<br>
	- Hyper parameter tuning.<br>
	- Prediction and inferences.<br>
</li>
	</ol>
<h4>Part 2: Deployment.</h4>
<ol type="1">
<li>model.py: It mostly is the subpart of Boombikes Prediction model.ipynb having the code where model is built and trained. At the end the object of the trained model is saved in the memory of a pickle package.</li>
<li>app.py: It contains the code of my flask app. Flask is a micro web framework written in Python.</li>
Basic flow of the app:
</ol>
