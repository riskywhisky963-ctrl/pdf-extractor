from flask import Flask, request, jsonify
import fitz
import tempfile

app = Flask(__name__)

@app.route('/extract', methods=['POST'])
def extract():

    uploaded_file = request.files['file']

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        uploaded_file.save(f.name)
        pdf_path = f.name

    doc = fitz.open(pdf_path)

    pages = []

    for i, page in enumerate(doc):
        text = page.get_text()

        pages.append({
            "page": i + 1,
            "text": text
        })

    return jsonify(pages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
