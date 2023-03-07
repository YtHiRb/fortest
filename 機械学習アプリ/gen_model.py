# %%
from PIL import Image
import os, glob
import numpy as np
# from sklearn import cross_validation
import sklearn.model_selection as cross_validation

classes = ["monkey", "boar", "crow"]
img_size = 50

X = []
y = []

for i, class_ in enumerate(classes):
    path = "./env_for_api/" + class_ + "/"
    file = glob.glob(path + "*.jpg")
    for j, f in enumerate(file):
        if j > 150:
            break
        img = Image.open(f).convert("RGB").resize((img_size,img_size))
        img = np.asarray(img)
        X.append(img)
        y.append(i)

X = np.array(X)
y = np.array(y)

# %%
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
from keras import optimizers

n_classes = len(classes)

def main():
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, stratify=y)
    X_train = X_train.astype(float) / 255
    X_test = X_test.astype(float) / 255
    y_train = np_utils.to_categorical(y_train, n_classes)
    y_test = np_utils.to_categorical(y_test, n_classes)
    
    model = model_train(X_train, y_train)
    model_eval(model, X_test, y_test)
    model.save("./env_for_api/animal_cnn.h5")

# %%
def model_train(X, y):
    model = Sequential()
    model.add(Conv2D(32,(3,3),padding="same",input_shape=X.shape[1:]))
    model.add(Activation("relu"))
    model.add(Conv2D(32,(3,3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64,(3,3),padding="same"))
    model.add(Activation("relu"))
    model.add(Conv2D(64,(3,3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation("relu"))
    model.add(Dropout(0.5))
    model.add(Dense(3))
    model.add(Activation("softmax"))

    opt = optimizers.RMSprop(lr=0.0001, decay=1e-6)
    model.compile(loss="categorical_crossentropy",
                  optimizer=opt,
                  metrics=["accuracy"])

    model.fit(X, y, batch_size=32, epochs=100)
    return model

# %%
def model_eval(model, X, y):
    scores = model.evaluate(X, y, verbose=1)
    print("test loss:",scores[0])
    print("test accuracy:",scores[1])

# %%
if __name__ == "__main__":
    main()


