# 1) A function to extract dataset
def unzip_rawdata(path):
    import zipfile
    rawdata = zipfile.ZipFile(path)
    rawdata.extractall()
    rawdata.close()
    

# 2) Function that gives a vague idea of the number of files and folders in a dataset
def dir_explorer(path):
    import os
    import matplotlib.pyplot
    a = {'train': 0
        ,'test': 0}
    for path,names,filenames in os.walk(path):
        print(f'There are {len(names)} folderes and {len(filenames)} files in {path}')
        if 'train' in path:
            a['train'] += len(filenames)
        else:
            a['test'] += len(filenames)
    return a
    
        
        
# 3) Custom function i use for some weired reasons.
def giver():
    import re
    from datetime import datetime
    return re.sub('[:, ,.,-]',"",str(datetime.now()))

