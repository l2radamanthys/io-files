import os
from flask import (
    Blueprint,
    request,
    flash,
    redirect,
    send_from_directory,
    render_template,
)
from werkzeug.utils import secure_filename
from urllib.parse import quote_plus


upload_folder = "/tmp"
routes_bp = Blueprint("app", __name__)


def allowed_file(filename):
    # TODO no restricted file types
    return True


@routes_bp.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(os.path.join(upload_folder, filename))
            file.save(os.path.join(upload_folder, filename))
            return f"{request.host_url}uploads/{quote_plus(filename)}"

    else:
        return render_template("index.html")


@routes_bp.route("/uploads/<name>")
def download_file(name):
    return send_from_directory(upload_folder, name)
