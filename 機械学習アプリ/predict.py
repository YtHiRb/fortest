from PIL import Image
import numpy as np
# from sklearn import cross_validation
import sklearn.model_selection as cross_validation
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import keras
import sys

classes = ["monkey", "boar", "crow"]
num_class = len(classes)
img_size = 50

def build_model():
    # model = Sequential()
    # model.add(Conv2D(32,(3,3),padding="same",input_shape=(50,50,3)))
    # model.add(Activation("relu"))
    # model.add(Conv2D(32,(3,3)))
    # model.add(Activation("relu"))
    # model.add(MaxPooling2D(pool_size=(2,2)))
    # model.add(Dropout(0.25))

    # model.add(Conv2D(64,(3,3),padding="same"))
    # model.add(Activation("relu"))
    # model.add(Conv2D(64,(3,3)))
    # model.add(Activation("relu"))
    # model.add(MaxPooling2D(pool_size=(2,2)))

    # model.add(Flatten())
    # model.add(Dense(512))
    # model.add(Activation("relu"))
    # model.add(Dropout(0.5))
    # model.add(Dense(3))
    # model.add(Activation("softmax"))

    # opt = keras.optimizers.RMSprop(lr=0.0001, decay=1e-6)
    # model.compile(loss="categorical_crossentropy",
    #               optimizer=opt,
    #               metrics=["accuracy"])

    model = keras.models.load_model("env_for_api/animal_cnn.h5")

    return model

def main():
    image = Image.open(sys.argv[1]).convert("RGB").resize((img_size,img_size))
    data = np.asarray(image)
    X = []
    X.append(data)
    X = np.array(X)
    model = build_model()

    result = model.predict([X])[0]
    predicted = np.argmax(result)
    percentage = int(result[predicted]*100)
    print("{} ({} %)".format(classes[predicted], percentage))

if __name__ == "__main__":
    main()