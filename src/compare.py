import numpy as np
import os
from PIL import Image

def check(path):
    for fname1 in os.listdir(path):
        for fname2 in os.listdir(path):
            if fname1 != fname2:
                if not (check_equal_files(path + '/' + fname1, path + '/' + fname2)):
                    print('error: ' + fname1 + ' vs ' + fname2)
    
def check_equal_images(A, B):
    return np.max(A - B) == 0

def check_equal_files(fname1, fname2):
    return operate(fname1, fname2, check_equal_images)

def diff_images(A, B):
    return A - B
    
def diff_files(fname1, fname2):
    return operate(fname1, fname2, diff_images)
    
def operate(fname1, fname2, f):
    A = PIL2array(Image.open(fname1))
    B = PIL2array(Image.open(fname2))
    return f(A,B)
    
def PIL2array(img):
    return np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)

#if __name__ == "__main__":