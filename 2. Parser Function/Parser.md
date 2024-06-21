# Parser Function

## Inputs
The Parser function takes 3 inputs:
- `Path`
- `Exclusion dataframe (df)`
- ``ID variable name``

  **Path** - Similar to the UnZipper function is where the images you have unzipped and need to be parsed are stored. If you used the UnZipper function this variable will be unchanged.

  **Exclusion_df** - The exclusion dataframe contains the unique identifiers of the patients you wish to *include in your study*. Any images not specified in this dataframe will be deleted by the function!

  **ID_variable_name** - The patient or image specific identifier used in the df and to name the images. Specify the name of the column containing the unique patient or image id as it is in the df e.g "Patient medical number".

  As with the UnZipper, these inputs can be put directly into the function or stored as vairables and called in the function.

## Usage
