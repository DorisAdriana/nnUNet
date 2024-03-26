import os
# import nibabel as nib

# Define the path to the folder containing the .nii.gz files
folder_path = "/home/rnga/dawezenberg/my-scratch/nnUNet_raw_data_base/nnUNet_raw_data/Task531_3D_cine_root_branches_gt/imagesTs/"

import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
from nilearn import plotting, image




####### RESHAPE TO 3 DIM
# Function to load a file, keep only the first three dimensions, and overwrite the original file
def process_and_save_file(file_path):
    # Load the NIfTI file
    img = nib.load(file_path)
    data = img.get_fdata()
    
    # Check if the data has more than three dimensions
    if data.ndim > 3:
        # Keep only the first three dimensions
        data = data[..., 0]
        # Create a new NIfTI image from the modified data
        new_img = nib.Nifti1Image(data, affine=img.affine)
        # Save the new image to the same file, replacing the original
        nib.save(new_img, file_path)
        print(f"Processed and saved: {file_path}")
    else:
        print(f"File already has 3 or fewer dimensions: {file_path}")

# Iterate over all .nii.gz files in the folder and process them
for file_name in os.listdir(folder_path):
    if file_name.endswith(".nii.gz"):
        file_path = os.path.join(folder_path, file_name)
        process_and_save_file(file_path)
