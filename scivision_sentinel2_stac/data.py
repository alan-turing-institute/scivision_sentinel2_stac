from pystac_client import Client
from odc.stac import stac_load
import xarray
from datetime import datetime


class scivision_sentinel2_stac:
    def __init__(self):
        self.data_name = 'scivision_sentinel2_stac'

    # def list_collections():
    #     return ["sentinel-s2-l2a-cogs", "sentinel-s2-l2a-cogs", "sentinel-s2-l2a-cogs"]
        
    def get_images(
        collection: str = "sentinel-s2-l2a-cogs",
        resolution: int = 100,
        crs: str = None,
        dates: list = None,
        bbox: list = None,
        limit: int = 100,
        #**kwargs
    ) -> xarray.Dataset:
        """Loads STAC collection based on input criteria.

            Parameters
            ----------
            TODO list mandatory, optionals in https://github.com/opendatacube/odc-stac/blob/9fc79013f398d038cca2cfe4b128b7a76b6a9233/odc/stac/_load.py
            **kwargs
            Additional arguments passed to :code:`odc.stac.stac_load()`. Some of them are
            :code:`epsg`, :code:`resolution`, and :code:`bbox`.

            Returns
            -------
            ds : xr.Dataset or zarr group
                Dataset with STAC collection data (composite according to the groupby arg)
            """

        if collection is None and resolution is None:
            raise ValueError("Either collection or resolution must be specified.")

        catalog = Client.open("https://earth-search.aws.element84.com/v0")

        query = catalog.search(
            collections=collection, datetime=dates, limit=limit, bbox=bbox
        )

        items = list(query.get_items())

        yy = stac_load(
            items,
            resolution=resolution,
            bbox=bbox,
            crs=crs,
            #**kwargs
        )

        return yy


if __name__ == "__main__":
    pass