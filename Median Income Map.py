# This file imports the median income data from the census and maps it to
# individual DAs specified by the GeoJSON file.

import json
import pandas
import folium

COORDS_ORIG = (45.3, -75.8)
GEOJSON_FILENAME = "OttawaDA.geojson"
CENSUS_FILENAME = "Ottawa Full Census by DA.csv"

# This contains all the polygons and their properties, but no census data.
with open(GEOJSON_FILENAME, "r") as tData:
    iDA = json.load(tData)

# You can edit usecols to extract the columns you want and make a different
# map or add more layers and information to it.
iStats = pandas.read_csv(
    CENSUS_FILENAME,
    skipinitialspace=True,
    usecols=["DA_UID", 'Median total income in 2015 among recipients ($)'],
    na_values="-999")

iStats.columns = ["DAUID", "Income"]
iStats["DAUID"] = iStats["DAUID"].astype(str)
iStats["Income"] = iStats["Income"].astype(float)

# This creates the map and the Choropleth layer then saves it
oMap = folium.Map(COORDS_ORIG, zoom_start=11, tiles="Stamen Toner")
mapIncome = folium.Choropleth(geo_data=iDA, data=iStats,
                              name="Median Income",
                              columns=("DAUID", "Income"),
                              key_on="feature.properties.DAUID",
                              fill_color="BuPu",
                              nan_fill_opacity=0.5, nan_fill_color="black")
oMap.add_child(mapIncome)
oMap.save("Median Income Map.html")
