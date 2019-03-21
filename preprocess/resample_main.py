import sys
import os
import numpy as np
import nibabel as nib
import argparse

from Resample import resample, save_file, mask2binary

parser = argparse.ArgumentParser()
parser.add_argument('--i', dest = "input_dir")
parser.add_argument('--o', dest = "output_dir")

args = parser.parse_args()

def resample(image=""):
    image = nib.load(image)
    print('original image size', image.get_data().shape)

    resampled_image, _ = resample(img_array=image, target_voxel=(1,1,1))
    print('resampled image size', resampled_image.shape)

    result_image = mask2binary(resampled_image)
    
    return result_image

data_path = args.input_dir
save_path = args.output_dir

if __name__ == "__main__":
        for mask_image in os.listdir(data_path):
                if '.DS_Store' in mask_image : continue
                image_path = os.path.join(data_path, mask_image)
                result_image = preprocess(image=image_path)
                save_file(mask_image, result_image, save_path, (1,1,1))
                print(mask_image, ' Done')