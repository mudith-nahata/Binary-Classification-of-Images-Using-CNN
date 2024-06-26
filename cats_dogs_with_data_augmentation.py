# -*- coding: utf-8 -*-
"""cats dogs with data augmentation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kuLxlltBPQ7g2aRCh4aPsTFrKIuBCk6P
"""

from keras.preprocessing.image import ImageDataGenerator

!mkdir -p ~/.kaggle
!cp kaggle.json ~/kaggle.json

!kaggle datasets download -d salader/dogs-vs-cats

import zipfile
zip_ref=zipfile.ZipFile('/content/dogs-vs-cats.zip','r')
zip_ref.extractall('/content')
zip_ref.close()

#batch_size=16

#this is the augmentation configuraton we will use for training
train_datagen=ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True

)

#this is the augmentation configuration we will use for testing
test_datagen=ImageDataGenerator(rescale=1./255)

#this is a generator will read pictures found in
#subfolders of 'content/train'and indefinately will generate
#batches of augmented image data

train_generator=train_datagen.flow_from_directory(
    '/content/train',
    target_size=(150,150), #all the images will be resized to 150X150
    batch_size=16,
    class_mode='binary' #since we use binary_crossentropy loss we need binary labels
)

#this is a similar generator for validation data
validation_generator=test_datagen.flow_from_directory(
    '/content/test',
    target_size=(150,150),
    batch_size=16,
    class_mode='binary'
)

import tensorflow
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten,Activation,Dropout

model=Sequential()

model.add(Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit_generator(
    train_generator,
    steps_per_epoch=2000//16,
    epochs=25,
    validation_data=validation_generator,
    validation_steps=1000//16
)