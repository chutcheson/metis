from config import KERAS_IMAGES
from pathlib import Path
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Conv2D, MaxPooling2D, Flatten, InputLayer, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.regularizers import l2

t = image_dataset_from_directory(
    KERAS_IMAGES, labels='inferred', label_mode='binary',
    class_names=None, color_mode='rgb', batch_size=32, image_size=(224,
    224), shuffle=True, seed=34829437, validation_split=.2, subset="training", 
    interpolation='bilinear', follow_links=False,
    crop_to_aspect_ratio=False
)

v = image_dataset_from_directory(
    KERAS_IMAGES, labels='inferred', label_mode='binary',
    class_names=None, color_mode='rgb', batch_size=32, image_size=(224,
    224), shuffle=True, seed=34829437, validation_split=.2, subset="validation", 
    interpolation='bilinear', follow_links=False,
    crop_to_aspect_ratio=False
)

model = Sequential()
model.add(InputLayer(input_shape=(224,224,3)))
model.add(Conv2D(filters=20, kernel_size=3, activation='relu',kernel_regularizer=l2(1e-5)))
model.add(MaxPooling2D())
model.add(Conv2D(filters=20, kernel_size=3, activation='relu',kernel_regularizer=l2(1e-5)))
model.add(MaxPooling2D())
model.add(Dropout(.2))
model.add(Flatten())
model.add(Dropout(.2))
model.add(Dense(100,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(t,validation_data=v,epochs=25,callbacks=[EarlyStopping(patience=3)])
