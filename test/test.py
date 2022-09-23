from scivision_sentinel2_stac import scivision_sentinel2_stac, cfgs

# AOI
# Query region
km2deg = 1.0 / 111
size = 6.5  # size of buffer
x, y = (113.887, -25.843)  # Center point of a query
r = size * km2deg
bbox = (x - r, y - r, x + r, y + r) #N, S, E, W bounding box

# Settings
collection = "sentinel-s2-l2a-cogs"
res = 100
dates = ["2021-09-16"]
crs = "epsg:3857"

kwargs = {"bands":["red", "green", "blue"],
          "groupby":"solar_day",
          "cfg": cfgs,
          }

yy = scivision_sentinel2_stac.get_images(
        collection=collection,
        datetime=dates,
        resolution=res,
        bbox=bbox,
        crs = crs
        #**kwargs
        #bands=bands,
        #groupby=groupby,
        #crs=crs,
        #centre_point=centre_point,
        #size=size,
        #cfg=cfgs
)

yy_xr = yy.compute()

import easystac as es
from geojson import Point

geom = Point([-76.3,3.4])

E84_S2_L2A = (es.ImageCollection('sentinel-s2-l2a-cogs')
    .fromSTAC('https://earth-search.aws.element84.com/v0')
    .filterBounds(geom)
    .filterDate("2021-01-01","2022-01-01")
    .getInfo(epsg = 4326,resolution = 0.0001,assets = ["B02","B03","B04"]))

E84_S2_L2A


import easystac.planetary as pc
from geojson import Point

pc.Authenticate()
pc.Initialize()

geom = Point([-76.1,4.3])

S2 = (pc.ImageCollection("sentinel-2-l2a")
    .filterBounds(geom)
    .filterDate("2020-01-01","2021-01-01")
    .getInfo(resolution = 10))