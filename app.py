from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Exp_pred(BaseModel):
    passg: float 
    male: float 
    female: float 
    kids: float
    nonveg_pas : float
    flight_dur : float
    day_night : float
    bus_class : float  