# import os
# import time
# from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
# from werkzeug.utils import secure_filename
# # import core_functions
# 
# UPLOAD_FOLDER = '/home/ThePhilosopher/image-supersizer/uploads/'
# PREDICTION_FOLDER = '/home/ThePhilosopher/image-supersizer/predictions/'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# 
# def allowed_file(filename):
    # return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# 
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# # model = core_functions.Predictor()
# 
# @app.route('/', methods=['GET', 'POST'])
# def index():
    # imagefilename = ""
# 
    # if request.method == 'POST':
        # # check if the post request has the file part
        # if 'file' not in request.files:
	    # flash('No file part')
	    # return redirect(request.url)
        # file = request.files['file']
        # # if user does not select file, browser also
        # # submit an empty part without filename
        # if file.filename == '': # Todo: bug. not working
            # flash('No selected file')
            # return redirect(request.url)
        # if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            # imagefilename = filename
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('prediction', filename=filename))
# 
    # return render_template("index.html", imagefilename=imagefilename)
# 
# @app.route('/prediction/<filename>')
# def prediction(filename):
    # # model.predict(filename)
    # os.system('predictor.py ' + filename)
    # while(not os.path.isfile(PREDICTION_FOLDER + filename)):
        # print("file doesn't exist yet")
        # time.sleep(3)
    # print("prediction created")
    # return send_from_directory(PREDICTION_FOLDER, filename)
# 
# if __name__ == "__main__":
    # app.run()

import os
import time
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "/home/ThePhilosopher/image-supersizer/uploads/"
PREDICTION_FOLDER = "/home/ThePhilosopher/image-supersizer/predictions/"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    imagefilename = ""

    if request.method == "POST":
        #check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            imagefilename = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('prediction', filename=filename))

    return render_template("index.html", imagefilename=imagefilename)

@app.route("/prediction/<filename>")
def prediction(filename):
    os.system('python3 predictor.py ' + filename)
    while (not os.path.isfile(PREDICTION_FOLDER + filename)):
        print("file doesn't exist yet")
        time.sleep(3)
    print("prediction created")
    return send_from_directory(PREDICTION_FOLDER, filename)

if __name__ == "__main__":
    app.run()
