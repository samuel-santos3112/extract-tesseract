from flask import request, jsonify, Blueprint, render_template

from app.services import ocr_service as ocr

api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/')
def index():
    return render_template('index.html')

@api.route('/upload/ocr', methods=['GET', 'POST'])
def upload_ocr():
    return jsonify({'status' : 'ok'}, 200)

    
  