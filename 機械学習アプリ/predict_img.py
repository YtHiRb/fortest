from flask import Flask, flash, request, redirect, url_for
import secrets
import os
from werkzeug.utils import secure_filename
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import keras, sys
from PIL import Image
import numpy as np

classes = ["monkey", "boar", "crow"]
num_class = len(classes)
img_size = 50

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = set(["jpg", "png", "gif"])

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
secret = secrets.token_urlsafe(32)
app.secret_key = secret

def allowed_file(filename):
    return "." in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["POST","GET"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("no selected file")#flask特有のprint的なやつ。
            return redirect(request.url)#失敗したので元のページにリダイレクト
        file = request.files["file"]
        if file.filename == "":
            flash("no file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # return redirect(url_for("download_file", tekitou=filename))#このtekitouという部分はなんでもよくて、
        #あとに書いているdownload_fileの関数のところで
        #@app.route("/uploads/<tekitou>")
        #と書いてもわかるように
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            model = keras.models.load_model("env_for_api/animal_cnn.h5")
            image = Image.open(filepath).convert("RGB").resize((img_size,img_size))
            data = np.asarray(image)
            X = []
            X.append(data)
            X = np.array(X)

            result = model.predict([X])[0]
            predicted = np.argmax(result)
            percentage = int(result[predicted]*100)
            return classes[predicted] + str(percentage) + " %"
            
    return '''
    <!doctype html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>あっぷろーどにゅーふぁいる</title></head>
    <body>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
    <p><input type=file name=file>
    <input type=submit value=Upload>
    </form>
    </body>
    </html>
    '''

from flask import send_from_directory

@app.route("/uploads/<tekitou>")
def download_file(tekitou):#引数を上のtekitouにしないといけない
    return send_from_directory(app.config["UPLOAD_FOLDER"], tekitou)