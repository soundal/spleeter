from flask import Flask, request, send_file
from spleeter.separator import Separator
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Directory for uploaded and output files
UPLOAD_FOLDER = '/path/to/upload'
OUTPUT_FOLDER = '/output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/separate', methods=['POST'])
def separate_audio():
    if 'audio' not in request.files:
        return "No audio file provided", 400
    file = request.files['audio']
    if file.filename == '':
        return "No file selected", 400
    if file:
        # Save the file
        filename = secure_filename(file.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(input_path)
        
        # Separate the audio
        separator = Separator('spleeter:2stems')
        separator.separate_to_file(input_path, OUTPUT_FOLDER)
        
        # Prepare output for download
        output_path_vocals = os.path.join(OUTPUT_FOLDER, 'vocals.wav')
        output_path_accompaniment = os.path.join(OUTPUT_FOLDER, 'accompaniment.wav')
        
        # Assuming you just want to return the vocals
        return send_file(output_path_vocals, as_attachment=True)

#if __name__ == '__main__':
 #   app.run(debug=True, host='0.0.0.0', port=5000)
