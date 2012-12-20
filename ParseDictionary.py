#字典解析
import os, glob
#import lib.humansize as humansize
from lib import humansize

metadata = [(xml, os.stat(xml)) for xml in glob.glob('xml\*.xml')] 
print(metadata[0])
metadata_dic = {xml:os.stat(xml) for xml in glob.glob('xml\*.xml')}
print({key:os.stat(key).st_size for key, value in metadata_dic.items()})
keys = list(metadata_dic.keys())
print(keys)
print(metadata_dic['xml\Basics021.xml'].st_size)
print({k:humansize.approximate_size(v.st_size) \
	for k,v in metadata_dic.items() if v.st_size > 1500})