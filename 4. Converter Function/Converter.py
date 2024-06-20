#dependencies------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import zipfile,fnmatch,os
import glob
import shutil
import dicom2nifti # to convert DICOM files to the NIftI format
import pydicom
import time 

#Converter--------------------------------------------------------------------------------------------------------------------------------
def Converter (Path):
    count = 0
    os.chdir(Path)
    for dirname in os.listdir(Path):
        dicom2nifti.convert_directory(dirname, dirname)
        count = count +1
        print("%s has been converted to NIfTI format (%s/%s)" % (dirname, count, len(os.listdir(Path))) )
    print("Done")
