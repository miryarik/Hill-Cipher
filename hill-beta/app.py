from flask import Flask, render_template, request, jsonify
import hill_cipher

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    plaintext = request.json.get('plaintext', '').lower()
    key = request.json.get('key', '')
    block_size = int(request.json.get('block_size', 2))
    encrypted_text = hill_cipher.hill_encrypt(key, plaintext, m=block_size)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    ciphertext = request.json.get('ciphertext', '').lower()
    key = request.json.get('key', '')
    block_size = int(request.json.get('block_size', 2))
    decrypted_text = hill_cipher.hill_decrypt(key, ciphertext, m=block_size)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)