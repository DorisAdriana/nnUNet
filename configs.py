### 1. configure
# activate virtual environment
# set working directory
# export nnUNet_raw_data_base="/home/rnga/dawezenberg/my-scratch/nnUNet_raw_data_base"
# export nnUNet_preprocessed="/home/rnga/dawezenberg/my-scratch/nnUNet_preprocessed"
# export RESULTS_FOLDER="/home/rnga/dawezenberg/my-scratch/nnUNetresults"

### 2. Get data in the right filder and adjust dataset.json file accordingly
# check if data is in 3-dim shape
# adjust configs in datasetjson file

# nnUNet_predict -i $nnUNet_raw_data_base/nnUNet_raw_data/Task005_Prostate/imagesTs/ -o OUTPUT_DIRECTORY -t 5 -m 3d_fullres
# nnUNet_predict -i $nnUNet_raw_data_base/nnUNet_raw_data/Task005_Prostate/imagesTs/ -o /home/rnga/dawezenberg/my-scratch/outputs/ -t 5 -m 3d_fullres --disable_tta

# Task531_3D_cine_root_branches
# nnUNet_predict -i $nnUNet_raw_data_base/nnUNet_raw_data/Task531_3D_cine_root_branches/imagesTs/ -o /home/rnga/dawezenberg/my-scratch/outputs/ -t 531 -m 3d_fullres --disable_tta -tr nnUNetTrainerV2_AMC_100epochs
# Note that you must ensure that the trainer file is located in the repo: /home/rnga/dawezenberg/my-rdisk/r-divi/RNG/Projects/stages/Pim/Doris/nnUNet/nnunet/training/network_training/
