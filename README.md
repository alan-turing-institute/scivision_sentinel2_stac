# scivision_sentinel2_stac
Scivision plugin for loading accessing Sentinel-2 Cloud-Optimized GeoTIFFs (following tutorial: https://odc-stac.readthedocs.io/en/latest/notebooks/stac-load-e84-aws.html)

The plugin can be installed via scivision:

`pip install scivision`

To run a demo showing how the plugin is used, open `demo.py` as a notebook like so:

1. Create a fresh environment to run the notebook e.g. `conda create --name test_env python=3.10`
2. Activate the env you created: `conda activate test_env`
3. Install dask and distributed: `conda install dask distributed`
4. Install the scivision package: `pip install scivision`
5. Install jupyter and jupytext: `pip install jupyter jupytext`
6. Run `jupyter notebook` and click on `demo.py`