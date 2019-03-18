# Data For Good : GIS tutorial using Python and folium 

This project is a tutorial for my colleagues in Data For Good, Ottawa local. They have access to the shapefile containing the polygons of every Dissemination Areas (DAs) in the Ottawa region, as well as the 2016 Census Data for each of these DAs. Executing the script "Median Income Map.py" will generate the map "Median Income Map.html", which can be viewed from any browser. From there, they can customize the script to use the columns they want and get familiar with python, pandas and folium.


## Getting the data

The data was taken from Statistics Canada's website, then filtered to only contain information relative to Ottawa.
Those whishing to clean the census data themselves can obtain it [here](https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/prof/details/download-telecharger/comp/page_dl-tc.cfm?Lang=E). They will need the software [Beyond 20/20](https://www.statcan.gc.ca/eng/public/beyond20-20) if they wish to manipulate the data without requiring "Big Data" skills. 
As for the shapefile, it can be found [here](https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-2016-eng.cfm). The regions of interest have the property "CDUID" set to "3506".


## Prerequesites

You need a working installation of Python 3, the packages *pandas* and *folium*, and their dependencies.
