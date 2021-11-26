from __future__ import absolute_import, division, print_function, unicode_literals
import os
import tensorflow.compat.v2 as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.models import model_from_json
from keras.models import load_model

celsius_q    = np.array([-40, -10, 0, 7.778, 15, 22.222, 37.778], dtype=float)
fahrenheit_a = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

json_file = open('model_num.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model_num.h5")

loaded_model.save('model_num.hdf5')
loaded_model=load_model('model_num.hdf5')
delta = 0.0 
for cdeg in range(-50,150):
    fdeg = (cdeg/(5/9)) + 32
    mddeg = loaded_model.predict([cdeg])
    delta += fdeg - mddeg 
    print(f'{cdeg} °C = {fdeg} °F; {mddeg} °Fm; delta = {fdeg - mddeg}')
print(delta)