import os
from flask import Blueprint, request, flash, redirect, url_for, send_from_directory, current_app
from werkzeug.utils import secure_filename
from urllib.parse import quote_plus


upload_folder = ""
#upload_folder = current_app.config['UPLOAD_FOLDER'] 

routes_bp = Blueprint("app", __name__)

def allowed_file(filename):
    #TODO no restricted file types
    return True


@routes_bp.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_folder, filename))
            #return redirect(url_for('download_file', name=filename))
            return f"{request.host_url}uploads/{quote_plus(filename)}"

    else:
        return '''
    <!doctype html>
    <html lang="es">
    <head>
    <title>Subir Archivo</title>
    </head>
    <body>
    <h1>Subir Archivo</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file> <br>
      <input type=submit value=Upload>
    </form>
    </body>
    </html>
    '''

@routes_bp.route('/uploads/<name>')
def download_file(name):
    print("::", name)
    return send_from_directory(upload_folder, name)