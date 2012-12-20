'''
Created on Dec 19, 2012

@author: dchen1
'''
import os
import glob
import time
import humansize

os.chdir('/daniel2/python_workspace1/DiveIntoPython3/src/main')
pyfiles = glob.glob('python/*.py')
print(pyfiles)
print(os.path.join(os.getcwd(), pyfiles[-2]))

metadata = os.stat(os.path.join(os.getcwd(), pyfiles[-2]))
print(metadata.st_mtime)
print(time.localtime(metadata.st_mtime))
print(metadata.st_size)
print(humansize.approximate_size(metadata.st_size))

print(os.path.realpath('test.py'))


