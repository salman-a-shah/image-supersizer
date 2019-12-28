import os
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import core_functions

UPLOAD_FOLDER = './uploads/'
PREDICITON_FOLDER = './predictions/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
model = core_functions.Predictor()

@app.route('/', methods=['GET', 'POST'])
def index():
	imagefilename = ""
	
	if request.method == 'POST':
	    # check if the post request has the file part
	    if 'file' not in request.files:
	        flash('No file part')
	        return redirect(request.url)
	    file = request.files['file']
	    # if user does not select file, browser also
	    # submit an empty part without filename
	    if file.filename == '': # Todo: bug. not working
	        flash('No selected file')
	        return redirect(request.url)
	    if file and allowed_file(file.filename):
	        filename = secure_filename(file.filename)
	        imagefilename = filename
	        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	        return redirect(url_for('prediction',
	                                filename=filename))
	        
	return render_template("index.html", imagefilename=imagefilename)

@app.route('/start', methods=['GET', 'POST'])
def upload_file():
	imagefilename = ""
	
	if request.method == 'POST':
	    # check if the post request has the file part
	    if 'file' not in request.files:
	        flash('No file part')
	        return redirect(request.url)
	    file = request.files['file']
	    # if user does not select file, browser also
	    # submit an empty part without filename
	    if file.filename == '': # Todo: bug. not working
	        flash('No selected file')
	        return redirect(request.url)
	    if file and allowed_file(file.filename):
	        filename = secure_filename(file.filename)
	        imagefilename = filename
	        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	        return redirect(url_for('prediction',
	                                filename=filename))
	return render_template("upload.html", imagefilename=imagefilename)

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)

@app.route('/prediction/<filename>')
def prediction(filename):
	model.predict(filename)
	return send_from_directory(PREDICITON_FOLDER, filename)

if __name__ == "__main__":
	app.run(debug=True)