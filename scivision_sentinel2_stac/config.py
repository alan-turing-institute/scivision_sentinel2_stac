"""
Source: https://github.com/opendatacube/odc-stac/blob/9fc79013f398d038cca2cfe4b128b7a76b6a9233/odc/stac/_load.py
Sometimes data source might be missing some optional STAC extensions. With ``stac_cfg=`` parameter
one can supply that information at load time. Configuration is per collection per asset. You can
provide information like pixel data type, ``nodata`` value used, ``unit`` attribute and band aliases
you would like to use.

Sample ``stac_cfg={..}`` parameter:

sentinel-2-l2a:  # < name of the collection, i.e. ``.collection_id``
 assets:
   "*":  # Band named "*" contains band info for "most" bands
     data_type: uint16
     nodata: 0
     unit: "1"
   SCL:  # Those bands that are different than "most"
     data_type: uint8
     nodata: 0
     unit: "1"
 aliases:  #< unique alias -> canonical map
   rededge: B05
   rededge1: B05
   rededge2: B06
   rededge3: B07

some-other-collection:
 assets:
 #...

"*": # Applies to all collections if not defined on a collection
 warnings: ignore  # ignore|all (default all)

"""

# set collections configs and optional settings
cfgs = {
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