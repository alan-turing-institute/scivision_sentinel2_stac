
# set collections
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

class cfgCollections:
    def __init__(self, collection='sentinel-s2-l2a-cogs'):
        self.collection = collection

    def cfg(self):
        self.cfg = cfgs[self.collection]
        return self.cfg