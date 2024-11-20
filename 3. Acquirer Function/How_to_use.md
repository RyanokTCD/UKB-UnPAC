# Acquirer

## Inputs
The Acquirer function takes 3 inputs:
- `Path`
- `Series_Number`
- `Series_Description`

`path` - The path variable remains the same as in the previous 2 functions. This is the location of the images in which the data augmentation needs to be preformed.

`series_numbers` - The series number is a charcteristic of the MRI metadata that describes a realative timeframe as to how the MRI was acquired. In the case of the UK-Biobank, these series numbers also correlate (not exactly) to
anatomical regions. A list of the UK-Biobank series number and their related anatomical regions can be found in the [Subdirectory for list], on this GitHub. The Acquirer function takes advantage of this.

`series_description` - Similar to the `series_number`, the series description is a characteristic of the conditions the MRI was acquired under. In the case of the UK-Biobank the DIXON weighted MR images were acquired under 8 different
conditions a list of which can be found in [subdirectory]. 

## Acquirer Script - This is a long one:
```python
    start_time = time.time()
    path = Path(path)

    dicom_files = list(path.rglob("*.dcm"))
    print(f'{len(dicom_files)} DICOM files found.')

    count = 0
    files_to_delete = []
```
This very first part of the function allows for the counting of the lenght of time the function takes as well as setting the path for where the DICOM images will be located. The count variable is to make visualisation of the 
function running and outputs easy to see.
```python
    for dicom_loc in dicom_files:
        try:
            ds = pydicom.dcmread(dicom_loc, force=True)

            series_number = ds.get("SeriesNumber", "NA")
            series_description = clean_text(ds.get("SeriesDescription", "NA"))
```
This part of the function navigates to where the images are stored and iteritavely reads through each of them. If any of the files in the directory are not DICOM files they are excluded.
```python
            if series_number in series_numbers and series_description in series_descriptions:
                
                modality = ds.get("Modality", "NA")
                series_instance_uid = ds.get("SeriesInstanceUID", "NA")
                instance_number = str(ds.get("InstanceNumber", "0"))
                file_name = f"{modality}.{series_instance_uid}.{instance_number}.dcm"
                
                save_path = dicom_loc.with_name(file_name)

                try:
                    ds.decompress()
                except Exception as e:
                    print(f"File {dicom_loc} could not be decompressed: {e}")
                    continue

                ds.save_as(save_path)
                count += 1
                print(f"Saved file: {save_path.name} ({count} of {len(dicom_files)})")

                if save_path != dicom_loc:
                    files_to_delete.append(dicom_loc)

            else:
                files_to_delete.append(dicom_loc)

        except Exception as e:
            print(f"Error processing file {dicom_loc}: {e}")

```
This entire portion of the function is dedicated to just extracting the metadata from the MRI scan, and then saving the portion of the scan specified by the researcher, identified by that metadata.

```python
    for file_path in files_to_delete:
        try:
            file_path.unlink()  # Safely remove unmatched .dcm files
        except FileNotFoundError:
            pass 
```
The final part of the removes the latent DICOM images, those that have not been specified by the researcher. 
````python
    print("Done")
    avg_time = (time.time() - start_time) / (len(dicom_files) or 1)
    print(f"--- {avg_time:.2f} seconds per file ---")
````
The final section of the acquirer outputs the word ("Done") and gives the researcher the time it took per patient to preform this function in seconds.


