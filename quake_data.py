from urllib.request import urlopen
import json


# Retrieve earthquake data for the past hour relating to earthquakes of magnitude 2.5+.

def print_results(data):
    # Load(deserialize a str instance) quake event data into python object
    data_json = json.loads(data.decode())
    # access the contents of the JSON
    if "title" in data_json["metadata"]:
        print(data_json["metadata"]["title"])

def main():
    url = urlopen("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson")
    print("Result code: " + str(url.getcode()))
    if url.getcode() == 200:
        data = url.read()
        print_results(data)
    else:
        print("Error, cannot retrieve results " + str(url.getcode()))





if __name__ == '__main__':
    main()
