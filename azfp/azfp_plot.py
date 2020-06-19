from netCDF4 import Dataset
import numpy as np

nc_file = '19070107.nc'
fh = Dataset(nc_file, mode='r')

for value in fh.groups.values():
	print(value.variables['temperature'])
	# for children in value:
	# print(children)
	break

# import xarray as xr
# fname = '19070107.nc'
# ds = xr.open_dataset(fname, group='Beam')  # open file as an xarray DataSet
# data_120k = ds.backscatter_r.sel()  # explicit indexing for frequency
# print(data_120k)