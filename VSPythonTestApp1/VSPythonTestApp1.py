"""
This is the tutorial for Python in Visual Studio. Step 6. 
https://learn.microsoft.com/en-us/visualstudio/python/tutorial-working-with-python-in-visual-studio-step-06-working-with-git
"""

from math import cos, radians
import numpy as np # installed with matplotlib
import matplotlib.pyplot as plt

def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

main()