
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.python.keras.layers import Dense, Activation
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.optimizers import Adam
from tensorflow.python.keras.metrics import categorical_crossentropy
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.applications import imagenet_utils
from sklearn.metrics import confusion_matrix
import itertools
import os
import shutil
import random
import matplotlib.pyplot as pit

# Download the mobile net model

mobile = tf.keras.applications.mobilenet.MobileNet()


def prepare_images(file):
    img_path = "ScriptDataBaddie"
    img = image.load_img(img_path + file ,target_size=(224,224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array,axis=0)
    return tf.keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)



from IPython.display import Image
Image(filename="ScriptDataBaddie/-mwRkx1g.jpeg",width=300,height=200)

preprocessed_image = [prepare_images("-mwRkx1g.jpeg")]
predictions = mobile.predict(preprocessed_image)
results = imagenet_utils.decode_predictions(predictions)
results