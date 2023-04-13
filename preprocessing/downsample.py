from PIL import Image as im
import numpy as np
import os

# photo resolution
# 5184x3456, 72dpi

# target resolution
# 2560x1920
data_size = (5184, 3456)
target_size = (2560, 1920)
if data_size < target_size:
    print("warning: loss in image quality. image is upsampled")

dir = 'D:/DATASET-1/Dataset-1_high_resolution'
mod_dir = os.curdir
files = os.listdir(dir)
num_files = len(files)

# Params for cropping image
left = (target_size[0]-target_size[1])/2
top = 0
right = target_size[0]-left
bottom = target_size[1]

# for file_IX in np.arange(0, num_files):

PATH = dir + '/' + files[0]
mod_PATH = mod_dir + '/' + files[0]
img = im.open(PATH)
img=img.convert('RGB')

img_r = img.getchannel('R')
img_g = img.getchannel('G')
img_b = img.getchannel('B')

r = img_r.resize(target_size)
r = r.crop((left, top, right, bottom))
g = img_g.resize(target_size)
g = g.crop((left, top, right, bottom))
b = img_b.resize(target_size)
b = b.crop((left, top, right, bottom))

ds_array = np.stack((r, g, b), axis=-1)
image = im.fromarray(ds_array)
image.save(mod_PATH)
print(np.shape(image))






