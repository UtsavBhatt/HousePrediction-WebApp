# HousePrediction-WebApp
This repo consist of My ML project of predicting housing price and rent in city of Bombay. with 3D interactive map using streamlit.

Mumbai House Rent and Price Prediction Webapp
This is a web application that predicts the rental and purchase prices of houses in Mumbai, India. The app is built using Python, Streamlit, PyCaret, and CatBoost. It also features a 3D map of Mumbai.

Getting Started
To get started, you'll need to have Python 3.6 or higher installed on your machine. You'll also need to install Streamlit, PyCaret, and CatBoost. You can do this by running the following commands:

Copy code
pip install streamlit pycaret catboost
Once you have everything installed, you can run the app by navigating to the project directory in your terminal and running the following command:

arduino
Copy code
streamlit run app.py
This will launch the app in your web browser.

Usage
When you first launch the app, you'll be presented with a 3D map of Mumbai. You can use your mouse to zoom in and out and rotate the map. You can also click on any of the markers on the map to see information about the house at that location.

To make a prediction, simply enter the details of the house you're interested in (such as the number of bedrooms, bathrooms, and square footage) in the sidebar on the left. Once you've entered all the details, click the "Predict" button to see the predicted rental and purchase prices.

Model Details
The prediction model used in this app is a CatBoost model that has been tuned using PyCaret. The model takes into account a variety of features, including the number of bedrooms, bathrooms, square footage, and location.

Contributing
If you find a bug or would like to contribute to this project, please open an issue or a pull request on GitHub.


Acknowledgments
This project was inspired by the work of many data scientists and developers who have created similar apps and tools. Special thanks to the creators of Streamlit, PyCaret, and CatBoost for their contributions to the data science community.
