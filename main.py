from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydeck as pdk

def predict_rent(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    
    return predictions_data['Label'][0]
    
model = load_model('my_best_catboost')

use_data = pd.read_csv("prop_data_clean.csv")
locales = list(pd.unique(use_data['locality']))

with st.sidebar: 
    st.image("pngwing.com.png")
    st.title("PredictHouseUtsavML")

st.title('Mumbai House Prices & Rent predictions in 2023') 
st.write("By Utsav Bhatt")
st.image('skyline.jpg')
st.write('The rent predictions of all the areas are predicted by a AI model\
          which uses tuned catboost model that was adjusted for the inflation in 2023\
         As the dataset available was from 2018 a lot of preprocessing and maniupilation\
         was done in order to create this datapipline.')

def mini (Bedroom):
    min_val = {0:10.0 ,1: 300.0, 2 : 600.0, 3 :900.0, 4:1200.0, 5:1500.0, 6:2000.0, 7:2500.0, 8:3000.0, 9:3700.0, 10:4200.0}
    for i in min_val:
        if i == Bedroom:
            minimum = min_val[i]
            return(minimum)
        
Bathrooms = int(st.sidebar.number_input("Number of Bathrooms", min_value=1, 
                                  max_value=10,
                                 value=5,
                                 step=1, help="Please select relevant number of bathrooms in correspondance to area."))


Bedrooms = int(st.sidebar.number_input("Number of Bedrooms", min_value=0, 
                                  max_value=10,
                                 value=5,
                                 step=1, help="Please select relevant number of bathrooms"))

val = mini(Bedrooms)

Area = int(st.sidebar.slider(label = 'Area in SqFt', min_value = val,
                          max_value = 9500.0 ,
                          value = val,
                          step = 5.0))

Locality = st.sidebar.selectbox(label="Locality", options= locales)

features = {'area': Area, 'bathroom_num': Bathrooms, 'bedroom_num': Bedrooms, 'locality': Locality}

feature_data = pd.DataFrame([features])
st.table(feature_data)  


apts = use_data[use_data['locality'] == Locality]
other_apts = apts.drop([ 'id','city','trans','url','post_date','id_string','title',
                         'furnishing', 'user_type', 'floor_count','type','floor_num'], axis=1).dropna()

Map = st.sidebar.button('Show Map', help= 'Drag the map to selected location.')

if Map == True:
    st.subheader("Implementation of 3D interavtive map that shows 3D bars where price is highest amongst selected Locality.")
    st.write(pdk.Deck(map_style="mapbox://styles/mapbox/light-v9", 
                  initial_view_state = pdk.ViewState(latitude= 19.009161, longitude=72.837608, zoom=12),
                  layers=[
        pdk.Layer(
        "HexagonLayer",
        data=other_apts[['latitude', 'longitude']],
        get_position=["longitude", "latitude"],
        auto_highlight=True,
        radius=100,
        extruded=True,
        pickable=True,
        elevation_scale=4,
        elevation_range=[0, 1000],
        ),
    ]))

if st.button('Predict'):
    
    prediction = predict_rent(model, feature_data)*0.70
    price = prediction*96.33

    check = {'Category':['Predicted Rent of '+str(Bedrooms)+' Bedroom '+str(Bathrooms)+ ' Bathroom apartment at '+ str(Locality),
                          'Predicted Price of ' + str(Bedrooms)+' Bedroom '+str(Bathrooms)+' Bathroom apartment at '+ str(Locality)],
              'Cost':[prediction, price]}
    st.table(check)
    st.subheader("Model trained, tested and deployed by Utsav Bhatt.")









