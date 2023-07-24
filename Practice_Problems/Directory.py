from os import listdir
from os.path import isfile , join

fileList = [f for f in listdir('/Windows') if isfile(join('/Windows',f))]

print(f"File list of Windows File {fileList}")