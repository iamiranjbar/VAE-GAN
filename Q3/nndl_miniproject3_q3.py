# -*- coding: utf-8 -*-
"""NNDL Miniproject3 Q3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/138H3uQIu28Cm-TTq7ImOjMf11FJvllu9

# StyleGAN

## Imports and mounting drive
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 1.x
import tensorflow
from google.colab import drive
drive.mount('/content/drive')

"""## Get code of StyleGAN"""

!git clone https://github.com/NVlabs/stylegan.git
!ls /content/stylegan/

import sys
sys.path.insert(0, "/content/stylegan")
import dnnlib

"""## Run pretrained example"""

!python /content/stylegan/pretrained_example.py

