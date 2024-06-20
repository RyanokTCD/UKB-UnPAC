import pandas as pd
import zipfile,fnmatch,os
import glob
import shutil
import dicom2nifti # to convert DICOM files to the NIftI format
import pydicom
import time 

#Attainer---------------------------------------------------------------------------------------------------------------------------------

def clean_text(string):
    # clean and standardize text descriptions, which makes searching files easier
    forbidden_symbols = ["*", ".", ",", "\"", "\\", "/", "|", "[", "]", ":", ";", " "]
    for symbol in forbidden_symbols:
        string = string.replace(symbol, "_") # replace everything with an underscore
    return string.lower()  

def Acquirer(Path, Series_Number, Series_Description):
    start_time = time.time()
    count = 1
    Path_dcm = Path + "\\**\\*.dcm"
    for i in os.listdir(Path):
        print('reading file list...')
        unsortedList = []
        for root, dirs, files in os.walk(Path):
            for file in files: 
                if ".dcm" in file:# exclude non-dicoms, good for messy folders
                    unsortedList.append(os.path.join(root, file))
    
        print('%s files found.' % len(unsortedList))
    
    for dicom_loc in unsortedList:
        # read the file
        loc_dicom = os.path.dirname(dicom_loc)
        ds = pydicom.read_file(dicom_loc, force=True)
        # get patient, study, and series information
        patientID = os.path.basename(Path)
        studyDate = clean_text(ds.get("StudyDate", "NA"))
        studyDescription = clean_text(ds.get("StudyDescription", "NA"))
        seriesDescription = clean_text(ds.get("SeriesDescription", "NA"))
        seriesNumber = ds.get("SeriesNumber", "NA")
          
            # generate new, standardized file name
        modality = ds.get("Modality","NA")
        seriesInstanceUID = ds.get("SeriesInstanceUID","NA")
        instanceNumber = str(ds.get("InstanceNumber","0"))
        fileName = modality + "." + seriesInstanceUID + "." + instanceNumber + ".dcm"
               
            # uncompress files (using the gdcm package)
        try:
            ds.decompress()
        except:
            print('an instance in file %s - %s - %s - %s" could not be decompressed. exiting.' % (patientID, studyDate, studyDescription, seriesDescription ))
                
        if seriesNumber in Series_Number:
            if seriesDescription in Series_Description:
                if not os.path.exists(os.path.join(loc_dicom)):
                    os.makedirs(os.path.join(loc_dicom))
                   
                if not os.path.exists(os.path.join(loc_dicom, studyDate)):
                    os.makedirs(os.path.join(loc_dicom, studyDate))
                       
                if not os.path.exists(os.path.join(loc_dicom, studyDate, studyDescription)):
                    os.makedirs(os.path.join(loc_dicom, studyDate, studyDescription))
                       
                if not os.path.exists(os.path.join(loc_dicom, studyDate, studyDescription, seriesDescription)):
                    os.makedirs(os.path.join(loc_dicom, studyDate, studyDescription, seriesDescription))
                    print('Saving out file: %s - %s - %s - %s.' % (patientID, studyDate, studyDescription, seriesDescription ))
                    print('%s files out of %s total files extracted.' % (count, len(unsortedList)))
                       
                ds.save_as(os.path.join(loc_dicom, studyDate, studyDescription, seriesDescription, fileName))
                count = count +1
    
    for filename in glob.glob(Path_dcm):
        os.remove(filename)
    print("Done")
    print("--- %s seconds per patient ---" % ((time.time()-start_time)/len(os.listdir(Path))))   
