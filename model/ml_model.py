from shapely.geometry import Point
import geopandas as gpd
from datetime import timedelta
from joblib import load
import numpy as np

# Model to predict the travel time


class Model:
    def __init__(self) -> None:
        self.model = load("linnearYellow.joblib")

    # Dummy method, should use more parameters for the final version

    def predict(self, fromlat, fromlon, tolat, tolon, requesttime):

        pnt1 = Point(fromlat, fromlon)
        pnt2 = Point(tolat, tolon)
        points_df = gpd.GeoDataFrame({"geometry": [pnt1, pnt2]}, crs="EPSG:4326")
        points_df = points_df.to_crs("EPSG:5234")
        points_df2 = (
            points_df.shift()
        )  # We shift the dataframe by 1 to align pnt1 with pnt2
        point = points_df.distance(points_df2).iloc[1]
        distance = point * 0.000621371192  # We convert to miles

        s = requesttime.split(":")
        pickup = timedelta(
            hours=int(s[0]), minutes=int(s[1]), seconds=int(s[2])
        ).total_seconds()
        pickup = int(pickup)

        prediction = self.model.predict(np.array([[distance, pickup]]))

        return int(prediction)
