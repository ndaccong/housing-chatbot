from utils.utils import API_GTFS
import os

if __name__ == "__main__":
    # Download data if not exist
    ptv_data = ["stops.csv", "stop_times.csv", "routes.csv", "trips.csv"]
    data_check = True
    for data in ptv_data:
        if not os.path.exists(f"data/{data}"):
            data_check = False

    if not data_check:
        API_GTFS.download_and_extract_data()