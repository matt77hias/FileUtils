import os

def remove_fname_extension(fname):
    return os.path.splitext(fname)[0]

def change_fname_extension(fname, extension):
    return remove_fname_extension(fname) + '.' + extension
    
def concat(path, fname):
    return path + '/' + fname