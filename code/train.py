from config import KERAS_IMAGES
from pathlib import Path
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras import models
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.optimizers import Adam

def preprocess(images, labels):
  return preprocess_input(images), labels

vaseDataset = image_dataset_from_directory(
    KERAS_IMAGES, labels='inferred', label_mode='binary',
    class_names=None, color_mode='rgb', batch_size=32, image_size=(224,
    224), shuffle=True, seed=34829437, validation_split=.2, subset="validation", 
    interpolation='bilinear', follow_links=False,
    crop_to_aspect_ratio=False
)

vaseDataset = vaseDataset.map(preprocess)

model = models.Sequential()

base_model = MobileNetV2(weights='imagenet',include_top=False,input_shape=(224,224,3))

for layer in base_model.layers[:-4]:
    
    layer.trainable = False

model.add(base_model)

model.add(Flatten())

model.add(Dense(1024, activation = 'relu'))

model.add(Dropout(0.5))

model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer=Adam(lr=0.0001),metrics=['accuracy'])

model.fit(vaseDataset,batch_size=64)
