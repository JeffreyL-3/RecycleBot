from flask import Flask, request, render_template, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
from interface import simple_output
import key
import shutil

app = Flask(__name__)

# Configure folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def empty_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

# Initial page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#Dynamic page updates
@app.route('/process', methods=['POST'])
def process():
    empty_folder(app.config['UPLOAD_FOLDER'])

    file = request.files['image']
    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)

        # Get other form data
        
        api_key = request.form.get('api_key')
        key.setKey(api_key)
                   
        town = request.form.get('town', 'Dedham')
        state = request.form.get('state', 'Massachusetts')
        object = request.form.get('object', 'object')
        personality = request.form.get('personality', 'a recycling expert')

        result_code, detected_object, header, details, *costOutput = simple_output(image_path, town, state, object, personality)
        # Return JSON response
        return jsonify({
            'result_code': result_code, 
            'detected_object': detected_object,
            'header': header, 
            'details': details, 
            'costOutput': costOutput if costOutput else None
        })

    else:
        return jsonify({'error': 'Invalid file format'}), 400

if __name__ == '__main__':
    app.run(debug=True)