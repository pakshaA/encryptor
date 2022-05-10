from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
import os


def encrypt(dataFile, publicKeyFile, curr_dirr):
    with open(dataFile, 'rb') as f:
        data = f.read()

    data = bytes(data)

    with open(publicKeyFile, 'rb') as f:
        publicKey = f.read()

    key = RSA.import_key(publicKey)
    sessionKey = os.urandom(16)

    cipher_session_key = PKCS1_OAEP.new(key)
    encrypted_session_key = cipher_session_key.encrypt(sessionKey)

    cipher = AES.new(sessionKey, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    [fileName, fileExtension] = dataFile.split('.')
    encryptedFile = curr_dirr + '/data_encrypted.' + fileExtension
    with open(encryptedFile, 'wb') as f:
        [f.write(x) for x in (encrypted_session_key, cipher.nonce, tag, ciphertext)]


def decrypt(dataFile, privateKeyFile, curr_dirr):
    with open(privateKeyFile, 'rb') as f:
        privateKey = f.read()
        key = RSA.import_key(privateKey)

    with open(dataFile, 'rb') as f:
        encryptedSessionKey, nonce, tag, ciphertext = [f.read(x) for x in (key.size_in_bytes(), 16, 16, -1)]

    cipher_session_key = PKCS1_OAEP.new(key)
    sessionKey = cipher_session_key.decrypt(encryptedSessionKey)

    cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    [fileName, fileExtension] = dataFile.split('.')
    decryptedFile = curr_dirr + '/data_decrypted.' + fileExtension
    with open(decryptedFile, 'wb') as f:
        f.write(data)
