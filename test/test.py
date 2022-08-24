from scivision_sentinel2_stac import scivision_sentinel2_stac

res = 10

yy = scivision_sentinel2_stac.load_data(resolution=res)

yy_xr = yy.compute()