import os
from time import time

root_path = '../center-first/'
slash = '/'
root = os.listdir(root_path)
text_file = open('../../datasetOneDirectory.txt', "w")
print 'Iterating through folders:'
t0 = time()

# Iterating through the item directories to get dir
i = 0
for files in root:
	strWrite = files + '\n'
	text_file.write(strWrite)	
	i = i + 1

text_file.close()
total_time = time() - t0
print 'Counted ', str(i),' files'
print 'Resize time: ', total_time, 's'
