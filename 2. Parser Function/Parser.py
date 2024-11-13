import os
import shutil

#Parser-----------------------------------------------------------------------------------------------------------------------------------

def parser(path, exclusion_df, id_variable_name):
    # Convert exclusion list to a set for faster lookup
    excluded_ids = set(exclusion_df[id_variable_name].astype(str))

    for dirname in os.listdir(path):
        dir_path = os.path.join(path, dirname)
        # Check if it is a directory and not in the exclusion list
        if os.path.isdir(dir_path) and dirname[:7] not in excluded_ids:
            shutil.rmtree(dir_path)

    print("Parsing complete")
