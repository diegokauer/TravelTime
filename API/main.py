from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

from model.ml_model import Model

model = Model()

# TravelTime class


class TravelTime(BaseModel):
    """TravelTime class, the only atribute is the travel time in seconds
    predicted by the model.
    """

    traveltime: int


app = FastAPI()


@app.get(
    "/traveltime", response_model=TravelTime, tags=["Travel Time"],
)
async def predict_travel_time(
    fromlat: float,
    fromlon: float,
    tolat: float,
    tolon: float,
    requesttime: str = datetime.now().strftime("%H:%M:%S"),
) -> TravelTime:
    """
    ### Summary:
    This endpoint gets the travel time (in seconds) in car from one location to another
    and also takes into account the time of day of the request

    ### Args:
    - **fromlat *(float)*:** Latitude of the origin location
    - **fromlon *(float)*:** Longitude of the origin location
    - **tolat *(float)*:** Latitude of the destination
    - **tolon *(float)*:** Longitude of the destintation
    - **requesttime *(str, optional)*:** Time of the request, format in HH:MM:SS. Defaults to datetime.now().strftime("%H:%M:%S").
    
    ### Returns:
    - **application/json:** JSON with the only key being "traveltime" which is the predicted travel time. 
    """

    time = model.predict(fromlat, fromlon, tolat, tolon, requesttime)
    return TravelTime(traveltime=time)
