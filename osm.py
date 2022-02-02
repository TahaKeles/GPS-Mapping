
import osmapi
import os
import overpass
import numpy as np
import pandas as pd
import folium








#
# api = osmapi.OsmApi()
# print(api.NodeGet(123))
# {u'changeset': 532907, u'uid': 14298,
# u'timestamp': u'2007-09-29T09:19:17Z',
# u'lon': 10.790009299999999, u'visible': True,
# u'version': 1, u'user': u'Mede',
# u'lat': 59.9503044, u'tag': {}, u'id': 123}


import shapefile
# shape = shapefile.Reader("turkey-latest-free/gis_osm_buildings_a_free_1.shp") #polygon

# shape = shapefile.Reader("turkey-latest-free/gis_osm_landuse_a_free_1.shp") #polygon

shape = shapefile.Reader("turkey-latest-free/gis_osm_roads_free_1.shp")
#
# shape = shapefile.Reader("turkey-latest-free/gis_osm_natural_free_1.shp")
#
# shape = shapefile.Reader("turkey-latest-free/gis_osm_places_a_free_1.shp")



count = 0
# print(shape.__len__())
# print(shape.__sizeof__())

coordinatesForPolygons = []
for eachRecord in shape.iterShapeRecords():
    print(eachRecord.shape.__geo_interface__)
    # print(eachRecord.shape.__geo_interface__["coordinates"][0][0]) # accessing north east coordinates
    coordinatesForPolygons.append(eachRecord.shape.__geo_interface__["coordinates"]) ## GeoJSON format




# print(coordinatesForPolygons)













# shape = shapefile.Reader("turkey-latest-free/gis_osm_landuse_a_free_1.shp")
#first feature of the shapefile
# feature = shape.shapeRecords()[0]
# featureSecond = shape.shapeRecords()[1]

# first = feature.shape.__geo_interface__
# second = featureSecond.shape.__geo_interface__
# print(first) # (GeoJSON format)
# print(second)
# {'type': 'LineString', 'coordinates': ((0.0, 0.0), (25.0, 10.0), (50.0, 50.0))}