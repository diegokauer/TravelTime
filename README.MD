# Time Travel Assignment

- Danilo Perovic
- Diego Kauer

We implemented the API using FastAPI, and trained the model in the file `projekt.ipynb`.

## Requirements

- geopandas
- fastapi
- uvicorn

You can use the eviroment.yml file to view the dependencies

## Running

To run the API go to the source folder of this project and run:
```
uvicorn API.main:app --reload
```

The API will start running on [http://127.0.0.1:8000](http://127.0.0.1:8000/docs). You can access the documentation [here](http://127.0.0.1:8000/docs) where you can run the API endpoint using a graphical interface.

# Endpoint:

## traveltime

### Summary
This endpoint gets the travel time (in seconds) in car from one location to another
and also takes into account the time of day of the request

### Args:
- **fromlat *(float)*:** Latitude of the origin location
- **fromlon *(float)*:** Longitude of the origin location
- **tolat *(float)*:** Latitude of the destination
- **tolon *(float)*:** Longitude of the destintation
- **requesttime *(str, optional)*:** Time of the request, format in HH:MM:SS. Defaults to datetime.now().strftime("%H:%M:%S").

#### Returns:
- **application/json** JSON with the only key being "traveltime" which is the predicted travel time.

#### Examples:

**URL:**
```
http://127.0.0.1:8000/traveltime?fromlat=40.72022253485829&fromlon=-73.9912536775281&tolat=40.766299191830804&tolon=-73.99340186612699&requesttime=11%3A54%3A45
```

**curl**
```
curl -X 'GET' \
  'http://127.0.0.1:8000/traveltime?fromlat=40.72022253485829&fromlon=-73.9912536775281&tolat=40.766299191830804&tolon=-73.99340186612699&requesttime=11%3A54%3A45' \
  -H 'accept: application/json'
```