import os
import nibabel as nib

# Define the path to the folder containing the .nii.gz files
folder_path = "/home/rnga/dawezenberg/my-scratch/outputs"

import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np

def plot_orthogonal_slices(nifti_file_path, slice_indices=None):
    """
    Plots axial, sagittal, and coronal slices of a NIfTI image.
    
    Parameters:
    - nifti_file_path: Path to the NIfTI file.
    - slice_indices: Tuple of indices (axial, sagittal, coronal) to plot.
                     If None, the middle slice in each direction is used.
    """
    # Load the NIfTI file
    img = nib.load(nifti_file_path)
    data = img.get_fdata()
    
    if slice_indices is None:
        # Default to the middle slice in each dimension if not specified
        slice_indices = (data.shape[2] // 2, data.shape[0] // 2, data.shape[1] // 2)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Axial
    axes[0].imshow(np.rot90(data[:, :, slice_indices[0]]), cmap="gray")
    axes[0].set_title("Axial")
    
    # Sagittal
    axes[1].imshow(np.rot90(data[slice_indices[1], :, :]), cmap="gray")
    axes[1].set_title("Sagittal")
    
    # Coronal
    axes[2].imshow(np.rot90(data[:, slice_indices[2], :]), cmap="gray")
    axes[2].set_title("Coronal")
    
    for ax in axes:
        ax.axis("off")
    
    plt.show()

# Path to your NIfTI file
nifti_file_path = 'path/to/your/file.nii.gz'

# Call the function
for file_name in os.listdir(folder_path):
    if file_name.endswith(".nii.gz"):
        nifti_file_path = os.path.join(folder_path, file_name)
        plot_orthogonal_slices(nifti_file_path)

###### GET SHAPE
# Function to load a file, keep only the first three dimensions, and overwrite the original file
# def inspectfile(file_path):
#     # Load the NIfTI file
#     img = nib.load(file_path)
#     data = img.get_fdata()
#     print(data.ndim)

# # Iterate over all .nii.gz files in the folder and process them
# for file_name in os.listdir(folder_path):
#     if file_name.endswith(".nii.gz"):
#         file_path = os.path.join(folder_path, file_name)
#         inspectfile(file_path)

####### RESHAPE TO 3 DIM
# # Function to load a file, keep only the first three dimensions, and overwrite the original file
# def process_and_save_file(file_path):
#     # Load the NIfTI file
#     img = nib.load(file_path)
#     data = img.get_fdata()
    
#     # Check if the data has more than three dimensions
#     if data.ndim > 3:
#         # Keep only the first three dimensions
#         data = data[..., 0]
#         # Create a new NIfTI image from the modified data
#         new_img = nib.Nifti1Image(data, affine=img.affine)
#         # Save the new image to the same file, replacing the original
#         nib.save(new_img, file_path)
#         print(f"Processed and saved: {file_path}")
#     else:
#         print(f"File already has 3 or fewer dimensions: {file_path}")

# # Iterate over all .nii.gz files in the folder and process them
# for file_name in os.listdir(folder_path):
#     if file_name.endswith(".nii.gz"):
#         file_path = os.path.join(folder_path, file_name)
#         process_and_save_file(file_path)
