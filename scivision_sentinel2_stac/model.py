import dask.distributed
import folium
import folium.plugins
import geopandas as gpd
import shapely.geometry
from IPython.display import HTML, display
from pystac_client import Client
from odc.stac import configure_rio, stac_load


class scivision_sentinel2_stac:
    def __init__(self):
        self.model_name = 'scivision_sentinel2_stac'
        # self.pretrained_model = self.load_images()

    def convert_bounds(bbox, invert_y=False):
        """
        Helper method for changing bounding box representation to leaflet notation

        ``(lon1, lat1, lon2, lat2) -> ((lat1, lon1), (lat2, lon2))``
        """
        x1, y1, x2, y2 = bbox
        if invert_y:
            y1, y2 = y2, y1
        return ((y1, x1), (y2, x2))
        
    def predict():
        
        # Since we will plot it on a map we need to use `EPSG:3857` projection
        crs = "epsg:3857"

        cfg = {
            "sentinel-s2-l2a-cogs": {
                "assets": {
                    "*": {"data_type": "uint16", "nodata": 0},
                    "SCL": {"data_type": "uint8", "nodata": 0},
                    "visual": {"data_type": "uint8", "nodata": 0},
                },
                "aliases": {"red": "B04", "green": "B03", "blue": "B02"},
            },
            "*": {"warnings": "ignore"},
        }

        km2deg = 1.0 / 111
        x, y = (113.887, -25.843)  # Center point of a query
        r = 100 * km2deg
        bbox = (x - r, y - r, x + r, y + r)

        catalog = Client.open("https://earth-search.aws.element84.com/v0")

        query = catalog.search(
            collections=["sentinel-s2-l2a-cogs"], datetime=["2021-09-16"], limit=100, bbox=bbox
        )

        items = list(query.get_items())

        # Convert STAC items into a GeoJSON FeatureCollection
        stac_json = query.get_all_items_as_dict()

        r = 6.5 * km2deg
        small_bbox = (x - r, y - r, x + r, y + r)

        yy = stac_load(
            items,
            bands=("red", "green", "blue"),
            crs=crs,
            resolution=10,
            chunks={},  # <-- use Dask
            groupby="solar_day",
            stac_cfg=cfg,
            bbox=small_bbox,
        )
        # display(yy.odc.geobox)

        return yy


if __name__ == "__main__":
    pass