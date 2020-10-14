from app.main import bp
from flask_login import login_required
from flask import render_template
from app.main.forms import UploadVideoForm
from flask import send_from_directory, send_file
from flask import current_app
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename
from app.main.utils import get_metadata
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
    video_length, video_fps = get_metadata(os.path.join(current_app.config['UPLOAD_PATH'], filename))
    metadata = 'video_length = {}\nvideo_fps = {}'.format(video_length, video_fps)
    return render_template('video.html', filename=filename, metadata=metadata)

@bp.route('/shredder', methods=['POST'])
def shredder():
    uploaded_file = request
    timestamps = request
    link_to_zip = {}
    return link_to_zip