# 1) A function to extract dataset
def unzip_rawdata(path):
    import zipfile
    rawdata = zipfile.ZipFile(path)
    rawdata.extractall()
    rawdata.close()
    

# 2) Function that gives a vague idea of what is in a dataset
def dir_explorer(path):
    import os
    import matplotlib.pyplot
    import warnings
    warnings.filterwarnings("ignore")
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
    matplotlib.pyplot.figure(figsize=(16,16))
    matplotlib.pyplot.subplot(1,3,1)
    matplotlib.pyplot.pie([pie['train'],pie['test']],labels=pie.keys(),autopct='%.1f%%')
    matplotlib.pyplot.title('Train vs Test')
    matplotlib.pyplot.subplot(1,3,2)
    matplotlib.pyplot.pie([value['train']],autopct=lambda p : '{:.0f}%  ({:,.0f})'.format(p,p * sum(value['train'])/100),labels=label['train'])
    matplotlib.pyplot.title('Contents of training dataset')
    matplotlib.pyplot.subplot(1,3,3)
    matplotlib.pyplot.pie([value['test']],autopct=lambda p : '{:.0f}%  ({:,.0f})'.format(p,p * sum(value['test'])/100),labels=label['test'])
    matplotlib.pyplot.title('Contents of testing dataset')
    matplotlib.pyplot.show()
        
# 3) Custom function i use for some unknown reasons.
def giver():
    import re
    from datetime import datetime
    return re.sub('[:, ,.,-]',"",str(datetime.now()))

# 4) Custom call-back function for tensorflow board
def tensorboard_callback(dir_name,exp_name):
    import tensorflow
    log_dir = dir_name + "/" + exp_name + "/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = tensorflow.keras.callbacks.TensorBoard(log_dir=log_dir)
    print(f"Saving TensorBoard log files to: {log_dir}")
    return tensorboard_callback