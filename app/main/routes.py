from app.main import bp
from flask_login import login_required
from flask import render_template
from app.main.forms import UploadVideoForm
from flask import send_from_directory, send_file
from flask import current_app
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename
from app.main.utils import split_segment
import os

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

@bp.route('/', methods=['POST'])
@bp.route('/index', methods=['POST'])
def upload_video():
    uploaded_file = request.files.get('file')
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        uploaded_file.save(os.path.join(current_app.config['UPLOAD_PATH'], filename))
    return {'filename':filename}


@bp.route('/uploads/<filename>')
def uploads(filename):
    print(split_segment(filename, 2))
    return render_template('video.html', filename=filename)

# import imghdr
# import os
# from flask import Flask, render_template, request, redirect, url_for, abort, \
