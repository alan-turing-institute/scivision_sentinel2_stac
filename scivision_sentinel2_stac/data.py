from pystac_client import Client
from odc.stac import stac_load
import xarray


class scivision_sentinel2_stac:
    def __init__(self):
        self.data_name = 'scivision_sentinel2_stac'

    def convert_bounds(bbox, invert_y=False):
        """
        Helper method for changing bounding box representation to leaflet notation

        ``(lon1, lat1, lon2, lat2) -> ((lat1, lon1), (lat2, lon2))``
        """
        x1, y1, x2, y2 = bbox
        if invert_y:
            y1, y2 = y2, y1
        return ((y1, x1), (y2, x2))
        
    # def list_collections():
    #     return ["sentinel-s2-l2a-cogs", "sentinel-s2-l2a-cogs", "sentinel-s2-l2a-cogs"]
        
    def get_images(
        collections: list = ["sentinel-s2-l2a-cogs"],
        resolution: int = 10,
        bands: list = None,
        groupby: str = "solar_day",
        crs: str = "epsg:3857",  # Plotting on a map we requires `EPSG:3857` projection
        datetime: list = ["2021-09-16"],
        limit: int = 100,
        centre_point: tuple = (),
        size: int = None,
        cfg: dict = {}
    ) -> xarray.Dataset:
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

        km2deg = 1.0 / 111
        x, y = centre_point  # Center point of a query
        r = size * km2deg

        bbox = (x - r, y - r, x + r, y + r)

        catalog = Client.open("https://earth-search.aws.element84.com/v0")

        query = catalog.search(
            collections=collections, datetime=datetime, limit=limit, bbox=bbox
        )

        items = list(query.get_items())

        yy = stac_load(
            items,
            bands=bands,
            crs=crs,
            resolution=resolution,
            chunks={},  # <-- use Dask
            groupby=groupby,
            # stac_cfg=cfg,
            bbox=bbox,
        )

        # display(yy.odc.geobox)

        return yy


if __name__ == "__main__":
    pass