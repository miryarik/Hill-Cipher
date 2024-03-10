const plaintextInput = document.getElementById('plaintext');
const encryptKeyInput = document.getElementById('encrypt_key');
const encryptBlockSizeInput = document.getElementById('encrypt_block_size');
const ciphertextInput = document.getElementById('ciphertext');
const decryptKeyInput = document.getElementById('decrypt_key');
const decryptBlockSizeInput = document.getElementById('decrypt_block_size');
const ciphertextOutput = document.getElementById('ciphertext-output');
const plaintextOutput = document.getElementById('plaintext-output');

function encryptInRealTime() {
    const plaintext = plaintextInput.value.toLowerCase();
    const key = encryptKeyInput.value;
    const blockSize = encryptBlockSizeInput.value;

    if (plaintext && key) {
        fetch('/encrypt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                plaintext,
                key,
                block_size: blockSize
            })
        })
        .then(response => response.json())
        .then(data => {
            ciphertextOutput.value = data.encrypted_text;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } else {
        ciphertextOutput.value = '';
    }
}

function decryptInRealTime() {
    const ciphertext = ciphertextInput.value.toLowerCase();
    const key = decryptKeyInput.value;
    const blockSize = decryptBlockSizeInput.value;

    if (ciphertext && key) {
        fetch('/decrypt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                ciphertext,
                key,
                block_size: blockSize
            })
        })
        .then(response => response.json())
        .then(data => {
            plaintextOutput.value = data.decrypted_text;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } else {
        plaintextOutput.value = '';
    }
}

plaintextInput.addEventListener('input', encryptInRealTime);
encryptKeyInput.addEventListener('input', encryptInRealTime);
encryptBlockSizeInput.addEventListener('input', encryptInRealTime);

ciphertextInput.addEventListener('input', decryptInRealTime);
decryptKeyInput.addEventListener('input', decryptInRealTime);
decryptBlockSizeInput.addEventListener('input', decryptInRealTime);