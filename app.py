import os
import time
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import load_environment_variables

# Using custom built working directory
# because pythonanywhere recommends using absolute paths
# to avoid issues
WORKING_DIRECTORY = os.environ.get("WORKING_DIRECTORY")
PYTHON = os.environ.get("PYTHON")

UPLOAD_FOLDER =  WORKING_DIRECTORY + "uploads/"
PREDICTION_FOLDER = WORKING_DIRECTORY + "predictions/"
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
    # TODO: seperate this into a predict() method and load_if_exists() method
    os.system(PYTHON + " predictor.py " + filename)
    while (not os.path.isfile(PREDICTION_FOLDER + filename)):
        print("file doesn't exist yet")
        time.sleep(3)
    print("prediction created")
    return send_from_directory(PREDICTION_FOLDER, filename)

if __name__ == "__main__":
    app.run()
