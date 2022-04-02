import os
from glob import glob

glob.dirname = os.path.dirname(__file__)

dirname = os.path.dirname(__file__)

print(dirname)
