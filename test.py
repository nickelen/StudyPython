import os, glob

#更改当前工作目录
print(os.getcwd())
os.chdir('/Users/Administrator/Desktop')
print(os.getcwd())
print(glob.glob('py/*.py'))

#列表解析
os.chdir('/Users/Administrator/Desktop/py')
pys = glob.glob('*.py')
changed_pys = [os.path.join(os.getcwd(), elem) for elem in pys ]
print(changed_pys)

#列表解析后面可以跟if来对列表作filter
pys2 = glob.glob('*.py')
changed_pys = [os.path.join(os.getcwd(), f) for f in pys2 if os.stat(f).st_size > 60]
print(changed_pys)

