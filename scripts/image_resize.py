from PIL import Image
import os
from time import time

new_width = 200
new_height = 66

root_path = '../../udacity-steering-image-dataset-part-3/center/'
rootSave = '../../udacity-steering-image-dataset-mini/center-third/'
slash = '/'
root = os.listdir(root_path)
print 'Iterating through folders:'
t0 = time()
i = 0
# Iterating through the item directories to get dir
for files in root:
	img = Image.open(root_path + files)
	width = img.size[0]
	height = img.size[1]
	img2 = img.resize((new_width, new_height), Image.ANTIALIAS)
	saveStr = rootSave  + files
	img2.save(saveStr, "PNG")
	i = i + 1
total_time = time() - t0
print 'Counted ', str(i),' files'
print 'Resize time: ', total_time, 's'
