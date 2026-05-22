from flask import Flask, request, jsonify
import fitz
import tempfile
import requests

app = Flask(__name__)

@app.route('/extract', methods=['POST'])
def extract():

    pdf_url = request.json.get("pdf_url")

    response = requests.get(pdf_url)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(response.content)
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