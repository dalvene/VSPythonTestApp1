"""
This is the tutorial for Python in Visual Studio. Step 3.
https://learn.microsoft.com/en-us/visualstudio/python/tutorial-working-with-python-in-visual-studio-step-03-interactive-repl
"""

import sys
from math import cos, radians

# Create a string with spaces proportional to a cosine of x in degrees
def make_dot_string(x):
    return ' ' * int(20 * cos(radians(x)) + 20) + 'o'

# iPython interative mode freezes at step 3 whenever a command is entered (https://github.com/microsoft/PTVS/issues/7118)
# Right click "Send to interactive" does nothing. 
