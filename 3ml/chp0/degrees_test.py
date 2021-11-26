from __future__ import absolute_import, division, print_function, unicode_literals
import os
import tensorflow.compat.v2 as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.models import model_from_json
from keras.models import load_model

celsius_q    = np.array([-40, -10, 0, 7.778, 15, 22.222, 37.778], dtype=float)
fahrenheit_a = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)
l0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([l0])
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
history = model.fit(celsius_q, fahrenheit_a, epochs=5000, verbose=False)
print("Завершили тренировку модели")
# print(history.history['loss'])
delta = 0.0 
# for cdeg in range(-50,150):
#     fdeg = (cdeg/(5/9)) + 32
#     mddeg = model.predict([cdeg])
#     delta += fdeg - mddeg 
#     print(f'{cdeg} °C = {fdeg} °F; {mddeg} °Fm; delta = {fdeg - mddeg}')
# print(delta)

model_json = model.to_json()
with open("model_num.json", "w") as json_file:
    json_file.write(model_json)

# serialize weights to HDF5
model.save_weights("model_num.h5")