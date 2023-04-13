import numpy as np
import os
from PIL import Image as im

data_dir = 'D:/DATASET-1/Dataset-1_high_resolution'
output_file = 'D:/DATASET-1/processed_data/data.npy'

# load data
files = os.listdir(data_dir)
num_data = 20 #len(files)

# initialize data array by finding dimensions
# MUST DOWNSAMPLE ARRAY otherwise too much info

image_PATH = data_dir + '/' + files[0]
img = im.open(image_PATH)
img_arr = np.asarray(img)
sz = len(np.ravel(img_arr))
X = np.zeros((num_data, sz))

# store data in array
for i in np.arange(num_data):
    image_PATH = data_dir + '/' + files[i]
    img = im.open(image_PATH)
    img_arr = np.asarray(img)
    X[i] = np.ravel(img_arr)
    # normalize data?

with open(output_file, 'wb') as f:
    np.save(f, X)
    f.close()