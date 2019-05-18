
# coding: utf-8

# In[9]:

# Put all files in ncfiles repository

# Output Corresponding csv in csv repository

import xarray as xr
import os
from os import listdir
from os.path import isfile, join




main_directory = "ncfiles"
directory = "csv"
if not os.path.exists(main_directory):
    os.makedirs(main_directory)
onlyfiles = [("{}/{}".format(main_directory, f)) for f in listdir(main_directory) if isfile(join(main_directory, f))]
for each_file in onlyfiles:
    ds = xr.open_dataset(each_file)
    df = ds.to_dataframe()
    df = df.reset_index()
    saved_file = ("{}/{}{}").format(directory, each_file.split("/")[1][:-3], "csv")
    df.to_csv(saved_file, index=False)

