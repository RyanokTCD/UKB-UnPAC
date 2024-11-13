import os
import fnmatch
import zipfile
import shutil

#UnZipper---------------------------------------------------------------------------------------------------------------------------------
def unzipper(path):
    pattern = '*.zip'
    for root, _, files in os.walk(path):
        for filename in fnmatch.filter(files, pattern):
            zip_path = os.path.join(root, filename)
            extract_dir = os.path.join(root, os.path.splitext(filename)[0])

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)

            os.remove(zip_path)

    print("Unzipping complete")
