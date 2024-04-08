import os
import numpy as np
import nibabel as nib
from medpy.metric.binary import hd, dc  # hd is Hausdorff distance, dc is Dice coefficient

def compute_metrics(vol1, vol2):
    """
    Compute both the Dice score and the Hausdorff Distance between two binary volumes.
    vol1 and vol2 are numpy arrays.
    """
    dice_score = dc(vol1, vol2)
    hausdorff_distance = hd(vol1, vol2)
    
    return dice_score, hausdorff_distance

def main(pred_folder, gt_folder):
    pred_folder = os.path.expanduser(pred_folder)
    gt_folder = os.path.expanduser(gt_folder)

    metrics_by_scan = {}
    metrics_by_phase = {}
    
    for filename in os.listdir(pred_folder):
        if filename.endswith('nii.gz'):
            pred_path = os.path.join(pred_folder, filename)
            gt_path = os.path.join(gt_folder, filename)
            
            pred_vol = nib.load(pred_path).get_fdata()
            gt_vol = nib.load(gt_path).get_fdata()
            
            dice_score, hausdorff_distance = compute_metrics(pred_vol > 0, gt_vol > 0)
            
            base_name = filename.rsplit('b', 1)[0]
            phase = filename.split('b')[-1].split('.')[0]  # Extract phase
            
            if base_name not in metrics_by_scan:
                metrics_by_scan[base_name] = {'dice': [], 'hausdorff': []}
            metrics_by_scan[base_name]['dice'].append(dice_score)
            metrics_by_scan[base_name]['hausdorff'].append(hausdorff_distance)
            
            if phase not in metrics_by_phase:
                metrics_by_phase[phase] = {'dice': [], 'hausdorff': []}
            metrics_by_phase[phase]['dice'].append(dice_score)
            metrics_by_phase[phase]['hausdorff'].append(hausdorff_distance)
            
            print(f"{filename}: Dice score = {dice_score:.4f}, Hausdorff Distance = {hausdorff_distance:.4f}")
    
    # Print average metrics for each scan
    for base_name, metrics in metrics_by_scan.items():
        avg_dice = np.mean(metrics['dice'])
        avg_hausdorff = np.mean(metrics['hausdorff'])
        print(f"{base_name}: Average Dice = {avg_dice:.4f}, Average Hausdorff Distance = {avg_hausdorff:.4f}")
    
    # Print average metrics for each phase
    for phase, metrics in metrics_by_phase.items():
        avg_dice = np.mean(metrics['dice'])
        avg_hausdorff = np.mean(metrics['hausdorff'])
        print(f"Phase {phase}: Average Dice = {avg_dice:.4f}, Average Hausdorff Distance = {avg_hausdorff:.4f}")

if __name__ == "__main__":
    pred_folder = "~/my-scratch/outputs/pred"
    gt_folder = "~/my-scratch/outputs/gt"
    main(pred_folder, gt_folder)
