# Welcome to UKB-UnPAC!
UKB-UnPAC is a Python package dedicated to the extraction of curated image data from the UK-Biobank. Developed by researchers in Trinity College Dublin’s Discipline of Radiation Therapy, as part of a project funded by the **World Cancer Research Fund** (WCRF). The funded project aimed to extract radiomics information from the Dixon weighted MRIs found in the UK-Biobank after being granted access. Considering the vastness of the data available an automated pipline was needed to streamline the acquisition of useful data from the UK-Biobank. This gave rise to UKB-UnPAC!

# What is UKB-UnPAC?
UKB-UnPAC offers an all-in-one system, designed to reduce the workload from extracting image data from the UK-Biobank, but can be adapted for any large scale radiological dataset. UKB-UnPAC has 4 main scripts which are its name sake, that allows researchers to:
* UnZip downloaded DICOM files.
* Parse those DICOM files based on researcher set variables.
* Acquire only anatomically relevant images from the UK-Biobank imaging datasets.
* Convert these images into a more research friendly format.

![Schematic diagram of the UKN-UnPAC process, highlighting inputs, outputs, and the 4 key processes](https://github.com/RyanokTCD/UKB-UnPAC/blob/main/Documents/Assets/Pipeline%20diagram.png)

More detail on each of the processes are detailed below. Usage instructions can be found in (LINK)

## UnZipper
When initally downloaded, the MRI images from the UK-Biobank (UKB) come in the form of compressed, zip files (.zip). This file type is not easily read into many applications and is not accesable for research purposes. To overcome this, the UnZipper script was created. This function iteratively unzips each of the files into a readable, unzipped format, ready for use in research activities. This function retains the name of the zip file and matches the unzipped and zipped directories based on name. After all directories have been unzipped, the function then deletes the original zipped directories, to reduce data storage. 

## Parser
The parser function allows researchers to filter which data to parse based on a user set variable. Resaerchers will need to have created a CSV file with the list of patient IDs to be included in the study, and assign the patient ID variable name when calling the function. **This function works by comparing the list of unzipped image files names to the CSV file list, therefore directory names and patient ID in the CSV must match!** Any directory not found on your CSV list will be deleted. 

## Acquirer
The acquirer function, as is illustrated above, reads the metadata of the MRI and splits the full body MRI into its component parts based on the name of the series and the series number. This can be changed to allow for scans of different anatomical areas to be retained. The acquirer function reads the metadata, organizes the files in a neater pathway, based on the work 
