# 1) A function to extract dataset
def unzip_rawdata(path):
    import zipfile
    rawdata = zipfile.ZipFile(path)
    rawdata.extractall()
    rawdata.close()
    

# 2) Function that gives a vague idea of the number of files and folders in a dataset
def dir_explorer(path):
    import os
    for path,names,filenames in os.walk(path):
        print(f'There are {len(names)} folderes and {len(filesnames)} files in {path}')
        
        
# 3) Custom function i use for some weired reasons.
def giver():
    import re
    from datetime import datetime
    return re.sub('[:, ,.,-]',"",str(datetime.now()))