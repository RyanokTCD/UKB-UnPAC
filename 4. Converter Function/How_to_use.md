# Converter 
## Inputs
The converter function takes a singular input, `Path`.

`Path` - The path variable is the same one that has been in use during the rest of the UnPAC.

## Converter Script:
```python
    count = 0
    os.chdir(Path)
```
The first section of this function creates a count variable, to allow us to track the progress of the converter, and also sets the working directory to wherever the images are, so we dont run into unecessary errors.

```python
    for dirname in os.listdir(Path):
        dicom2nifti.convert_directory(dirname, dirname)
        count = count +1
        print("%s has been converted to NIfTI format (%s/%s)" % (dirname, count, len(os.listdir(Path))) )
    print("Done")
```
The second part of this function contains a loop that reads through each of the directories in the `Path` variable and converts any dicom files it finds within them into NIFTI files. The directory name is maintained for these new NIFTI files.
The count variable is increased by 1 and a print statement feeds out the current progress of the function.
When fully completed the function will output "Done"
And congratulations! You have UnPAC'ed!
