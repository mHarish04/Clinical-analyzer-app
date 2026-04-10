"""
Medical Report Processor - Flask Backend
Accepts patient form data + PDF, sends both to Claude LLM, returns suggestions.
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

from pdf_processor import extract_text_from_pdf
from ai_processor import analyze_report_with_claude

load_dotenv()

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'message': 'Backend is running'})


@app.route('/api/analyze', methods=['POST'])
def analyze():
    """
    Main endpoint: Accept patient form fields + PDF, send both to Claude, return suggestions.

    Form fields (multipart/form-data):
      - name         (required)
      - age          (required)
      - gender       (required)
      - symptoms     (optional – free-text notes from the user)
      - file         (required – PDF report)
    """
    try:
        # --- validate required form fields ---
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        gender = request.form.get('gender', '').strip()
        symptoms = request.form.get('symptoms', '').strip()

        if not name or not age or not gender:
            return jsonify({'error': 'name, age, and gender are required'}), 400

        # --- validate file ---
        if 'file' not in request.files:
            return jsonify({'error': 'No PDF file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        if not allowed_file(file.filename):
            return jsonify({'error': 'Only PDF files are allowed'}), 400

        # --- save & extract PDF ---
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        pdf_text = extract_text_from_pdf(filepath)
        if not pdf_text:
            return jsonify({'error': 'No text could be extracted from the PDF'}), 400

        # Cap at 12,000 chars (~3,000 tokens) to stay within limits while keeping full context
        if len(pdf_text) > 12000:
            pdf_text = pdf_text[:12000] + '\n\n[... report truncated for length ...]'

        print(f"[analyze] Patient: {name} | PDF chars: {len(pdf_text)}")

        # --- call Claude ---
        patient_info = {
            'name': name,
            'age': age,
            'gender': gender,
            'symptoms': symptoms,
        }
        result = analyze_report_with_claude(patient_info, pdf_text)

        if result['status'] == 'success':
            return jsonify({
                'status': 'success',
                'analysis': result['analysis'],
                'model': result.get('model'),
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'error': result.get('error', 'Claude processing failed'),
            }), 500

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
