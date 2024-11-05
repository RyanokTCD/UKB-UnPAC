import pandas as pd
import zipfile,fnmatch,os
import glob
import shutil
import dicom2nifti # to convert DICOM files to the NIftI format
import pydicom
import time 

#UnZipper---------------------------------------------------------------------------------------------------------------------------------
def UnZipper (Path):
    rootPath = Path
    pattern = '*.zip'
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print(os.path.join(root, filename))
            zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(root, os.path.splitext(filename)[0]))
        for file in files:
            if file.endswith(".zip"):
                os.remove(os.path.join(root, file))
    print("Done")
