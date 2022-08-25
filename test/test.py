from scivision_sentinel2_stac import scivision_sentinel2_stac, cfgCollections

# Settings
collections = ["sentinel-s2-l2a-cogs"]
res = 100
bands = ["B04", "B03", "B02"]
crs = "epsg:3857"
groupby = "solar_day"
dates = ["2021-09-16"]
# Query region
centre_point = [113.887, -25.843]
size = 6.5  # size of buffer

cfg = cfgCollections(collections[0]).cfg()

yy = scivision_sentinel2_stac.get_images(
        collections=collections,
        resolution=res,
        bands=bands,
        groupby=groupby,
        crs=crs,
        datetime=dates,
        centre_point=centre_point,
        size=size
)

yy_xr = yy.compute()