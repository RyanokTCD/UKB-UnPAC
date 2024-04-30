# Welcome to UKB-UnPAC!
UKB-UnPAC is a Python package dedicated to the extraction of curated image data from the UK-Biobank. Developed by researchers in Trinity College Dublin’s Discipline of Radiation Therapy, as part of a project funded by the **World Cancer Research Fund** (WCRF). The funded project aimed to extract radiomics information from the Dixon weighted MRIs found in the UK-Biobank after being granted access. Considering the vastness of the data available an automated pipline was needed to streamline the acquisition of useful data from the UK-Biobank. This gave rise to UKB-UnPAC!

# What is UKB-UnPAC?
UKB-UnPAC offers an all-in-one system, designed to reduce the workload from extracting image data from the UK-Biobank, but can be adapted for any large scale radiological dataset. UKB-UnPAC has 4 main scripts which are its name sake, that allows researchers to:
* UnZip downloaded DICOM files.
* Parse those DICOM files based on researcher set variables.
* Acquire only anatomically relevant images from the UK-Biobank imaging datasets.
* Convert these images into a more research friendly format.
