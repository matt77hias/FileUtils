import numpy as np
import matplotlib.pyplot as plt

def plot_txt(file_path):
    plt.imshow(np.loadtxt(file_path))