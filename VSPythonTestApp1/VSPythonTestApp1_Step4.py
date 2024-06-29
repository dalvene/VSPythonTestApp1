"""
This is the tutorial for Python in Visual Studio. Step 4. 
https://learn.microsoft.com/en-us/visualstudio/python/tutorial-working-with-python-in-visual-studio-step-04-debugging
"""

from math import cos, radians

# Create a string with spaces proportional to a cosine of x in degrees
def make_dot_string(x):
    rad = radians(x)                        # cos works with radians
    numspaces = int(20 * cos(rad) + 20)    # scale to 0-40 spaces
    st = ' ' * numspaces + 'o'              # Place 'o' after the spaces
    return st

def main():
    for i in range(0, 1800, 12):
        s = make_dot_string(i)
        print(s)

main()