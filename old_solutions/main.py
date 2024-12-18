#editing images in buk https://dev.to/code_jedi/how-to-edit-images-in-bulk-with-python-in-20-lines-of-code--4b66 for later
#actually being used https://www.tensorflow.org/tutorials/images/classification

import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras

from keras import layers
from keras.models import Sequential

import pathlib 

data_dir = tf.keras.utils.get_file('/usr/local/bin/python3 /Users/rameezrauf/Desktop/BBall/test', extract=True)
data_dir = pathlib.Path(data_dir).with_suffix('')

image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)
