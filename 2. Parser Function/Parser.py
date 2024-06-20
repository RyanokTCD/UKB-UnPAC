import pandas as pd
import zipfile,fnmatch,os
import glob
import shutil
import dicom2nifti # to convert DICOM files to the NIftI format
import pydicom
import time 

#Parser-----------------------------------------------------------------------------------------------------------------------------------

def Parser(Path, Exclusion_df, ID_variable_name):
    eid = Exclusion_df[ID_variable_name].values.tolist()
    eid = str(eid)
    os.chdir(Path)
    try:
        for dirname in os.listdir(Path):
            if dirname[:7] not in eid:
                shutil.rmtree(dirname)
    except NotADirectoryError:
        print("Done")
