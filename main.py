from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename



app = Flask(__name__)


 


@app.route("/")
def hello_world():
   return render_template('index.html')


@app.errorhandler(404) 
def not_found(e): 
   return render_template("404.html") 



@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return render_template("uploader.html") 

		
if __name__ == '__main__':
   app.run(debug = True)