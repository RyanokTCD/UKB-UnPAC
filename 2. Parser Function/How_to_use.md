# Parser Function

## Inputs
The Parser function takes 3 inputs:
- `path`
- `exclusion dataframe (df)`
- ``id variable name``

  **path** - Similar to the UnZipper function is where the images you have unzipped and need to be parsed are stored. If you used the UnZipper function this variable will be unchanged.

  **exclusion_df** - The exclusion dataframe contains the unique identifiers of the patients you wish to *include in your study*. Any images not specified in this dataframe will be deleted by the function!

  **id_variable_name** - The patient or image specific identifier used in the df and to name the images. Specify the name of the column containing the unique patient or image id as it is in the df e.g "Patient medical number".

  As with the unzipper, these inputs can be put directly into the function or stored as vairables and called in the function.

## The Parser Script:
```python
    excluded_ids = set(exclusion_df[id_variable_name].astype(str))
```
The first part of the Parser function, the unique patient identiier from the dataframe is converted to a set to allow it to be easily read by the function.

```python
    for dirname in os.listdir(path):
        dir_path = os.path.join(path, dirname)
        if os.path.isdir(dir_path) and dirname[:7] not in excluded_ids:
            shutil.rmtree(dir_path)
```
The next section of the script looks for directories in the given path and removes files which the first 7 indexes `dirname[:7]` dont match any in the dataframe. Changing the numerical value in this section of the script will allow the researcher to change the index that the function looks for. I.e making `dirname[:2]` will only keep images where the frist 3 symbols are the same. 
E.g if our dataframe patient ID is 12345 and the image is called '12345_MRI', having `dirname[:4]` means the function will only match the first 5 numbers of the image name to the dataframe, so only '12345' will be compared against the dataframe. If it was `dirname[:2]` only '123' would be compared against the dataframe.
```python
    print("Parsing complete")
```
Finally the function will print "Pasring Complete".
