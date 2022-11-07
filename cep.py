from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class cep(BaseModel):
    passg: float 
    male: float 
    female: float 
    kids: float
    no_of_veg : float
    no_of_nonveg : float
    seasonal_food_orders : float
    coffee_orders: float
    biodegrabdle_cutlery : float
    dessert_orders : float
    stops : float
    weekend : float
    flight_dur : float
    day_night : float
    bus_class : float  