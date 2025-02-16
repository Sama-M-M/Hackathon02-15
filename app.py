from flask import Flask, jsonify
import requests
from google.transit import gtfs_realtime_pb2

app = Flask(__name__)

# Calgary Transit Real-Time Vehicle Positions API
VEHICLE_POSITIONS_URL = "https://data.calgary.ca/download/am7c-qe3u/application%2Foctet-stream"

@app.route('/')
def home():
    return "Welcome to the Calgary Transit API! 🚍"

@app.route('/vehicles', methods=['GET'])
def get_vehicle_positions():
    """Fetch real-time Calgary Transit bus locations"""
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(VEHICLE_POSITIONS_URL)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch transit data"}), 500

    feed.ParseFromString(response.content)
    vehicles = []

    for entity in feed.entity:
        if entity.HasField('vehicle'):
            vehicle = entity.vehicle
            vehicles.append({
                "vehicle_id": vehicle.vehicle.id,
                "latitude": vehicle.position.latitude,
                "longitude": vehicle.position.longitude,
                "bearing": vehicle.position.bearing if vehicle.position.HasField("bearing") else None
            })

    return jsonify(vehicles)

if __name__ == '__main__':
    app.run(debug=True)
