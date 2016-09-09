from urllib.request import urlopen


# Retrieve earthquake data for the past hour relating to earthquakes of magnitude 2.5+.

def main():
    url = urlopen("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson")
    print("Result code: " + str(url.getcode()))
    if url.getcode() == 200:
        data = url.read()
        print(data)
    else:
        print("Error, cannot retrieve results " + str(url.getcode()))


if __name__ == '__main__':
    main()
