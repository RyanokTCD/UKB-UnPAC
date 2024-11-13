import dicom2nifti

#Converter--------------------------------------------------------------------------------------------------------------------------------
def converter(path):
    path = Path(path)
    directories = [d for d in path.iterdir() if d.is_dir()]
    
    for count, dirname in enumerate(directories, start=1):
        try:
            dicom2nifti.convert_directory(dirname, dirname)
            print(f"{dirname.name} has been converted to NIfTI format ({count}/{len(directories)})")
        except Exception as e:
            print(f"Failed to convert {dirname.name}: {e}")

    print("Conversion complete.")
