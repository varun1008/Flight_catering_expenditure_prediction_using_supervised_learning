import uvicorn ##ASGI
from fastapi import FastAPI
from joblib import dump,load 
import numpy as np
import pandas as pd
from app import Exp_pred 
from cep import cep
from fastapi.middleware.cors import CORSMiddleware


# 2. Create the app object
app = FastAPI()

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

linearmodel = load('linearmodel.joblib')
linearscaler = load('linearscaler.joblib')

poly_linear_model = load('poly_linear_model.joblib')
poly_features = load('poly_features.joblib')
# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.post('/predict')
def predict_exp(data:Exp_pred):
    dt = data.dict()
    passg = dt['passg']
    male = dt['male']
    female = dt['female']
    kids =  dt['kids']
    nonveg_pas = dt['nonveg_pas']
    flight_dur = dt['flight_dur']
    day_night = dt['day_night']
    bus_class = dt['bus_class']
   
    return {
        'prediction': linearmodel.predict(linearscaler.transform([[passg,male,female,kids,nonveg_pas,flight_dur,day_night,bus_class]]))[0]
    }

@app.post('/api/predict')
def predict_ce(data:cep):
	data = data.dict()
	passg = data['passg']
	male = data['male']
	female =  data['female'] 
	kids =  data['kids']
	no_of_veg =  data['no_of_veg'] 
	no_of_nonveg = data['no_of_nonveg'] 
	seasonal_food_orders = data['seasonal_food_orders'] 
	coffee_orders = data['coffee_orders']
	biodegrabdle_cutlery = data['biodegrabdle_cutlery']
	dessert_orders = data['dessert_orders']
	stops = data['stops']
	weekend = data['weekend']
	flight_dur = data['flight_dur']
	day_night = data['day_night']
	bus_class = data['bus_class']      
	return {
        'prediction': poly_linear_model.predict(poly_features.transform([[passg,male,female,kids,no_of_veg,no_of_nonveg,seasonal_food_orders,coffee_orders,biodegrabdle_cutlery,dessert_orders,stops,weekend,flight_dur,day_night,bus_class]]))[0]
    }


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload