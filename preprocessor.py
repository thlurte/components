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
    pie = {'train': 0,'test': 0}
    value = {'train':[],'test':[]}
    label = {'train':[],'test':[]}
    for path,names,filenames in os.walk(path):
        if 'train' in path:
            pie['train'] += len(filenames)
            value['train'].append(len(filenames))
            label['train'].append(path.split('/')[-1])
        else:
            pie['test'] += len(filenames)
            value['test'].append(len(filenames))
            label['test'].append(path.split('/')[-1])
    matplotlib.pyplot.figure(figsize=(9,9))
    matplotlib.pyplot.pie([pie['train'],pie['test']],labels=pie.keys(),autopact='%.1f%%')
    matplotlib.pyplot.title('Train vs Test')
    matplotlib.pyplot.show()
    matplotlib.pyplot.figure(figsize=(9,9))
    matplotlib.pyplot.pie([value['train']],autopct=lambda p : '{:.2f}%  ({:,.0f})'.format(p,p * sum(value['train'])/100),labels=label['train'])
    matplotlib.pyplot.title('Contents of training dataset')
    matplotlib.pyplot.show()
    matplotlib.pyplot.figure(figsize=(9,9))
    matplotlib.pyplot.pie([value['test']],autopct=lambda p : '{:.2f}%  ({:,.0f})'.format(p,p * sum(value['test'])/100),labels=label['test'])
    matplotlib.pyplot.title('Contents of testing dataset')
    matplotlib.pyplot.show()
    
    
    
        
        
# 3) Custom function i use for some weired reasons.
def giver():
    import re
    from datetime import datetime
    return re.sub('[:, ,.,-]',"",str(datetime.now()))

