from flask import request, jsonify, Blueprint, render_template

from app.services import ocr_service as ocr

api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@api.route('/upload/ocr', methods=['POST'])
def upload_ocr():
    image_path = ocr.saveImage(request)
    processed_image = ocr.readImage(image_path)
    return jsonify(processed_image), 200




