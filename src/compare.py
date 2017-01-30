import cv2
import numpy as np

from name import concat
from os import listdir

path = 'C:\Users\Matthias\Documents\Courses\Masterproef\Tests\Session 2.0\A'

#optimization: binary tree comparison
def check(path):
    for fname1 in listdir(path):
        for fname2 in listdir(path):
            if fname1 < fname2:
                A = cv2.imread(concat(path, fname1), 1)
                B = cv2.imread(concat(path, fname2), 1)  
                if not np.array_equal(A, B):
                    s = fname1 + ' vs ' + fname2
                    nz = np.nonzero(A - B)
                    Dout = A.copy()
                    xs = nz[0] 
                    ys = nz[1]
                    for i in range(xs.shape[0]):
                        Dout[xs[i],ys[i],:] = np.array([0,0,255], dtype=np.uint8)
                        
                    print('error [' + str(xs.shape[0]) + ']: ' +  s)
                    
                    cv2.imshow(s, Dout)