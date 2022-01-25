#!/usr/bin/env python
# coding: utf-8
# SPDX-License-Identifier: MIT
# Copyright 2022 Marco Cominelli

import h5py
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv1D

# Configuration variables
csi_filename = 'antisense_dataset/csi_active_clean.h5'
positions_filename = 'antisense_dataset/positions.h5'
rx = 'rx1'

# Load data as 'float' values
csi = h5py.File(csi_filename, 'r')
positions = h5py.File(positions_filename, 'r')

training_set = np.array(csi.get(rx + '/training')).astype('float')
testing_set = np.array(csi.get(rx + '/testing')).astype('float')
validation_set = np.array(csi.get(rx + '/validation')).astype('float')

training_positions = np.array(positions.get('/training')).astype('float')
testing_positions = np.array(positions.get('/testing')).astype('float')
validation_positions = np.array(positions.get('/validation')).astype('float')

# Use training dataset (available to the attacker) to normalize the CSI
maxval = np.max(training_set)
training_set = training_set/maxval
testing_set = testing_set/maxval
validation_set = validation_set/maxval

# Print summary
print('CSI DATASET:')
print('  Training set size =', training_set.shape)
print('   Testing set size =', testing_set.shape)
print('Validation set size =', validation_set.shape)
print('---------------------------------------------')
print('GROUND TRUTH:')
print('  Training set size =', training_positions.shape)
print('   Testing set size =', testing_positions.shape)
print('Validation set size =', validation_positions.shape)

# Define CNN model
earlystopping_cb = tf.keras.callbacks.EarlyStopping(monitor='accuracy',patience=3,mode='max')
num_neurons_first_layer = training_set.shape[1:]

model = Sequential()
model.add(Conv1D(30, 5, padding='same', activation='relu', input_shape=num_neurons_first_layer))
model.add(Conv1D(50, 5, padding='same', activation='relu'))
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(8, activation='softmax'))

model.compile(loss="categorical_crossentropy", optimizer="adam",metrics=['accuracy'])

# Train the CNN
model.fit(
    training_set, training_positions,
    batch_size=100, epochs=100, shuffle=True,
    callbacks=[earlystopping_cb],
    verbose=1);

# Evaluate results
results = model.evaluate(testing_set, testing_positions)
print(results)

