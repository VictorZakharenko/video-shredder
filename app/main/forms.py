from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField

class UploadVideoForm(FlaskForm):
    video_file = FileField('Video File')
    submit = SubmitField('Submit')
