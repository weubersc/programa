import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt

class contorno():


    def __init__(self,x,y,z):
        lat = np.array(x,dtype=float)
        long = np.array(y, dtype=float)
        z=np.array(z, dtype=float)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(lat, long)
        plt.scatter(x, y, s=z)
        plt.show()

