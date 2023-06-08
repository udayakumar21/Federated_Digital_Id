from flask import Flask, request, jsonify
import hashlib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/generate_id', methods=['POST'])
def generate_id_route():
    if request.method == 'POST':
        aadhar = request.form['aadhar']
        pan = request.form['pan']
        voter = request.form['voter']
        generated_id = generate_id(aadhar, pan, voter)
        return jsonify(generated_id)
    else:
        return "Invalid request method"


def generate_id(aadhar, pan, voter):
    sha256 = hashlib.sha256(aadhar.encode('utf-8')).hexdigest()
    suffix = int(sha256[-8:], 16)
    numbers = str(suffix % 1000000).zfill(6)  # Ensure 6 digits

    generated_id = f'IN{pan[:2]}{numbers}{voter[-2:]}'
    return generated_id


if __name__ == '__main__':
    app.run(debug=True)
