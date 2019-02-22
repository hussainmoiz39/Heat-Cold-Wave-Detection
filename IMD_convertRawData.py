# Filename: IMD_convertRawData.py
# Author: Satyam & Moiz
# Date Created: Feb 16, 2019
# Last Edited: Feb 21, 2019
# Data: from NCC ZIP file   
# Purpose: Reads in GRaDS data files, concatenates them, and then exports netCDF versions  
# Notes: To be run after "convert_to_GrADS.R"
# need to install cdo and netcdf4 through pip
# install cdo from apt-get

import os, sys
from cdo import *
from netCDF4 import Dataset
import numpy as np
#import pandas as pd 
import cdo as cdo
# add local dir to search path
sys.path.append(os.path.dirname(sys.path[0]))
sys.path.append('/usr/local/lib/python3.6/dist-packages/cdo.py')
if 'CDF_MOD' in os.environ:
    CDF_MOD = os.environ['CDF_MOD']
else:
    CDF_MOD = 'netcdf4'

root_path = "/home/satyam/course/IMD_DATA_Temperature" 

cdo = Cdo() 


root_path = "/home/satyam/course/IMD_DATA_Temperature" 
ctl_root = os.path.join(root_path, "CTL_Files")


def tempOutput(var, ctl, root):
	"""
	Read in binary data and output as a netCDF file.
	var: weather variable   
	ctl: root path for all .ctl's
	root: project root path
	"""

	# -- rename variables for consistency with other projects
	temp_rename = {"MaxT": "tmax", "MinT": "tmin", "MeanT": "tmean"}

	# initialize using first year's data 
	t = cdo.import_binary(input = os.path.join(ctl, var, var + "_1951.ctl"))

	# -- loop through each remaining year 
	for y in range(1952,2014):
		print("Now processing " + str(y))
		fn = var + "_" + str(y) + ".ctl"	
		print("Processing " + str(os.path.join(ctl_root, var, fn)))

		# -- concatenate into a single file
		data = cdo.import_binary(input = os.path.join(ctl_root, var, fn))
		t = cdo.cat(input = " ".join([t,data]))

	# -- save variable-specific file	
	t = cdo.copy(input = t, options = "-f nc", output = os.path.join(root, temp_rename[var] + "Proc.nc"))


tempOutput("MaxT", ctl_root, root_path)
tempOutput("MinT", ctl_root, root_path)
tempOutput("MeanT", ctl_root, root_path)