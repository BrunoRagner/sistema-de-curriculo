import os
from flask import Flask, flash, request, redirect, url_for, render_template, make_response
from werkzeug.utils import secure_filename




UPLOAD_FOLDER = '/home/bruno/Documentos/bruno/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

 
app.logger.debug('Um valor para depuração')
app.logger.warning('Ocorreu um avis (%d apples)', 42)
app.logger.error('Ocorreu um erro')



@app.route("/")
def index():
   return render_template('index.html')


@app.route("/")
def Cookie():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp



@app.route("/vaga")
def vaga():
   return render_template("vaga.html")

   
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