from scivision_sentinel2_stac import scivision_sentinel2_stac

# Settings
collections = ["sentinel-s2-l2a-cogs"]
res = 10
bands = ["B04", "B03", "B02"]
crs = "epsg:3857"
groupby = "solar_day"
dates = ["2021-09-16"]
# Query region
centre_point = [113.887, -25.843]
size = 6.5  # size of buffer

# optional args
# cfg = {
#     "sentinel-s2-l2a-cogs": {
#         "assets": {
#             "*": {"data_type": "uint16", "nodata": 0},
#             "SCL": {"data_type": "uint8", "nodata": 0},
#             "visual": {"data_type": "uint8", "nodata": 0},
#         },
#         "aliases": {"red": "B04", "green": "B03", "blue": "B02"},
#     },
#     "*": {"warnings": "ignore"},
# }

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