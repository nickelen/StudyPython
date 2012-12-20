'''
Created on Dec 19, 2012

@author: dchen1
'''
import os

previousPath = os.getcwd()
print(previousPath)
os.chdir('/daniel2/python_workspace1/DiveIntoPython3/src/main')
print(os.getcwd())

print(os.path.join(previousPath,'humansize.py'))
print(os.path.join(previousPath+'/','humansize.py'))
print(os.path.expanduser('~'))

mypath = os.path.join(os.path.expanduser('~'), 'mytestpath1', 'mytestpath2', 'humansize.py')
print(mypath)
(filepath, filename) = os.path.split(mypath)
print(filepath)
print(filename)
(shortname, extension) = os.path.splitext(filename)
print(shortname)
print(extension)