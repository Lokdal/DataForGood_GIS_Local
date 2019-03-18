# Data For Good : GIS tutorial using Python and folium 

This project is a tutorial for my colleagues in Data For Good, Ottawa local. They have access to the shapefile containing the polygons of every Dissemination Areas (DAs) in the Ottawa region, as well as the 2016 Census Data for each of these DAs. Executing the script "Median Income Map.py" will generate the map "Median Income Map.html", which can be viewed in any browser. From there, they can customize the script to use the columns they want and get familiar with python, pandas and folium.


## Why would I want to download your project?

To be able to create dynamic, colorful and insightful maps that are easy to share, like [this one](Median Income Map.html)


## Getting the data

The data was taken from Statistics Canada's website, then filtered to only contain information relative to Ottawa. The files "Ottawa Full Census by DA.csv" and "OttawaDA.geojson" are ready to be used without further processing.

For those whishing to clean the census and GIS data themselves, you will need a GIS software such as QGIS and [Beyond 20/20](https://www.statcan.gc.ca/eng/public/beyond20-20) if you wish to manipulate the data without requiring "Big Data" skills. You are looking to filter the DAs in the Ottawa region, which means their "CDUID" will be "3506" and thus their DAUID will start with "3506" as well.
The census data can be found [here](https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/prof/details/download-telecharger/comp/page_dl-tc.cfm?Lang=E).
The shapefile can be found [here](https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-2016-eng.cfm).


## Prerequesites

You need a working installation of Python 3, the packages *pandas* and *folium*, and their dependencies.
