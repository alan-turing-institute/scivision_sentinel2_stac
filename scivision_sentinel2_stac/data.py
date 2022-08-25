from pystac_client import Client
from odc.stac import stac_load
import xarray


class scivision_sentinel2_stac:
    def __init__(self):
        self.data_name = 'scivision_sentinel2_stac'

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

        return yy


if __name__ == "__main__":
    pass