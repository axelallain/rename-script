# rename.py

import os

path = './'
files = os.listdir(path)

for index, file in enumerate(files):
	if file != "rename.py":
		os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index+1) + ".png"]))) 
