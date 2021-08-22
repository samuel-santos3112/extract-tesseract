from flask import Flask
from flask_cors import CORS

from app.ocr_endpoint import api

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.abspath('upload_image')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'


app.register_blueprint(api)
