# UnZipper

## Inputs:
The Unzipper function only takes one input `Path`. Path refers to the location of the files that you intend to run UnPac on, and is usually in the format of;
'C:\User\You\Downloaded_images'

You can enter this path directly into the function: 
```python
Unzipper(r"C:\User\You\Downloaded_images")
``` 
or you can store the path as a variable to save yourself having to retype it each time:
```python
Path = r"C:\User\You\Downloaded_images"
Unzipper(Path)
```
Both will result in the same output. 

The function will print the word "Done" once it has unzipped all files in the given path.

## The UnZipper script:
```python
    rootPath = Path
    pattern = '*.zip'
    src_zip = rootPath + "\*.zip"
```
The first section of the UnZipper function sets out what we're looking for and where we are looking for it. In this case we are looking in the Path directory and we are secifying that we are looking for .zip files.
The last line creates a variable that is a combination of the pattern and path to allow us to delete unused files later.

```python
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print(os.path.join(root, filename))
            zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(root, os.path.splitext(filename)[0]))
```
The first two for loops in the script iteritley go through the contents of the Path and identify those in the Path that match the specified file type (.zip). After its done this it unzips and extracts the contents to the same
location.

```python
    for filename in glob.glob(src_zip):
        os.remove(filename) 
    print("Done")
```
The final loop in this fucntion removes the remaining .zip files and prints the word "Done".
