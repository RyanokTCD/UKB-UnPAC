# unipper

## Inputs:
The Unzipper function only takes one input `Path`. Path refers to the location of the files that you intend to run UnPac on, and is usually in the format of;
'C:\User\You\Downloaded_images'

You can enter this path directly into the function: 
```python
unzipper(r"C:\User\You\Downloaded_images")
``` 
or you can store the path as a variable to save yourself having to retype it each time:
```python
Path = r"C:\User\You\Downloaded_images"
unzipper(Path)
```
Both will result in the same output. 

The function will print the word "Done" once it has unzipped all files in the given path.

## The UnZipper script:
```python
    pattern = '*.zip'
```
The first section of the UnZipper function sets out what we're looking for and where we are looking for it. In this case we are looking in the Path directory and we are specifying that we are looking for .zip files.

```python
    for root, _, files in os.walk(path):
        for filename in fnmatch.filter(files, pattern):
            zip_path = os.path.join(root, filename)
            extract_dir = os.path.join(root, os.path.splitext(filename)[0])

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
```
The first two for loops in the script iteratively go through the contents of the Path and identify those in the Path that match the specified file type (.zip). After its done this it unzips and extracts the contents to the same location.

```python
            os.remove(zip_path)

    print("Unzipping complete")
```
The final part in this function removes the remaining .zip files and prints "Unzipping complete". Be aware THIS WILL REMOVE ALL ZIP FILES IN YOUR DIRECTORY. If you want to retain both the zip and unzipped versions remove this section from the function.
