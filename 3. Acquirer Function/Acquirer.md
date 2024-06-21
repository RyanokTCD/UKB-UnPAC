# Acquirer

## Inputs
The Acquirer function takes 3 inputs:
- `Path`
- `Series_Number`
- `Series_Description`

`Path` - The path variable remains the same as in the previous 2 functions. This is the location of the images in which the data augmentation needs to be preformed.

`Series_Number` - The series number is a charcteristic of the MRI metadata that describes a realative timeframe as to how the MRI was acquired. In the case of the UK-Biobank, these series numbers also correlate (not exactly) to
anatomical regions. A list of the UK-Biobank series number and their related anatomical regions can be found in the [Subdirectory for list], on this GitHub. The Acquirer function takes advantage of this.

`Series_Description` - Similar to the `Series_Number`, the series description is a characteristic of the conditions the MRI was acquired under. In the case of the UK-Biobank the DIXON weighted MR images were acquired under 8 different
conditions a list of which can be found in [subdirectory]. 

## Acquirer Script - This is a long one:
```python
    start_time = time.time()
    count = 1
    Path_dcm = Path + "\\**\\*.dcm"
```
This very first part of the function allows for the counting of the lenght of time the function takes as well as setting the path for where the DICOM images will be located. The count variable is to make visualisation of the 
function running and outputs easy to see.
```python
    for i in os.listdir(Path):
        print('reading file list...')
        unsortedList = []
        for root, dirs, files in os.walk(Path):
            for file in files: 
                if ".dcm" in file:
                    unsortedList.append(os.path.join(root, file))
    
        print('%s files found.' % len(unsortedList))
```
This part of the function navigates to where the images are stored and iteritavely reads through each of them. If any of the files in the directory are not DICOM files they are excluded. It also outputs a string to make the user
aware that the function is running. 
```python
    for dicom_loc in unsortedList:
        loc_dicom = os.path.dirname(dicom_loc)
        ds = pydicom.read_file(dicom_loc, force=True)

        patientID = os.path.basename(Path)
        studyDate = clean_text(ds.get("StudyDate", "NA"))
        studyDescription = clean_text(ds.get("StudyDescription", "NA"))
        seriesDescription = clean_text(ds.get("SeriesDescription", "NA"))
        seriesNumber = ds.get("SeriesNumber", "NA")
          
        modality = ds.get("Modality","NA")
        seriesInstanceUID = ds.get("SeriesInstanceUID","NA")
        instanceNumber = str(ds.get("InstanceNumber","0"))
        fileName = modality + "." + seriesInstanceUID + "." + instanceNumber + ".dcm"
```
This entire portion of the function is dedicated to just extracting the metadata from the MRI scan. It then combines these metadata variables to create a unique filling system for the DICOM images, allowing for a neater
and more easily read dataset. 

```python
        try:
            ds.decompress()
        except:
            print('an instance in file %s - %s - %s - %s" could not be decompressed. exiting.' % (patientID, studyDate, studyDescription, seriesDescription ))
```
This piece of the function decompresses the file. 
````python
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
````
This is the heart of the acquirer function. These loops compares the inputs you have given to the function with the data it currently has and creates folders to store only the specified scans in the desired series and 
with the desired series description. The reason it takes both into consideration when series number alone may result in the same outcome is that some of the labelling in the UK-Biobank is inconsistent. So even if an image is
series number 10 if it does not also fit the description it is likley that it is of the wrong anatomical area. The Acquirer function accounts for this and removes images that do not fit the series number requirement **and**
the series descriptor requirment.
````python
    for filename in glob.glob(Path_dcm):
        os.remove(filename)
    print("Done")
    print("--- %s seconds per patient ---" % ((time.time()-start_time)/len(os.listdir(Path))))
````
The final part of the removes the latent DICOM images, those that have not been specified by the researcher. It will then output the string "Done" as well as how long the function took to preform the task per patient in the
dataset. 
